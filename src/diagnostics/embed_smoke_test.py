import os
import numpy as np
from dotenv import load_dotenv
from llama_index.embeddings.siliconflow import SiliconFlowEmbedding

load_dotenv()
emb = SiliconFlowEmbedding(model="BAAI/bge-m3", api_key=os.getenv("SILICONFLOW_API_KEY"))

texts = {
    "中文问题": "如何衡量 AI 产品是否成功",
    "英文同义": "How do you measure whether an AI product is successful",
    "英文无关": "A recipe for braised pork belly with soy sauce",
}
vec = {k: np.array(emb.get_text_embedding(v)) for k, v in texts.items()}
cos = lambda a, b: float(a @ b / np.linalg.norm(a) / np.linalg.norm(b))

print("向量维度:", len(vec["中文问题"]))
print("中文 vs 英文同义:", round(cos(vec["中文问题"], vec["英文同义"]), 3))
print("中文 vs 英文无关:", round(cos(vec["中文问题"], vec["英文无关"]), 3))