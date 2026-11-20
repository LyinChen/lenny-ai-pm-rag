# Day 5 检索评测结果


评审：大模型（DeepSeek-V3.2），待人工抽检校准。A=改进前（原问题+向量），B=改进后（改写+混合）
评审标准 v1：段落能直接回答问题才算"相关"。样本 20 题。

## 汇总（20 道库内题）

| 指标 | A 改进前 | B 改进后 |
|---|---|---|
| Hit@5（至少1条相关） | 60% | 60% |
| P@5 严格（只算相关） | 22% | 21% |
| P@5 宽松（含部分相关） | 79% | 85% |
| MRR（首个相关的排名） | 0.44 | 0.42 |

## 逐题（相关数/部分相关数）

| 题号 | A | B | 改写出的英文问法 |
|---|---|---|---|
| Q01 | 0/3 | 0/4 | AI feature launch criteria and evaluation framework；how to assess business value of AI product features；AI product prioritization metrics and ROI analysis |
| Q02 | 0/2 | 0/3 | key performance indicators for AI feature launch；metrics to measure success of AI product functionality；evaluating AI feature performance post-deployment |
| Q03 | 1/3 | 1/3 | product manager and engineering collaboration in AI product development；best practices for PM and engineer partnership in artificial intelligence projects；how product managers work with AI engineers effectively |
| Q04 | 1/1 | 1/1 | differences between AI feature PRD and traditional product requirements document；how to write product requirements for AI features versus standard features；AI product requirements document best practices and differences from conventional PRD |
| Q05 | 2/2 | 1/3 | How to pitch AI feature development to leadership and secure resources；Strategies for advocating AI product initiatives and obtaining executive buy-in；Building business case for AI feature implementation and resource allocation |
| Q06 | 0/5 | 1/4 | mitigate AI hallucination in product design；reduce LLM factual inaccuracy user experience；combat AI misinformation response strategies |
| Q07 | 0/5 | 0/3 | common pitfalls in AI product interaction design；UX challenges in designing AI product workflows；mistakes to avoid in conversational AI interface design |
| Q08 | 0/3 | 0/5 | AI product safety guardrails and content filtering policies；scenarios where AI systems should refuse to answer user queries；ethical boundaries and limitations for AI assistant responses |
| Q09 | 0/4 | 1/4 | product manager transition from traditional to AI products；how traditional product managers can become AI product managers；skills needed for product managers to transition into AI product management |
| Q10 | 2/2 | 3/2 | no-code AI prototype tools for product managers；how to create AI demo without engineering resources；rapid prototyping AI features with mock data |
| Q11 | 3/2 | 1/4 | AI tools for product manager productivity and workflow automation；How product managers leverage artificial intelligence in daily tasks and decision making；Product management efficiency using AI for user research, data analysis, and roadmap prioritization |
| Q12 | 2/1 | 3/2 | managing AI response variability in product design；handling output inconsistency in generative AI products；product strategies for AI response unpredictability |
| Q13 | 3/2 | 3/1 | human-in-the-loop AI implementation strategy；phased rollout vs full automation for AI features；gradual automation approach for AI product features |
| Q14 | 0/4 | 0/5 | AI trust issues user adoption resistance；overcoming skepticism towards AI recommendations；building user confidence in AI system outputs |
| Q15 | 1/4 | 2/3 | How will the core competencies of a product manager evolve in the age of artificial intelligence?；Key skills and responsibilities for product managers in the AI era；Impact of artificial intelligence on product management roles and required capabilities |
| Q16 | 3/2 | 3/2 | Duolingo user growth strategy turnaround；How Duolingo revived its user acquisition and retention；Duolingo product-led growth tactics and user engagement revival |
| Q17 | 1/4 | 0/5 | Anthropic product team structure and workflow；How Anthropic builds AI products development process；Claude product management team organization collaboration |
| Q18 | 2/2 | 0/3 | product manager prioritization framework saying no to feature requests；how product managers reject stakeholder demands and manage expectations；product management decision making trade-offs stakeholder management |
| Q19 | 0/3 | 0/4 | build custom AI model vs use pre-trained large language models；in-house AI model training versus API integration for product features；when to train own AI model versus leverage existing foundation models |
| Q20 | 1/3 | 1/3 | How to measure product-market fit；Signs and indicators of achieving product-market fit；Metrics and methods for evaluating product-market fit |

## 各题最近距离（Day 8 定拒答规则用）

| 题号 | 类型 | A 原问题 | B 改写后（取最小） |
|---|---|---|---|
| Q01 | 库内 | 0.353 | 0.405 |
| Q02 | 库内 | 0.348 | 0.399 |
| Q03 | 库内 | 0.353 | 0.375 |
| Q04 | 库内 | 0.414 | 0.394 |
| Q05 | 库内 | 0.359 | 0.387 |
| Q06 | 库内 | 0.364 | 0.381 |
| Q07 | 库内 | 0.366 | 0.369 |
| Q08 | 库内 | 0.404 | 0.368 |
| Q09 | 库内 | 0.337 | 0.389 |
| Q10 | 库内 | 0.362 | 0.359 |
| Q11 | 库内 | 0.329 | 0.352 |
| Q12 | 库内 | 0.353 | 0.377 |
| Q13 | 库内 | 0.374 | 0.351 |
| Q14 | 库内（偏弱） | 0.354 | 0.367 |
| Q15 | 库内（偏薄） | 0.316 | 0.350 |
| Q16 | 库内 | 0.316 | 0.292 |
| Q17 | 库内 | 0.299 | 0.313 |
| Q18 | 库内 | 0.392 | 0.449 |
| Q19 | 库内 | 0.406 | 0.370 |
| Q20 | 库内 | 0.371 | 0.307 |
| Q21 | 库外·半相关 | 0.413 | 0.463 |
| Q22 | 库外·半相关 | 0.440 | 0.467 |
| Q23 | 库外·半相关 | 0.435 | 0.366 |
| Q24 | 库外·半相关 | 0.424 | 0.442 |
| Q25 | 库外·半相关 | 0.386 | 0.468 |
| Q26 | 库外·无关 | 0.531 | 0.561 |
| Q27 | 库外·无关 | 0.522 | 0.539 |
| Q28 | 库外·无关 | 0.547 | 0.539 |

本次大模型用量：输入 16638 token，输出 2303 token（以账单为准）