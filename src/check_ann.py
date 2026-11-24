import numpy as np

import retrieval as R
from eval_retrieval import load_questions

q = next(x["q"] for x in load_questions() if x["id"] == "Q19")
cid = "boris-cherny-0045"

got = R.col.get(include=["embeddings"])
ids = got["ids"]
E = np.array(got["embeddings"], dtype=float)
E /= np.linalg.norm(E, axis=1, keepdims=True)
idx = ids.index(cid)

for t in range(12):
    v = np.array(R.emb.get_query_embedding(q), dtype=float)
    v /= np.linalg.norm(v)
    sims = E @ v
    exact = int((sims > sims[idx]).sum()) + 1
    res = R.col.query(query_embeddings=[v.tolist()], n_results=100, include=[])["ids"][0]
    ann = res.index(cid) + 1 if cid in res else None
    print(f"第 {t + 1} 次  精确位次 {exact}  |  Chroma 前 100 内位次 {ann}")