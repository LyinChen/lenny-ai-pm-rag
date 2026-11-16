import json
import re

chunks = [json.loads(l) for l in open("data/processed/chunks.jsonl", encoding="utf-8")]
KEYWORDS = {
    "Q01 值不值得做":   r"worth (building|it)|should we build|prioriti[sz]",
    "Q02 指标":         r"\bevals?\b|north star|\bKPI\b",
    "Q03 PM与工程师":   r"working with (your )?engineers|PM.{0,30}engineer",
    "Q04 需求文档":     r"\bPRD\b|product requirements?",
    "Q05 争取资源":     r"headcount|buy-in|convince|persuade",
    "Q06 幻觉":         r"hallucinat",
    "Q07 交互设计":     r"chat interface|\bUX\b|interaction design",
    "Q08 边界":         r"guardrail|out of scope|boundar",
    "Q09 转型AI PM":    r"AI product manager|\bAI PM\b|transition into|break into",
    "Q10 做原型":       r"prototyp",
    "Q11 AI提效":       r"productivity|copilot|use AI (to|for)",
    "Q12 不确定性":     r"non-?determinis",
    "Q13 人把关":       r"low agency|high control|human[- ]in[- ]the[- ]loop",
    "Q14 用户信任":     r"user trust|trust (in|with) (the )?(AI|model)",
    "Q15 PM能力变化":   r"future of product management|role of (the )?PM",
    "Q16 Duolingo":     r"Duolingo",
    "Q17 Anthropic":    r"Anthropic",
    "Q18 说不":         r"saying no|say no to",
    "Q19 自训还是调用": r"fine-tun|build vs\.? buy|off-the-shelf|foundation model",
    "Q20 PMF":          r"product[- ]market fit|\bPMF\b",
    "Q21 字节":         r"ByteDance|TikTok|Douyin|Doubao",
    "Q22 国内合规":     r"\bChina\b|Chinese|regulat|compliance",
    "Q23 微调":         r"fine-tun",
    "Q24 薪资":         r"salary|compensation|pay band",
    "Q25 跨境电商":     r"cross-border|e-?commerce|Shopify|Temu",
}
for name, pat in KEYWORDS.items():
    hit = [c for c in chunks if re.search(pat, c["text"], re.I)]
    print(f"{name:14s} {len(hit):4d} 个块 / {len({c['doc_id'] for c in hit}):2d} 篇文档")