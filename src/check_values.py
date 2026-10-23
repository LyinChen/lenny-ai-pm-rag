from pathlib import Path
from collections import Counter
import re

ROOT = Path("data/raw")
SKIP = {"readme.md", "license.md"}
types, bad_date, empty = Counter(), [], []

for f in sorted(ROOT.rglob("*.md")):
    if f.name.lower() in SKIP:
        continue
    head = f.read_text(encoding="utf-8").split("---")[1]
    meta = {}
    for line in head.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    types[meta.get("type", "")] += 1
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", meta.get("date", "")):
        bad_date.append(f.name)
    for k in ("title", "type", "date"):
        if not meta.get(k):
            empty.append((f.name, k))

print("type 取值:", dict(types))
print("日期格式异常:", bad_date)
print("关键字段为空:", empty)