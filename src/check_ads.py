import re
from pathlib import Path
from prepare_data import parse_doc, parse_turns, wc

MARK = re.compile(
    r"supporting sponsor|today's sponsor|word from our|brought to you by|our sponsors", re.I)
files_hit, hits = set(), []
for f in sorted(Path("data/raw/podcasts").glob("*.md")):
    _, body = parse_doc(f.read_text(encoding="utf-8").replace("\r\n", "\n"))
    for i, t in enumerate(parse_turns(body)):
        if MARK.search(t["text"]):
            files_hit.add(f.name)
            hits.append((f.name, i, t))

print("命中文件数:", len(files_hit), "命中段数:", len(hits))
for name, i, t in hits[:10]:
    txt = t["text"]
    print(f"\n--- {name} 第{i}段 {t['speaker']} ({t['ts']}) 共{wc(txt)}词")
    print("开头:", txt[:200])
    print("结尾:", txt[-200:])