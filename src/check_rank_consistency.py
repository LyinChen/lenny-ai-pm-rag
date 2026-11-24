import sys

import retrieval as R
from eval_retrieval import load_questions

qid, cid = sys.argv[1], sys.argv[2]
q = next(x["q"] for x in load_questions() if x["id"] == qid)
for n in (100, 300, 100, 300):
    ids = [c for c, _ in R.dense(q, n)]
    print(f"取前 {n}：{cid} 位次 =", ids.index(cid) + 1 if cid in ids else "不在")