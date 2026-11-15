"""Day 5 步骤2：检索基线评测（只新增文件，不修改 src/ 与既有 docs/）

算 Hit Rate@5 / @10、MRR，按中英双问分别统计；并对库外问题取距离分布，
给出拒答阈值的候选值及其代价。

用法: python eval/eval_retrieval.py
输出: eval/report-day5-baseline.md
"""
import json
import os
import time
from pathlib import Path

import chromadb
from dotenv import load_dotenv
from llama_index.embeddings.siliconflow import SiliconFlowEmbedding

ROOT = Path(__file__).resolve().parent.parent
QS = ROOT / "eval/questions.jsonl"
CACHE = ROOT / "eval/.query_cache.json"
OUT = ROOT / "eval/report-day5-baseline.md"
TOP_N = 10
COLLECTION = "lenny_chunks"

load_dotenv(ROOT / ".env")
emb = SiliconFlowEmbedding(model="BAAI/bge-m3", api_key=os.getenv("SILICONFLOW_API_KEY"))
col = chromadb.PersistentClient(path=str(ROOT / "chroma_db")).get_collection(COLLECTION)

cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}


def vec(text):
    if text not in cache:                      # 逐条缓存，重跑评测不再重复付费
        for attempt in range(4):
            try:
                cache[text] = emb.get_query_embedding(text)
                break
            except Exception as e:
                wait = 3 * 2 ** attempt
                print(f"  embedding 失败 {str(e)[:60]}，{wait}s 后重试")
                time.sleep(wait)
        else:
            raise SystemExit("embedding 连续失败")
        CACHE.write_text(json.dumps(cache))
    return cache[text]


def retrieve(text, n=TOP_N):
    r = col.query(query_embeddings=[vec(text)], n_results=n,
                  include=["metadatas", "distances"])
    return list(zip(r["ids"][0], r["distances"][0], r["metadatas"][0]))


qs = [json.loads(l) for l in open(QS, encoding="utf-8")]
lib = [q for q in qs if q["in_library"]]
oob = [q for q in qs if not q["in_library"]]

rows = []
for q in lib:
    res = {}
    for lang in ("zh", "en"):
        res[lang] = retrieve(q[lang])
    first_rank, best_d = {}, {}
    for lang in ("zh", "en"):
        ranks = [i + 1 for i, (cid, _, _) in enumerate(res[lang]) if cid in q["gold_ids"]]
        first_rank[lang] = ranks[0] if ranks else None
        best_d[lang] = res[lang][0][1]
    gold_doc = q["gold_ids"][0].rsplit("-", 1)[0]   # 块 ID 去掉序号即文档 ID
    hit5_doc = {lang: any(m["source_doc"] == gold_doc for _, _, m in res[lang][:5])
                for lang in ("zh", "en")}
    hit5 = {lang: (first_rank[lang] or 99) <= 5 for lang in ("zh", "en")}
    rows.append({
        "q": q, "res": res, "first_rank": first_rank, "best_d": best_d,
        "hit5": hit5, "hit5_any": hit5["zh"] or hit5["en"],
        "hit5_doc": hit5_doc, "hit5_doc_any": hit5_doc["zh"] or hit5_doc["en"],
        "hit10": {lang: (first_rank[lang] or 99) <= 10 for lang in ("zh", "en")},
        "mrr": sum(1 / first_rank[l] if first_rank[l] else 0 for l in ("zh", "en")) / 2,
        "hit5_or": hit5["zh"] or hit5["en"],
    })

n = len(rows)
hit5_zh = sum(r["hit5"]["zh"] for r in rows) / n
hit5_en = sum(r["hit5"]["en"] for r in rows) / n
hit5_any = sum(r["hit5_any"] for r in rows) / n
hit5_doc_zh = sum(r["hit5_doc"]["zh"] for r in rows) / n
hit5_doc_en = sum(r["hit5_doc"]["en"] for r in rows) / n
hit5_doc_any = sum(r["hit5_doc_any"] for r in rows) / n
hit10_zh = sum(r["hit10"]["zh"] for r in rows) / n
hit10_en = sum(r["hit10"]["en"] for r in rows) / n
mrr = sum(r["mrr"] for r in rows) / n

oob_d = []
for q in oob:
    oob_d.append((q["id"], q["zh"], retrieve(q["zh"], 1)[0][1],
                  retrieve(q["en"], 1)[0][1]))
lib_best = [(r["q"]["id"], min(r["best_d"]["zh"], r["best_d"]["en"])) for r in rows]

lines = ["# Day 5 检索基线评测（未调优，纯 bge-m3 向量检索）\n",
         f"- 题集：库内 {n} 题 × 中英双问；库外 {len(oob)} 题",
         f"- 索引：`{COLLECTION}`，余弦距离，Top-{TOP_N}",
         "- 判分：Top-5 内出现任一 gold 块即算命中\n",
         "## 一、基线成绩\n",
         "| 指标 | 数值 | PRD 目标 | 结论 |",
         "|---|---|---|---|",
         f"| Hit Rate@5（中文提问） | **{hit5_zh:.0%}** | ≥80% | {'✅' if hit5_zh >= .8 else '❌'} |",
         f"| Hit Rate@5（英文提问） | **{hit5_en:.0%}** | ≥80% | {'✅' if hit5_en >= .8 else '❌'} |",
         f"| Hit Rate@5（任一中英命中） | **{hit5_any:.0%}** | ≥80% | {'✅' if hit5_any >= .8 else '❌'} |",
         f"| Hit Rate@10（中文 / 英文） | {hit10_zh:.0%} / {hit10_en:.0%} | — | 看召回天花板 |",
         f"| **文档级 Hit@5**（任一中英） | **{hit5_doc_any:.0%}** | — | 命中正确文档但块不对 |",
         f"| 文档级 Hit@5（中文 / 英文） | {hit5_doc_zh:.0%} / {hit5_doc_en:.0%} | — | 跨语言差距 |",
         f"| MRR（中英平均） | {mrr:.3f} | — | 命中位置是否靠前 |\n"]

lines.append("## 二、逐题明细\n")
lines.append("| 题 | 中文首命中 | 英文首命中 | 中文 Top1 距离 | 英文 Top1 距离 | 文档级命中(中/英) |")
lines.append("|---|---|---|---|---|---|")
for r in rows:
    lines.append("| {} {} | {} | {} | {:.3f} | {:.3f} | {} / {} |".format(
        r["q"]["id"], r["q"]["zh"][:22],
        r["first_rank"]["zh"] or "未命中",
        r["first_rank"]["en"] or "未命中",
        r["best_d"]["zh"], r["best_d"]["en"],
        "✅" if r["hit5_doc"]["zh"] else "✗",
        "✅" if r["hit5_doc"]["en"] else "✗"))

miss = [r for r in rows if not r["hit5_or"]]
lines.append(f"\n## 三、失败案例（中英都未进 Top-5）：{len(miss)} 题\n")
lines.append("区分两类：**文档没召回**（检索真跑偏）/ **文档召回但块不对**（切块粒度问题）\n")
for r in miss:
    kind = "文档召回但块不对 ⚠️" if r["hit5_doc_any"] else "文档未召回 ❌"
    lines.append(f"### {r['q']['id']} · {r['q']['zh']} —— {kind}")
    lines.append(f"- gold: {', '.join(x[-4:] for x in r['q']['gold_ids'])}")
    for lang in ("zh", "en"):
        lines.append(f"- {lang} 取回 Top-5：")
        for i, (cid, d, m) in enumerate(r["res"][lang][:5], 1):
            mark = "★" if cid in r["q"]["gold_ids"] else " "
            lines.append(f"  - {i}.{mark} {d:.3f} `{cid[-4:]}` {m['title'][:34]}")
    lines.append("")

half = [r for r in rows if r["hit5_or"] and not (r["hit5"]["zh"] and r["hit5"]["en"])]
lines.append(f"## 四、只有一种语言命中的题：{len(half)} 题（跨语言短板）\n")
for r in half:
    lines.append(f"- {r['q']['id']} {r['q']['zh'][:26]}：中={r['first_rank']['zh'] or '✗'} "
                 f"英={r['first_rank']['en'] or '✗'}")
lines.append("")

lines.append("## 五、库内 vs 库外的距离分布（拒答阈值依据）\n")
lines.append("| 库内（题） | 最佳 Top1 距离 |  | 库外（题） | 中文 Top1 | 英文 Top1 |")
lines.append("|---|---|---|---|---|---|")
for i in range(max(len(lib_best), len(oob_d))):
    a = f"| {lib_best[i][0]} | {lib_best[i][1]:.3f} |" if i < len(lib_best) else "|  |  |"
    b = (f"  | {oob_d[i][0]} {oob_d[i][1][:10]} | {oob_d[i][2]:.3f} | {oob_d[i][3]:.3f} |"
         if i < len(oob_d) else "  |  |  |  |")
    lines.append(a + b)

lines.append("\n### 阈值候选（规则：最佳 Top1 距离 > 阈值 → 判为库外，直接拒答）\n")
lines.append("| 阈值 | 库内被误拒（漏答） | 库外被误答（该拒没拒） |")
lines.append("|---|---|---|")
for t in (0.42, 0.45, 0.48, 0.50, 0.55, 0.60):
    wrong_reject = sum(1 for _, d in lib_best if d > t) / len(lib_best)
    wrong_answer = sum(1 for x in oob_d if max(x[2], x[3]) <= t) / len(oob_d)
    lines.append(f"| {t:.2f} | {wrong_reject:.0%} | {wrong_answer:.0%} |")

lines.append("\n## 六、判读要点\n")
lines.append("- 若「任一中英命中」明显高于单语，说明问题不在向量能力，而在**中文问句与英文原文的表述差异**，"
             "优先做查询改写/翻译，而不是继续换模型。")
lines.append("- 若 Hit@10 远高于 Hit@5，说明**答案在库里但排序不行**，优先加 rerank 或混合检索。")
lines.append("- 若两语都稳定不命中，且 gold 距离 > 0.6，可能是**切块或问题太笼统**，需回到切块层检查。")

OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"报告：{OUT.relative_to(ROOT)}")
print(f"Hit@5  中 {hit5_zh:.0%} | 英 {hit5_en:.0%} | 任一 {hit5_any:.0%}   MRR {mrr:.3f}")
print(f"文档级 Hit@5 中 {hit5_doc_zh:.0%} | 英 {hit5_doc_en:.0%} | 任一 {hit5_doc_any:.0%}")
print(f"块级 Hit@10 中 {hit10_zh:.0%} | 英 {hit10_en:.0%}")
print("失败题中：文档召回但块不对 %d 题；文档未召回 %d 题" % (
    sum(1 for r in miss if r["hit5_doc_any"]),
    sum(1 for r in miss if not r["hit5_doc_any"])))
print("库内最佳距离区间: %.3f ~ %.3f" % (min(d for _, d in lib_best), max(d for _, d in lib_best)))
print("库外 Top1 距离区间: 中 %.3f ~ %.3f | 英 %.3f ~ %.3f" % (
    min(x[2] for x in oob_d), max(x[2] for x in oob_d),
    min(x[3] for x in oob_d), max(x[3] for x in oob_d)))
