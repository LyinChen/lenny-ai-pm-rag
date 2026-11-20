import json
import os
import re
import time

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
_client = OpenAI(api_key=os.getenv("SILICONFLOW_API_KEY"),
                 base_url="https://api.siliconflow.cn/v1")
CHAT_MODEL = "deepseek-ai/DeepSeek-V3.2"       # 模型名来自你的账单
USAGE = {"in": 0, "out": 0}                    # 累计用量，用来核对费用


def chat_json(system, user, model=CHAT_MODEL, retries=4):
    for i in range(retries):
        try:
            r = _client.chat.completions.create(
                model=model, temperature=0, max_tokens=400,
                messages=[{"role": "system", "content": system},
                          {"role": "user", "content": user}])
            if r.usage:
                USAGE["in"] += r.usage.prompt_tokens
                USAGE["out"] += r.usage.completion_tokens
            return json.loads(re.search(r"\{.*\}", r.choices[0].message.content, re.S).group(0))
        except Exception as e:
            print("  调用出错，重试:", str(e)[:80])
            time.sleep(3 * 2 ** i)
    raise RuntimeError("大模型调用连续失败")