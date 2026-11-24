import retrieval as R
from eval_retrieval import load_questions

cid = "boris-cherny-0045"
q = next(x["q"] for x in load_questions() if x["id"] == "Q19")


def check(tag):
    ids = [c for c, _ in R.dense(q, 100)]
    print(tag, "→ Boris 位次:", ids.index(cid) + 1 if cid in ids else "不在前 100")


check("步骤 0  只导入 retrieval、eval_retrieval")
from eval_retrieval import load_cache
load_cache()
check("步骤 1  load_cache() 之后")
from pool_rate import probe_ids
check("步骤 2  import pool_rate 之后")
probe_ids()
check("步骤 3  probe_ids() 之后")