import os
from dotenv import load_dotenv
from llama_index.llms.openai_like import OpenAILike
from llama_index.embeddings.siliconflow import SiliconFlowEmbedding

load_dotenv()
key = os.getenv("SILICONFLOW_API_KEY")

llm = OpenAILike(model="deepseek-ai/DeepSeek-V4-Flash",  # 换成模型广场里你选的免费模型名
                 api_base="https://api.siliconflow.cn/v1",
                 api_key=key, is_chat_model=True)
print(llm.complete("用一句话解释RAG").text)

emb = SiliconFlowEmbedding(model="BAAI/bge-m3", api_key=key)
print("向量维度:", len(emb.get_text_embedding("product manager")))