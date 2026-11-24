import sys

import numpy as np

import retrieval as R
from eval_retrieval import load_questions

qid, cid = sys.argv[1], sys.argv[2]
q = next(x["q"] for x in load_questions() if x["id"] == qid)


def rank_of(vec):
    ids = R.col.query(query_embeddings=[vec], n_results=300, include=[])["ids"][0]
    return ids.index(cid) + 1 if cid in ids else None


vecs, ranks = [], []
for _ in range(8):
    v = np.array(R.emb.get_query_embedding(q))     # 同一个问题，重复生成 8 次向量
    vecs.append(v)
    ranks.append(rank_of(v.tolist()))
cos = [float(v @ vecs[0] / np.linalg.norm(v) / np.linalg.norm(vecs[0])) for v in vecs[1:]]
print("同一问题 8 次生成向量后的位次:", ranks)
print("与第 1 次向量的余弦相似度，最小值:", round(min(cos), 6))

same = [rank_of(vecs[0].tolist()) for _ in range(5)]
print("同一个向量查库 5 次的位次:", same)