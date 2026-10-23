from pathlib import Path

ROOT = Path("data/raw")
SKIP = {"readme.md", "license.md"}
no_link, only_post, only_yt, both = [], 0, 0, 0
for f in sorted(ROOT.rglob("*.md")):
    if f.name.lower() in SKIP:
        continue
    head = f.read_text(encoding="utf-8").split("---")[1]
    has_post = "post_url:" in head
    has_yt = "youtube_url:" in head
    if has_post and has_yt: both += 1
    elif has_post: only_post += 1
    elif has_yt: only_yt += 1
    else: no_link.append(f.name)

print("两个链接都有:", both)
print("只有 post_url:", only_post)
print("只有 youtube_url:", only_yt)
print("都没有:", len(no_link))
print(no_link[:10])
print("\n无链接文件的类型:")
from collections import Counter
types = Counter()
for name in no_link:
    f = next(ROOT.rglob(name))
    head = f.read_text(encoding="utf-8").split("---")[1]
    for line in head.splitlines():
        if line.startswith("type:"):
            types[line.split(":", 1)[1].strip().strip('"')] += 1
print(dict(types))