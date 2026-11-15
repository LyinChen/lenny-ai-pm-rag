"""Day 4: 把文本块向量化并存入 Chroma（支持断点续跑）"""
import json
import os
import time
from pathlib import Path

import chromadb
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex
from llama_index.core.schema import TextNode
from llama_index.embeddings.siliconflow import SiliconFlowEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

load_dotenv()
CHUNKS = Path("data/processed/chunks.jsonl")
DB_DIR, COLLECTION, BATCH = "chroma_db", "lenny_chunks", 50
META_KEYS = ("title", "type", "guest", "date", "source_url",
             "speakers", "start_ts", "chunk_index", "words")

embed = SiliconFlowEmbedding(model="BAAI/bge-m3", api_key=os.getenv("SILICONFLOW_API_KEY"))
chunks = [json.loads(l) for l in open(CHUNKS, encoding="utf-8")]

client = chromadb.PersistentClient(path=DB_DIR)
col = client.get_or_create_collection(COLLECTION, metadata={"hnsw:space": "cosine"})
done = set(col.get(include=[])["ids"])
todo = [c for c in chunks if c["chunk_id"] not in done]
print(f"总块数 {len(chunks)}，已入库 {len(done)}，待处理 {len(todo)}")


def to_node(c):
    meta = {k: c[k] for k in META_KEYS}
    meta["source_doc"] = c["doc_id"]      # 不能叫 doc_id，会被框架覆盖
    node = TextNode(id_=c["chunk_id"], text=c["text"], metadata=meta)
    node.excluded_embed_metadata_keys = list(meta)
    node.excluded_llm_metadata_keys = ["source_doc", "chunk_index", "words"]
    return node


index = VectorStoreIndex.from_vector_store(
    ChromaVectorStore(chroma_collection=col), embed_model=embed)

start = time.time()
for i in range(0, len(todo), BATCH):
    batch = [to_node(c) for c in todo[i:i + BATCH]]
    for attempt in range(5):
        try:
            index.insert_nodes(batch)
            break
        except Exception as e:      # 限流或服务繁忙时等待后重试
            wait = 5 * 2 ** attempt
            print(f"  出错：{str(e)[:100]}，{wait} 秒后重试")
            time.sleep(wait)
    else:
        raise SystemExit("连续失败，请稍后重新运行本脚本（会自动接着做）")
    print(f"  进度 {min(i + BATCH, len(todo))}/{len(todo)}  已用 {int(time.time() - start)} 秒")

print(f"完成。库内总数: {col.count()}，本次新增 {len(todo)} 块，用时 {int(time.time() - start)} 秒")