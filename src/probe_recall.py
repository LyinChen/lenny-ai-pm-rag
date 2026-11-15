"""诊断：答案在库里吗？如果在，检索排第几？
用法: python src/probe_recall.py "问题" "关键词正则"
"""
import json
import os
import re
import sys

import chromadb
from dotenv import load_dotenv
from llama_index.embeddings.siliconflow import SiliconFlowEmbedding

load_dotenv()
question, pattern = sys.argv[1], re.compile(sys.argv[2], re.I)

chunks = {}
for line in open("data/processed/chunks.jsonl", encoding="utf-8"):
    c = json.loads(line)
    chunks[c["chunk_id"]] = c
hits = {cid for cid, c in chunks.items() if pattern.search(c["text"])}
docs = {chunks[i]["doc_id"] for i in hits}
print(f"全库含关键词的块: {len(hits)} 个，分布在 {len(docs)} 篇文档")

emb = SiliconFlowEmbedding(model="BAAI/bge-m3", api_key=os.getenv("SILICONFLOW_API_KEY"))
col = chromadb.PersistentClient(path="chroma_db").get_collection("lenny_chunks")
N = 50
r = col.query(query_embeddings=[emb.get_query_embedding(question)],
              n_results=N, include=["distances"])
ranks = [(i + 1, cid, d) for i, (cid, d) in
         enumerate(zip(r["ids"][0], r["distances"][0])) if cid in hits]
print(f"检索前 {N} 名里含关键词的块: {len(ranks)} 个；不在前 {N} 的: {len(hits) - len(ranks)} 个")
for rank, cid, d in ranks[:8]:
    c = chunks[cid]
    m = pattern.search(c["text"])
    s = max(0, m.start() - 80)
    print(f"  第{rank}名 距离{d:.3f} | {c['title'][:30]} | ...{c['text'][s:m.end() + 80]!r}")