"""Day 6 体检（零评审版）：只测"重排把块挪到哪"，不新增任何块级评审。

能回答：无关块有没有被挤出前 5？相关块有没有被保住？前 5 换了几个新块？
不能回答：换进来的新块好不好（需要新评审，留到回答级验收）。

用法：
  python src/rank_check.py                  全量 20 题，池 20
  LIMIT=3 python src/rank_check.py          冒烟：只看能否跑通，数字不作结论
  POOL=30 python src/rank_check.py          换池大小
  SKIP_PROBES=1 python src/rank_check.py    块号核对不过时，先跳过已知好块体检
"""
import os
import time
from pathlib import Path

import rerank as RK
import retrieval as R
from eval_retrieval import load_cache, load_questions
from pool_rate import probe_ids

POOL = int(os.getenv("POOL", "20"))
LIMIT = int(os.getenv("LIMIT", "20"))
SKIP_PROBES = os.getenv("SKIP_PROBES") == "1"
ONLY = [x for x in os.getenv("ONLY", "").split(",") if x]
OUT = Path("docs/day6-results-partial.md" if ONLY else "docs/day6-results.md")


def main():
    questions = load_questions()
    QS = {q["id"]: q["q"] for q in questions}
    lib = [q["id"] for q in questions if q["type"].startswith("库内")][:LIMIT]
    if ONLY:
        lib = [q for q in lib if q in ONLY]
    cache = load_cache()

    if SKIP_PROBES:
        print("已跳过已知好块体检（SKIP_PROBES=1）")
        probes = []
    else:
        probes = probe_ids()      # 块号对不上会在这里直接报错，且发生在任何接口调用之前

    rows, probe_rows, lat, tops = [], [], [], []

    for qid in lib:
        q = QS[qid]
        print("处理", qid, q[:22])

        deep = [c for c, _ in R.dense(q, 100)]      # 取前 100；前 5 和候选池都从这里切
        a5 = deep[:5]                               # 改进前的前 5，与 Day 5 的 A 近似同源
        labels = [cache.get(f"{qid}|{c}", {}).get("label", "未评") for c in a5]

        t0 = time.time()
        ranked = RK.rerank(q, deep[:POOL])          # 对候选池重排
        lat.append(time.time() - t0)
        tops.append((ranked[0][1], ranked[-1][1]))  # 第 1 名与最后一名的重排分数

        rr = {c: i for i, (c, _) in enumerate(ranked, 1)}   # 重排后位次（从 1 起）
        after = [rr.get(c) for c in a5]                     # None 表示不在候选池内
        new = sum(1 for c, _ in ranked[:5] if c not in a5)  # 前 5 里的新面孔个数
        rows.append({"qid": qid, "labels": labels, "after": after, "new": new})

        for pq, cid, note in probes:
            if pq == qid:
                p = deep.index(cid) + 1 if cid in deep else None
                probe_rows.append((qid, cid, note, p, rr.get(cid)))

    # ---------- 汇总 ----------
    n = len(rows)
    hit = sum("相关" in r["labels"] for r in rows)
    strict = sum(r["labels"].count("相关") for r in rows) / (5 * n)
    mrr = sum(1 / (r["labels"].index("相关") + 1) if "相关" in r["labels"] else 0
              for r in rows) / n
    unrated = sum(r["labels"].count("未评") for r in rows)

    pairs = [(lab, af) for r in rows for lab, af in zip(r["labels"], r["after"])]
    rel_n = sum(1 for lab, _ in pairs if lab == "相关")
    rel_kept = sum(1 for lab, af in pairs if lab == "相关" and af is not None and af <= 5)
    irr_n = sum(1 for lab, _ in pairs if lab == "无关")
    irr_out = sum(1 for lab, af in pairs if lab == "无关" and (af is None or af > 5))
    new_total = sum(r["new"] for r in rows)

    usage = getattr(RK, "USAGE", {}).get("in")
    top_lo, top_hi = min(t[0] for t in tops), max(t[0] for t in tops)
    bot_lo, bot_hi = min(t[1] for t in tops), max(t[1] for t in tops)

    out = ["# Day 6 重排记录（零评审版）\n",
           "本文件不含任何新评审：位移用的是 Day 5 缓存里已有的块标签（v2 标准）。\n",
           "## 1. 口径自检\n"]
    if n == 20:
        out += [f"- A5 从缓存计算：Hit {hit}/{n}（{hit / n:.0%}）/ 严格 P {strict:.0%} / MRR {mrr:.2f}",
                "- 应与 day5-results-v2 的 A 列（60% / 20% / 0.43）基本一致。"
                "向量检索有 0.001 级浮动，前 5 可能换一块，差一格算正常；差得多说明缓存或代码被改过。"]
    else:
        out += [f"- 本次只跑了 {n} 题，自检数字不适用，只用来确认流程能跑通。"]
    out += [f"- 前 5 里缺评审标签的块：{unrated} 个（不为 0 说明这次的前 5 与缓存的 A 不完全一致）\n",
            f"## 2. 位移体检（池 {POOL}，样本 {n} 题）\n",
            f"- 已知相关块：{rel_kept}/{rel_n} 仍在前 5",
            f"- 已知无关块：{irr_out}/{irr_n} 被挤出前 5",
            f"- 前 5 新面孔：共 {new_total} 个（{n} 题 × 5 = {5 * n} 个位置）",
            f"- 重排耗时：平均 {sum(lat) / len(lat):.2f} 秒，最长 {max(lat):.2f} 秒",
            f"- 重排分数范围：第 1 名 {top_lo:.4f}-{top_hi:.4f}；最后一名 {bot_lo:.6f}-{bot_hi:.4f}",
            f"- 重排输入 token：{usage if usage is not None else '未记录（rerank.py 未加用量补丁）'}",
            "- 注意：相关块只有 20 个、无关块只有 10 个，每个块都占很大比重，只看个数，不折算成百分比。\n",
            "## 3. 逐题\n",
            "| 题 | A5 标签分布 | 原前 5 重排后位次（— 为池外） | 前 5 新面孔 |",
            "|---|---|---|---|"]
    for r in rows:
        dist = " / ".join(f"{k}{r['labels'].count(k)}"
                          for k in ("相关", "部分相关", "无关", "未评")
                          if r["labels"].count(k))
        after = " ".join(str(a) if a else "—" for a in r["after"])
        out.append(f"| {r['qid']} | {dist} | {after} | {r['new']}/5 |")

    if probes:
        out += ["\n## 4. 已知好块体检（向量位次 / 重排后位次）\n",
                "说明：这批块是看过排名之后挑的，有选择偏差，只作体检，不当成绩。\n",
                "| 题 | 块 | 说明 | 向量位次 | 重排后 |",
                "|---|---|---|---|---|"]
        for qid, cid, note, p, rr_ in probe_rows:
            out.append(f"| {qid} | {cid.split('-')[-1]} | {note} | {p or '—'} | {rr_ or '—'} |")
    else:
        out += ["\n## 4. 已知好块体检\n", "本次已跳过。"]

    out += ["\n## 5. 结论范围（别越界引用）\n",
            "- 本表能说明：无关块是否被清出前 5、相关块是否被保住、重排改动有多大。",
            "- 本表不能说明：新进前 5 的块是否更好。要证明必须评块，留到回答级验收。",
            "- 重排分数只用于排序，绝对值不可解释，不可作拒答阈值；拒答只用向量最近距离。",
            "- 金额：本次只有重排调用，没有评审费用，价格以硅基流动账单为准。"]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(out), encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    main()
