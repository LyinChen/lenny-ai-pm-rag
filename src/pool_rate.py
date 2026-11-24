"""Day 6 第一步：已知好内容的进池率。只做向量查询，不调评审、不花钱。"""
import re

import retrieval as R
from eval_retrieval import load_questions

# (题号, 标题关键词, 起始时间戳, 块首正则, 期望块号, 说明)
PROBES = [
    ("Q01", "Aishwarya", "01:03:25", None,
     "aishwarya-naresh-reganti--kiriti-badam-0038", "想清楚能否解决真问题"),
    ("Q01", "Father of the iPod", "00:20:44", None,
     "tony-fadell-0012", "怎么决定什么值得做"),
    ("Q08", "Aishwarya", "00:16:02", None,
     "aishwarya-naresh-reganti--kiriti-badam-0009", "按风险高低决定是否人工把关"),
    ("Q08", "Aishwarya", "00:56:17", None,
     "aishwarya-naresh-reganti--kiriti-badam-0034", "按动作数量或话题限制自主权"),
    ("Q19", "Boris Cherny", "01:04:06", None,
     "boris-cherny-0045", "押注通用模型，别微调"),
    ("Q19", "Why LinkedIn", "00:38:49", None,
     "tomer-cohen-0022", "微调可做成团队战略（观点对立）"),
    ("Q02", "Beyond vibe checks", "", r"What exactly are evals",
     "beyond-vibe-checks-a-pms-complete-guide-to-evals-0002", "evals 到底是什么"),
    ("Q02", "Beyond vibe checks", "", r"Looking ahead",
     "beyond-vibe-checks-a-pms-complete-guide-to-evals-0010", "Day5 记的向量第 2 名块"),
]


def resolve(qid, kw, ts, rx, want):
    pat = re.compile(rx, re.I) if rx else None
    # 新闻稿没有时间戳，用"块首 80 字"定位：切块重叠会把下一块的开头粘到上一块尾部
    ids = [c["chunk_id"] for c in R.CHUNKS
           if kw.lower() in c["title"].lower()
           and (c["start_ts"] == ts if ts else pat.search(c["text"][:80]))]
    if ids != [want]:
        raise SystemExit(
            f"「{qid} {kw} {ts or rx}」解析到 {ids}，期望 [{want}]。\n"
            f"块号可能因清洗/切块规则变化而偏移，请人工核对后改期望值，不要跳过。")
    return ids[0]


def probe_ids():
    return [(q, resolve(q, kw, ts, rx, want), note)
            for q, kw, ts, rx, want, note in PROBES]


if __name__ == "__main__":
    QS = {q["id"]: q["q"] for q in load_questions()}
    probe = probe_ids()
    ranks = {}
    for qid, cid, note in probe:
        if qid not in ranks:
            ranks[qid] = {c: i for i, (c, _) in enumerate(R.dense(QS[qid], 300), 1)}
        print(f"{qid} | {note} | 向量位次 {ranks[qid].get(cid, '300 名外')}")

    print(f"\n共 {len(probe)} 个已知好块")
    for n in (20, 30, 50, 100):
        hit = sum(1 for qid, cid, _ in probe if (ranks[qid].get(cid) or 9999) <= n)
        print(f"  池 {n}: {hit}/{len(probe)}")
