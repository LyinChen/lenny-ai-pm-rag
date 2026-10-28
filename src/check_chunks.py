import json
from collections import Counter

chunks = [json.loads(l) for l in open("data/processed/chunks.jsonl", encoding="utf-8")]
order = ["<50", "50-99", "100-199", "200-299", "300-375", ">375"]
bins = Counter()
for c in chunks:
    w = c["words"]
    k = ("<50" if w < 50 else "50-99" if w < 100 else "100-199" if w < 200
         else "200-299" if w < 300 else "300-375" if w <= 375 else ">375")
    bins[k] += 1
for k in order:
    print(f"{k:8s} {bins[k]}")

print("\n最短的 5 个块:")
for c in sorted(chunks, key=lambda x: x["words"])[:5]:
    print(c["words"], c["chunk_id"], "|", c["text"][:120].replace("\n", " "))