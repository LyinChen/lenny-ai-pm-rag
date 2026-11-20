import json
import os
import re

import chromadb
from dotenv import load_dotenv
from llama_index.embeddings.siliconflow import SiliconFlowEmbedding
from rank_bm25 import BM25Okapi

from llm import chat_json

load_dotenv()
emb = SiliconFlowEmbedding(model="BAAI/bge-m3", api_key=os.getenv("SILICONFLOW_API_KEY"))
col = chromadb.PersistentClient(path="chroma_db").get_collection("lenny_chunks")
CHUNKS = [json.loads(l) for l in open("data/processed/chunks.jsonl", encoding="utf-8")]
BY_ID = {c["chunk_id"]: c for c in CHUNKS}

STOP = set("the a an and or of to in on for is are was were be been it that this with as at by "
           "from i you we they he she not but so if do does did have has had can will would "
           "just like".split())


def tokenize(text):
    text = re.sub(r"\(\d\d:\d\d:\d\d\)", " ", text.lower())      # 去掉时间戳
    return [t for t in re.findall(r"[a-z0-9]+", text) if t not in STOP]


BM25 = BM25Okapi([tokenize(c["text"]) for c in CHUNKS])

REWRITE_SYS = (
    "You write search queries for a knowledge base of English interviews and articles about "
    "product management and AI products. Given a user's question (it may be in Chinese), write "
    "3 different English search queries that would retrieve passages answering it. Use the "
    "vocabulary practitioners actually use, including synonyms and related phrasings. "
    'Return JSON only: {"queries": ["...", "...", "..."]}')


def rewrite(question):
    out = chat_json(REWRITE_SYS, question)
    qs = [q for q in out.get("queries", []) if isinstance(q, str) and q.strip()]
    return qs[:3] or [question]


def dense(query, n=20):
    r = col.query(query_embeddings=[emb.get_query_embedding(query)], n_results=n,
                  include=["distances"])
    return list(zip(r["ids"][0], r["distances"][0]))


def bm25(query, n=20):
    scores = BM25.get_scores(tokenize(query))
    top = sorted(range(len(scores)), key=lambda i: -scores[i])[:n]
    return [(CHUNKS[i]["chunk_id"], float(scores[i])) for i in top if scores[i] > 0]


def rrf(rank_lists, k=60, top=5):
    score = {}
    for lst in rank_lists:
        for rank, cid in enumerate(lst, 1):
            score[cid] = score.get(cid, 0) + 1 / (k + rank)
    return sorted(score, key=lambda c: -score[c])[:top]


def baseline(question, top=5):
    """改进前：原问题直接做向量检索（Day 4 的做法）"""
    res = dense(question, top)
    return {"ids": [c for c, _ in res], "best_distance": res[0][1]}


def pipeline(question, top=5):
    """改进后：改写成 3 个英文问法，每个问法做向量+关键词两路检索，再合并"""
    qs = rewrite(question)
    lists, best = [], 9.0
    for q in qs:
        d = dense(q)
        best = min(best, d[0][1])
        lists += [[c for c, _ in d], [c for c, _ in bm25(q)]]
    return {"queries": qs, "ids": rrf(lists, top=top), "best_distance": best}