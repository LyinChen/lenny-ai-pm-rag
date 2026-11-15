"""Day 5 步骤1：为每道验收题定位候选标准答案块（不修改 src/ 与既有 docs/）

输出 eval/candidates.md，供人工确认 gold_ids。
用法: python eval/gen_candidates.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHUNKS = ROOT / "data/processed/chunks.jsonl"
SEEDS = ROOT / "eval/seeds.jsonl"
OUT = ROOT / "eval/candidates.md"

chunks = [json.loads(l) for l in open(CHUNKS, encoding="utf-8")]
seeds = [json.loads(l) for l in open(SEEDS, encoding="utf-8")]

lines = ["# Day 5 候选标准答案块（待人工确认）\n",
         "规则：只在该题的目标文档内匹配关键句式；一条块算数需能直接回答问题。\n"]
for s in seeds:
    pat = re.compile(s["regex"], re.I)
    cand = [c for c in chunks if c["doc_id"] == s["doc"] and pat.search(c["text"])]
    lines.append(f"\n## {s['id']} · {s['zh']}")
    lines.append(f"- 目标文档：`{s['doc']}` ｜ 候选块 {len(cand)} 个")
    if not cand:
        lines.append("- ⚠️ 无候选，需换文档或换句式")
    for c in cand[:6]:
        hit = pat.search(c["text"])
        snip = c["text"][max(0, hit.start() - 60): hit.end() + 90].replace("\n", " ")
        lines.append(f"- `{c['chunk_id']}` 块#{c['chunk_index']} {c['start_ts'] or '-'} ｜ …{snip}…")

OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"已生成 {OUT.relative_to(ROOT)}，共 {len(seeds)} 题")
miss = [s["id"] for s in seeds
        if not any(re.search(s["regex"], c["text"], re.I)
                   for c in chunks if c["doc_id"] == s["doc"])]
print("无候选的题:", miss or "无")
