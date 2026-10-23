from pathlib import Path
from collections import Counter

ROOT = Path("data/raw")
SKIP = {"readme.md", "license.md"}
cnt, total = Counter(), 0
for f in ROOT.rglob("*.md"):
    if f.name.lower() in SKIP:
        continue
    text = f.read_text(encoding="utf-8")
    if not text.startswith("---"):
        continue
    total += 1
    head = text.split("---")[1]
    for line in head.splitlines():
        if ":" in line:
            cnt[line.split(":")[0].strip()] += 1

print("有 frontmatter 的文件:", total)
for k, v in cnt.most_common():
    print(f"{k:15s} {v}")