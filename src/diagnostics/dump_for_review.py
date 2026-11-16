import os

import chromadb
from dotenv import load_dotenv
from llama_index.embeddings.siliconflow import SiliconFlowEmbedding

load_dotenv()
emb = SiliconFlowEmbedding(model="BAAI/bge-m3", api_key=os.getenv("SILICONFLOW_API_KEY"))
col = chromadb.PersistentClient(path="chroma_db").get_collection("lenny_chunks")

QUESTIONS = ["怎么给 AI 产品定义成功指标？",
             "How do you define success metrics for AI products?"]
out = ["# Day 4 检索人工评估\n",
       "判断标准：**相关**=能直接回答问题；**部分相关**=沾边但不能回答；**无关**=答非所问\n"]
for q in QUESTIONS:
    r = col.query(query_embeddings=[emb.get_query_embedding(q)], n_results=5,
                  include=["metadatas", "documents", "distances"])
    out.append(f"\n## 问：{q}\n")
    for i, (d, m, t) in enumerate(zip(r["distances"][0], r["metadatas"][0], r["documents"][0]), 1):
        out.append(f"### {i}. 距离 {d:.3f} | {m['title']} | {m['guest'] or '文章'} | {m['start_ts'] or '-'}\n")
        out.append(t + "\n")
        out.append("**判断：** （相关 / 部分相关 / 无关）\n")

open("docs/retrieval-check-day4.md", "w", encoding="utf-8").write("\n".join(out))
print("已生成 docs/retrieval-check-day4.md")