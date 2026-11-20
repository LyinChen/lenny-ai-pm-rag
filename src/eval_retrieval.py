import json
import random
from pathlib import Path

import retrieval as R
from llm import USAGE, chat_json

CACHE = Path("data/eval/judgments.jsonl")
CACHE.parent.mkdir(parents=True, exist_ok=True)

JUDGE_SYS = (
    "你是检索质量评审员。给定一个用户问题和一个知识库段落，判断该段落对回答这个问题的价值。\n"
    "相关：入门产品经理读完这一段，至少能拿到一条可直接照做的具体方法、做法或明确结论。\n"
    "部分相关：主题沾边，但只点明现象、只讲相邻话题，或只有零散信息，拿不到可直接用的做法。\n"
    "无关：主题不同，或只是碰巧出现了相同的词。\n"
    '只输出 JSON：{"label": "相关|部分相关|无关", "reason": "一句话理由"}')


def load_questions():
    qs = []
    for line in open("docs/eval-questions.md", encoding="utf-8"):
        if line.startswith("| Q"):
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            qs.append({"id": c[0], "q": c[1], "type": c[2]})
    return qs


def load_cache():
    cache = {}
    if CACHE.exists():
        for l in open(CACHE, encoding="utf-8"):
            d = json.loads(l)
            cache[d["key"]] = d
    return cache


def judge(cache, qid, q, cid):
    key = f"{qid}|{cid}"
    if key not in cache:                      # 同一个块只评一次，保证两个版本口径一致
        ch = R.BY_ID[cid]
        out = chat_json(JUDGE_SYS, f"问题：{q}\n\n段落（来自《{ch['title']}》）：\n{ch['text']}")
        label = out.get("label", "无关")
        cache[key] = {"key": key, "qid": qid, "cid": cid, "q": q,
                      "label": label if label in ("相关", "部分相关", "无关") else "无关",
                      "reason": out.get("reason", "")}
        with open(CACHE, "a", encoding="utf-8") as f:
            f.write(json.dumps(cache[key], ensure_ascii=False) + "\n")
    return cache[key]["label"]


def metrics(rows):
    n = len(rows)
    hit = sum("相关" in r["labels"] for r in rows) / n
    strict = sum(r["labels"].count("相关") for r in rows) / (5 * n)
    lenient = sum(sum(l != "无关" for l in r["labels"]) for r in rows) / (5 * n)
    mrr = sum(1 / (r["labels"].index("相关") + 1) if "相关" in r["labels"] else 0 for r in rows) / n
    return hit, strict, lenient, mrr


def main():
    cache, rows, dists = load_cache(), [], []
    for q in load_questions():
        if q["type"].startswith("闲聊"):
            continue
        print("处理", q["id"], q["q"][:24])
        A, B = R.baseline(q["q"]), R.pipeline(q["q"])
        dists.append((q["id"], q["type"], A["best_distance"], B["best_distance"]))
        if q["type"].startswith("库内"):
            for name, res in (("A", A), ("B", B)):
                labels = [judge(cache, q["id"], q["q"], cid) for cid in res["ids"]]
                rows.append({"qid": q["id"], "p": name, "labels": labels, "ids": res["ids"],
                             "queries": res.get("queries")})

    out = ["# Day 5 检索评测结果\n",
           "评审：大模型（DeepSeek-V3.2），待人工抽检校准。A=改进前（原问题+向量），B=改进后（改写+混合）\n",
           "## 汇总（20 道库内题）\n", "| 指标 | A 改进前 | B 改进后 |", "|---|---|---|"]
    mA = metrics([r for r in rows if r["p"] == "A"])
    mB = metrics([r for r in rows if r["p"] == "B"])
    for i, name in enumerate(["Hit@5（至少1条相关）", "P@5 严格（只算相关）",
                              "P@5 宽松（含部分相关）", "MRR（首个相关的排名）"]):
        out.append(f"| {name} | {mA[i]:.0%} | {mB[i]:.0%} |" if i < 3 else
                   f"| {name} | {mA[i]:.2f} | {mB[i]:.2f} |")

    out += ["\n## 逐题（相关数/部分相关数）\n", "| 题号 | A | B | 改写出的英文问法 |", "|---|---|---|---|"]
    for qid in sorted({r["qid"] for r in rows}):
        a = next(r for r in rows if r["qid"] == qid and r["p"] == "A")
        b = next(r for r in rows if r["qid"] == qid and r["p"] == "B")
        f = lambda r: f'{r["labels"].count("相关")}/{r["labels"].count("部分相关")}'
        out.append(f"| {qid} | {f(a)} | {f(b)} | {'；'.join(b['queries'])} |")

    out += ["\n## 各题最近距离（Day 8 定拒答规则用）\n",
            "| 题号 | 类型 | A 原问题 | B 改写后（取最小） |", "|---|---|---|---|"]
    out += [f"| {i} | {t} | {a:.3f} | {b:.3f} |" for i, t, a, b in dists]
    out.append(f"\n本次大模型用量：输入 {USAGE['in']} token，输出 {USAGE['out']} token（以账单为准）")
    Path("docs/day5-results.md").write_text("\n".join(out), encoding="utf-8")
    print("\n".join(out[:12]))

    # 抽检：三种判断各取最多 4 条，打乱后让你盲评
    used = {f"{r['qid']}|{c}" for r in rows for c in r["ids"]}
    pool = [cache[k] for k in used]
    random.seed(42)
    pick = []
    for lab in ("相关", "部分相关", "无关"):
        grp = [x for x in pool if x["label"] == lab]
        pick += random.sample(grp, min(4, len(grp)))
    random.shuffle(pick)
    md, key = ["# 评审员抽检（请盲评，先别看大模型的判断）\n",
               "标准：相关=能直接回答；部分相关=沾边但不够；无关=答非所问。在“你的判断：”后面填写。\n"], {}
    for i, x in enumerate(pick, 1):
        ch = R.BY_ID[x["cid"]]
        md += [f"## [#{i}] 问题：{x['q']}", f"来源：《{ch['title']}》 {ch['start_ts'] or ''}\n",
               ch["text"], "\n你的判断：\n"]
        key[str(i)] = {"label": x["label"], "reason": x["reason"]}
    Path("docs/judge-spotcheck.md").write_text("\n".join(md), encoding="utf-8")
    Path("data/eval/spotcheck_key.json").write_text(json.dumps(key, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()