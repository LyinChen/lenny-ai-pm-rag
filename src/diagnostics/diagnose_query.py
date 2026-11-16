import json
import os
import re

import chromadb
from dotenv import load_dotenv
from llama_index.embeddings.siliconflow import SiliconFlowEmbedding

load_dotenv()
emb = SiliconFlowEmbedding(model="BAAI/bge-m3", api_key=os.getenv("SILICONFLOW_API_KEY"))
col = chromadb.PersistentClient(path="chroma_db").get_collection("lenny_chunks")
chunks = [json.loads(l) for l in open("data/processed/chunks.jsonl", encoding="utf-8")]

print("== 资料里有没有这些词 ==")
for kw in ["success metric", "evals", "north star", "KPI", "key metric"]:
    hit = [c for c in chunks if re.search(kw, c["text"], re.I)]
    print(f"{kw:15s} 出现在 {len(hit):3d} 个块 / {len({c['doc_id'] for c in hit}):2d} 篇文档")

QUERIES = [
    "AI product success metrics",
    "how to write evals for an AI product",
    "what metrics should a PM track for an AI feature",
    "north star metric for AI product",
    "怎么给 AI 功能设计评估指标",
]
for q in QUERIES:
    r = col.query(query_embeddings=[emb.get_query_embedding(q)], n_results=5,
                  include=["metadatas", "documents", "distances"])
    print(f"\n问：{q}")
    for d, m, t in zip(r["distances"][0], r["metadatas"][0], r["documents"][0]):
        print(f"  {d:.3f} | {m['title'][:34]} | {m['guest'] or '文章'} | "
              f"{m['start_ts'] or '-'} | {t[:80].replace(chr(10), ' ')}")