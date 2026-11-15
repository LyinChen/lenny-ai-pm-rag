import json
import re

chunks = [json.loads(l) for l in open("data/processed/chunks.jsonl", encoding="utf-8")]
CHECK = {
    "Q14 用户信任": r"trust.{0,60}(AI|model|output|answer)|(AI|model|output|answer).{0,60}trust",
    "Q15 PM能力变化": r"future of product management|role of (the )?PM",
    "Q21 字节（不含TikTok）": r"ByteDance|Douyin|Doubao",
    "Q22 中国": r"\bChina\b|Chinese",
    "Q23 微调": r"fine-tun",
    "Q24 薪资": r"salary|compensation",
    "Q25 跨境电商": r"cross-border|Temu|Shein",
}
for name, pat in CHECK.items():
    rx = re.compile(pat, re.I)
    hits = [(c, rx.search(c["text"])) for c in chunks]
    hits = [(c, m) for c, m in hits if m]
    print(f"\n===== {name}：{len(hits)} 块 / {len({c['doc_id'] for c, _ in hits})} 篇 =====")
    seen = set()
    for c, m in hits:
        if c["doc_id"] in seen:
            continue
        seen.add(c["doc_id"])
        s, e = max(0, m.start() - 120), min(len(c["text"]), m.end() + 120)
        print(f"[{c['title'][:30]} | {c['start_ts'] or '-'}] ...{c['text'][s:e].replace(chr(10), ' ')}...")
        if len(seen) >= 4:
            break