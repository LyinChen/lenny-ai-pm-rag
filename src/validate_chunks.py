import json
import re

chunks = [json.loads(l) for l in open("data/processed/chunks.jsonl", encoding="utf-8")]
checks = {
    "[inaudible] 残留": r"inaudible",
    "图片行残留": r"Image from",
    "招聘广告残留": r"Hiring\?",
    "赞助商句式残留": r"supporting sponsor|today's sponsor|word from our",
    "告别语残留": r"Have a fulfilling",
    "Vanta 整词（需人工看上下文）": r"\bvanta\b",
}
for name, pat in checks.items():
    hits = [c["chunk_id"] for c in chunks if re.search(pat, c["text"], re.I)]
    print("✅" if not hits else "❌", name, len(hits), hits[:6])

short = [c["chunk_id"] for c in chunks if c["words"] < 50]
print("✅" if not short else "❌", "过短块(<50词)", len(short))
print("块总数:", len(chunks))