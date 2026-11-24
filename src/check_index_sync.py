import retrieval as R
from eval_retrieval import load_questions

# 1. 全库比对：Chroma 里存的文本 vs 现在的 chunks.jsonl
got = R.col.get(include=["documents"])
stored = dict(zip(got["ids"], got["documents"]))
diff = [c["chunk_id"] for c in R.CHUNKS if stored.get(c["chunk_id"]) != c["text"]]
print(f"Chroma {len(stored)} 块，chunks.jsonl {len(R.CHUNKS)} 块，文本不一致 {len(diff)} 块", diff[:5])

# 2. Boris 的块：同一个进程里，用两种方式各查一次
cid = "boris-cherny-0045"
q = next(x["q"] for x in load_questions() if x["id"] == "Q19")
print("块号是否存在于 Chroma:", cid in stored)
print("文本含 fine-tune:", "fine-tune" in stored.get(cid, "").lower())
for n in (100, 300):
    ids = [c for c, _ in R.dense(q, n)]
    print(f"R.dense 取前 {n}：", ids.index(cid) + 1 if cid in ids else "不在")