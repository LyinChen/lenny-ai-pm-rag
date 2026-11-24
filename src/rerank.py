"""Day 6：重排序（精排）。这是功能代码，不是实验脚本 —— Day 7 的 answer 直接用它。"""
USAGE = {"in": 0}

def _tokens(d):
    m = d.get("meta")
    if isinstance(m, list):
        m = m[0] if m else {}
    t = d.get("tokens") or (m or {}).get("tokens") or {}
    return t.get("input_tokens", 0)



import os
import time

import requests
from dotenv import load_dotenv

import retrieval as R

load_dotenv()
URL = "https://api.siliconflow.cn/v1/rerank"
MODEL = "BAAI/bge-reranker-v2-m3"
HEADERS = {"Authorization": f"Bearer {os.getenv('SILICONFLOW_API_KEY')}",
           "Content-Type": "application/json"}


def rerank(query, cids, retries=3):
    """把问题和每个候选块拼在一起打分，返回按分数从高到低排好的 (块id, 分数)。

    注意：分数只可用于排序，绝对值无意义（实测正确项 0.027、错误项 1.6e-5）。
    绝不可用作拒答阈值。
    """
    docs = [R.BY_ID[c]["text"] for c in cids]
    body = {"model": MODEL,
            "query": query,
            "documents": docs,
            "top_n": len(docs),
            "return_documents": False}
    for i in range(retries):
        try:
            r = requests.post(URL, headers=HEADERS, json=body, timeout=90)
            r.raise_for_status()
            body_json = r.json()
            USAGE["in"] += _tokens(body_json)
            res = r.json()["results"]
            return [(cids[x["index"]], float(x["relevance_score"])) for x in res]
        except Exception as e:
            print("  重排出错，重试:", str(e)[:90])
            time.sleep(3 * 2 ** i)
    raise RuntimeError("重排序连续失败，检查额度，或稍后重跑（向量接口偶发 data:null 也在重试里兜住）")


def search(question, pool=20, top=6):
    """完整检索链路：粗排 pool 个 → 精排 → 取 top。

    返回值是 Day 7 的输入契约，不要随便改字段名：
      ids           最终 top 个块的 id
      scores        对应重排分数（只可排序，不可阈值）
      best_distance 粗排第一名的向量距离 —— 拒答规则只用这个（临时阈值 0.47）
      pool_ids      进了候选池的全部块 id（排查"天花板"问题用）
    """
    cand = R.dense(question, pool)
    ranked = rerank(question, [c for c, _ in cand])
    return {"ids": [c for c, _ in ranked[:top]],
            "scores": [s for _, s in ranked[:top]],
            "best_distance": cand[0][1],
            "pool_ids": [c for c, _ in cand]}
