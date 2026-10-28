import re
from pathlib import Path
from prepare_data import parse_doc, parse_turns, wc

PAT = re.compile(r"framer\.com|rules and restrictions", re.I)
files, rows = set(), []
for f in sorted(Path("data/raw/podcasts").glob("*.md")):
    _, body = parse_doc(f.read_text(encoding="utf-8").replace("\r\n", "\n"))
    turns = parse_turns(body)
    for i, t in enumerate(turns):
        if PAT.search(t["text"]):
            files.add(f.stem)
            rows.append((f.stem, i, turns))

print("含 Framer 广告的文件数:", len(files))
print("命中段数:", len(rows))
for stem, i, turns in rows[:3]:
    print(f"\n=== {stem} ===")
    for t in turns[max(0, i - 1):i + 2]:
        print(f'[{t["speaker"]} {t["ts"]} {wc(t["text"])}词] {t["text"][:700]}\n')