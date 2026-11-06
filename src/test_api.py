import os
from dotenv import load_dotenv
from llama_index.llms.openai_like import OpenAILike
from llama_index.embeddings.siliconflow import SiliconFlowEmbedding

load_dotenv()
key = os.getenv("SILICONFLOW_API_KEY")
print("Key 已读取:", bool(key), "| 长度:", len(key or ""))

CANDIDATES = [
    "Qwen/Qwen3-8B",
    "Qwen/Qwen3-30B-A3B",
    "deepseek-ai/DeepSeek-V3.2",
    "Qwen/Qwen2.5-7B-Instruct",
]

print("\n--- 对话模型探测 ---")
for m in CANDIDATES:
    try:
        llm = OpenAILike(model=m, api_base="https://api.siliconflow.cn/v1",
                         api_key=key, is_chat_model=True, max_retries=0)
        out = llm.complete("用一句话解释RAG").text
        print("✅ 可用:", m, "|", out[:50].replace("\n", " "))
    except Exception as e:
        print("❌", m, "|", str(e)[:100])

print("\n--- Embedding 探测 ---")
try:
    emb = SiliconFlowEmbedding(model="BAAI/bge-m3", api_key=key)
    print("✅ bge-m3 可用，向量维度:", len(emb.get_text_embedding("product manager")))
except Exception as e:
    print("❌ bge-m3 |", str(e)[:200])