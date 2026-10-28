from pathlib import Path
from prepare_data import parse_doc, parse_turns

targets = {"boris-cherny": "00:01:47", "brian-halligan": "00:01:32",
           "jenny-wen": "00:01:20", "jessica-fain": "00:02:11",
           "sherwin-wu-v2": "00:01:11"}
for stem, ts in targets.items():
    _, body = parse_doc(Path(f"data/raw/podcasts/{stem}.md")
                        .read_text(encoding="utf-8").replace("\r\n", "\n"))
    turns = parse_turns(body)
    i = next(k for k, t in enumerate(turns) if t["ts"] == ts)
    print(f"\n=== {stem} ===")
    for t in turns[i:i + 3]:
        print(f'{t["speaker"]} ({t["ts"]}): {t["text"][:220]}')