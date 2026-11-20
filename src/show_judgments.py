import sys

import retrieval as R
from eval_retrieval import load_cache, load_questions

if len(sys.argv) < 2:
    sys.exit("用法: python src/show_judgments.py Q19")

cache, qid = load_cache(), sys.argv[1]
q = next(x for x in load_questions() if x["id"] == qid)
print("问题:", q["q"])
for rank, cid in enumerate(R.baseline(q["q"])["ids"], 1):
    j, ch = cache.get(f"{qid}|{cid}"), R.BY_ID[cid]
    print(f"\n[{rank}] 评审员判：{j['label'] if j else '未评'} | {ch['title'][:40]} | {ch['start_ts'] or '-'}")
    print("    评审理由:", j["reason"] if j else "-")
    print("    原文:", ch["text"][:400].replace("\n", " "))