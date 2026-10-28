import json
import re

chunks = [json.loads(l) for l in open("data/processed/chunks.jsonl", encoding="utf-8")]

def show(title, pattern, width=160):
    print(f"\n===== {title} =====")
    for c in chunks:
        m = re.search(pattern, c["text"], re.I)
        if m:
            s, e = max(0, m.start() - width), min(len(c["text"]), m.end() + width)
            print(f'[{c["chunk_id"]}] ...{c["text"][s:e]!r}...')

show("Vanta（整词）", r"\bvanta\b")
show("Hiring?", r"Hiring\?")
show("告别语", r"Have a fulfilling")
show("广告网址", r"vanta\.com|\.com/lenny")