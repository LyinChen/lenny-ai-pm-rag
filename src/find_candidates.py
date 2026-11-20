import re
import sys

import retrieval as R

if len(sys.argv) < 3:
    sys.exit('用法: python src/find_candidates.py "问题" "关键词(正则)"')

q, pat = sys.argv[1], re.compile(sys.argv[2], re.I)
rank = {cid: i for i, (cid, _) in enumerate(R.dense(q, 500), 1)}
hits = sorted((c for c in R.CHUNKS if pat.search(c["text"])),
              key=lambda c: rank.get(c["chunk_id"], 9999))
print(f"含关键词的块共 {len(hits)} 个，按向量排名显示前 8 个\n")
for c in hits[:8]:
    m = pat.search(c["text"])
    s, e = max(0, m.start() - 250), min(len(c["text"]), m.end() + 350)
    print(f"[向量排名 {rank.get(c['chunk_id'], '500以外')}] {c['title'][:40]} | {c['start_ts'] or '-'}")
    print(c["text"][s:e].replace("\n", " "), "\n")