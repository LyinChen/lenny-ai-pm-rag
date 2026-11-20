import json
import re

key = json.load(open("data/eval/spotcheck_key.json", encoding="utf-8"))
text = open("docs/judge-spotcheck.md", encoding="utf-8").read()
LABEL = re.compile(r"部分相关|相关|无关")
mine = {}
for block in text.split("## [#")[1:]:
    k = block.split("]")[0]
    m = re.search(r"你的判断：(.*?)(?=\n## \[#|\Z)", block, re.S)
    if m and LABEL.search(m.group(1)):
        mine[k] = LABEL.search(m.group(1)).group(0)

print(f"已解析 {len(mine)} / {len(key)} 条")
exact = binary = 0
for k in sorted(mine, key=int):
    a, b = mine[k], key[k]["label"]
    exact += a == b
    binary += (a == "相关") == (b == "相关")
    print(f"#{k:>2} 你:{a}  大模型:{b}{'' if a == b else '  ← 不一致'}")
print(f"三分类一致 {exact}/{len(mine)}；“是否相关”一致 {binary}/{len(mine)}")