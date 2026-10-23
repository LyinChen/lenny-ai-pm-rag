from pathlib import Path
from collections import Counter

ROOT = Path("data/raw")
SKIP = {"readme.md", "license.md"}
files = [f for f in sorted(ROOT.rglob("*.md")) if f.name.lower() not in SKIP]

print("md 文件总数:", len(files))
print("按文件夹统计:", dict(Counter(f.parent.relative_to(ROOT).as_posix() for f in files)))

rows = [(f, len(f.read_text(encoding="utf-8").split())) for f in files]
total = sum(w for _, w in rows)
print("总词数:", total)
print("估算 token（词数÷0.75）:", int(total / 0.75))
print("平均每篇词数:", total // len(rows))

srt = sorted(rows, key=lambda x: x[1])
print("\n最短 3 篇:", [(w, f.name) for f, w in srt[:3]])
print("最长 3 篇:", [(w, f.name) for f, w in srt[-3:]])

print("\n===== 随机看一篇的开头 =====")
sample = srt[len(srt) // 2][0]
print("文件:", sample)
print(sample.read_text(encoding="utf-8")[:1500])

print("\n===== index.json =====")
for p in ROOT.rglob("index.json"):
    print(p, p.stat().st_size, "bytes")