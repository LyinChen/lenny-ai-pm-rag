import re
import sys

import retrieval as R

if len(sys.argv) < 3:
    sys.exit('用法: python src/probe_recall.py "问题" "目标块里的关键词(正则)"')

question, pattern = sys.argv[1], re.compile(sys.argv[2], re.I)
targets = {c["chunk_id"] for c in R.CHUNKS if pattern.search(c["text"])}
print(f"目标块 {len(targets)} 个，来自 {len({R.BY_ID[t]['doc_id'] for t in targets})} 篇文档")
if not targets:
    sys.exit("没有块匹配这个关键词，请换一个")


def first_rank(ids):
    for i, cid in enumerate(ids, 1):
        if cid in targets:
            return i
    return None    # 前 300 名里没有


print("原问题·向量检索，首个目标块排名:", first_rank([c for c, _ in R.dense(question, 300)]))
for rq in R.rewrite(question):
    print(f"改写「{rq[:50]}」 向量:{first_rank([c for c, _ in R.dense(rq, 300)])}"
          f"  关键词:{first_rank([c for c, _ in R.bm25(rq, 300)])}")