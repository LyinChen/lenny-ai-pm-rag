import os

import chromadb
import numpy as np
from dotenv import load_dotenv
from llama_index.embeddings.siliconflow import SiliconFlowEmbedding

load_dotenv()
emb = SiliconFlowEmbedding(model="BAAI/bge-m3", api_key=os.getenv("SILICONFLOW_API_KEY"))
col = chromadb.PersistentClient(path="chroma_db").get_collection("lenny_chunks")
expected = sum(1 for _ in open("data/processed/chunks.jsonl", encoding="utf-8"))

print("入库数量:", col.count(), "预期:", expected, "✅" if col.count() == expected else "❌")
print("集合设置:", col.metadata)

# 元数据完整性：每条都要有有效的 source_doc 和 title
metas = col.get(include=["metadatas"])["metadatas"]
bad = [m for m in metas if m.get("source_doc") in (None, "", "None") or not m.get("title")]
print("元数据完整性:", "✅" if not bad else f"❌ {len(bad)} 条缺失")
print("文档总数:", len({m["source_doc"] for m in metas}), "（预期 60）")


def search(q, n=5):
    qv = emb.get_query_embedding(q)
    r = col.query(query_embeddings=[qv], n_results=n,
                  include=["metadatas", "documents", "distances"])
    return qv, r


def show(q):
    qv, r = search(q)
    print(f"\n问：{q}")
    for d, m, t in zip(r["distances"][0], r["metadatas"][0], r["documents"][0]):
        print(f"  距离{d:.3f} | {m['title'][:36]} | {m['guest'] or '文章'} | "
              f"{m['start_ts'] or '-'} | {t[:70].replace(chr(10), ' ')}")
    return {m["source_doc"] for m in r["metadatas"][0]}


# 1. 距离含义核对
qv, r = search("how to define success metrics for AI products", 1)
vid = r["ids"][0][0]
stored = np.array(col.get(ids=[vid], include=["embeddings"])["embeddings"][0])
q = np.array(qv)
cos = float(q @ stored / np.linalg.norm(q) / np.linalg.norm(stored))
print(f"\n手算 1-余弦 = {1 - cos:.3f}，数据库报告距离 = {r['distances'][0][0]:.3f}")
print("→ 余弦距离 ✅" if abs((1 - cos) - r["distances"][0][0]) < 0.01 else "→ ❌ 不一致")

# 2. 跨语言
a = show("怎么给 AI 产品定义成功指标？")
b = show("How do you define success metrics for AI products?")
print("\n中文命中文档:", sorted(a))
print("英文命中文档:", sorted(b))
print("共同文档:", sorted(a & b))

# 3. 库外问题（Day 5 定拒答阈值用）
show("红烧肉怎么做？")
show("今天北京的天气怎么样？")