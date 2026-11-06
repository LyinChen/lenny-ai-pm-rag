import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
c = OpenAI(api_key=os.getenv("SILICONFLOW_API_KEY"),
           base_url="https://api.siliconflow.cn/v1")
try:
    r = c.embeddings.create(model="BAAI/bge-m3", input="product manager")
    print("✅ bge-m3 可用，维度:", len(r.data[0].embedding))
except Exception as e:
    print("❌", type(e).__name__, "|", str(e)[:300])