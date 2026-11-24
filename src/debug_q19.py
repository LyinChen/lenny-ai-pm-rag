import retrieval as R
from eval_retrieval import load_cache, load_questions
from pool_rate import probe_ids

q = next(x["q"] for x in load_questions() if x["id"] == "Q19")
print("问题原文:", repr(q))
deep = [c for c, _ in R.dense(q, 100)]
cache = load_cache()
print("前 8 名:")
for i, c in enumerate(deep[:8], 1):
    print(" ", i, c, "| 评审标签:", cache.get(f"Q19|{c}", {}).get("label", "未评"))
for p, c, note in probe_ids():
    if p == "Q19":
        print(repr(c), note, "| 在前 100 吗:", c in deep, "| 位次:", deep.index(c) + 1 if c in deep else None)