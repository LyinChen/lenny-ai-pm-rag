# Day 5 检索评测结果

评审：大模型（DeepSeek-V3.2），待人工抽检校准。A=改进前（原问题+向量），B=改进后（改写+混合）
评审标准 v2：入门 PM 读完能拿到可直接用的做法或明确结论才算"相关"。样本 20 题。
## 汇总（20 道库内题）

| 指标 | A 改进前 | B 改进后 |
|---|---|---|
| Hit@5（至少1条相关） | 60% | 50% |
| P@5 严格（只算相关） | 20% | 20% |
| P@5 宽松（含部分相关） | 90% | 96% |
| MRR（首个相关的排名） | 0.43 | 0.34 |

## 逐题（相关数/部分相关数）

| 题号 | A | B | 改写出的英文问法 |
|---|---|---|---|
| Q01 | 0/4 | 0/5 | evaluating AI feature ROI business value metrics；criteria for launching AI product features prioritization framework；measuring AI feature success user impact adoption metrics |
| Q02 | 0/4 | 1/4 | key performance indicators for AI feature launch；metrics to measure AI product success post-launch；evaluating AI feature performance after deployment |
| Q03 | 1/4 | 1/3 | product manager and engineering collaboration in AI product development；best practices for PM and engineer partnership in artificial intelligence projects；how product managers work with AI engineers effectively |
| Q04 | 1/3 | 0/4 | differences between AI feature product requirements document and traditional PRD；how to write product requirements for AI features versus standard features；AI product requirements documentation best practices and differences |
| Q05 | 1/3 | 0/5 | How to pitch AI feature development to leadership and secure resources；Strategies for advocating AI product initiatives and obtaining executive buy-in；Business case presentation for AI feature development and resource allocation |
| Q06 | 0/5 | 1/4 | How to reduce AI hallucination in product design；Strategies for minimizing factual inaccuracies in AI responses；Techniques to improve answer reliability and reduce AI confabulation |
| Q07 | 0/5 | 0/5 | common pitfalls in AI product interaction flow design；UX design challenges for AI-powered products；mistakes to avoid when designing user flows for artificial intelligence applications |
| Q08 | 0/3 | 0/5 | AI product management guardrails and boundaries；scenarios where AI should not provide answers；ethical constraints for AI response systems |
| Q09 | 1/4 | 1/4 | product manager transition from traditional to AI products；how traditional product managers can become AI product managers；skills and training needed for PMs to move into AI product management |
| Q10 | 2/2 | 4/1 | no-code AI prototype tools for product managers；how to create AI demo without engineering resources；rapid prototyping AI features for stakeholder presentation |
| Q11 | 3/2 | 2/3 | product manager daily workflow AI automation tools；how product managers use artificial intelligence for productivity；AI applications for product management efficiency and time management |
| Q12 | 0/5 | 0/5 | managing AI output variability and consistency in product design；handling non-deterministic AI responses in user-facing applications；product strategies for dealing with stochastic AI model behavior |
| Q13 | 3/2 | 3/2 | human-in-the-loop AI implementation strategy；phased rollout vs full automation for AI features；gradual automation approach for AI products |
| Q14 | 0/5 | 0/5 | user trust issues with AI outputs adoption barriers；overcoming skepticism towards AI-generated results in product management；strategies to increase user confidence in AI system recommendations |
| Q15 | 1/4 | 3/2 | How will the core competencies of product managers evolve in the AI era?；What are the essential skills for product managers in the age of artificial intelligence?；How does AI impact the role and required capabilities of product managers? |
| Q16 | 3/2 | 3/2 | Duolingo user growth strategy turnaround；Duolingo product-led growth revival case study；How Duolingo reignited user acquisition and retention |
| Q17 | 1/4 | 1/4 | Anthropic product team structure and development process；How Anthropic builds AI products and manages product development；Anthropic product management methodology and team collaboration |
| Q18 | 2/3 | 0/4 | product manager prioritization framework saying no to feature requests；how product managers push back on unreasonable requirements stakeholder management；product management trade-off decisions rejecting low-value features |
| Q19 | 0/3 | 0/5 | build vs buy AI model strategy for product features；custom model training versus API integration for AI products；in-house AI development compared to third-party large language model APIs |
| Q20 | 1/3 | 0/4 | How to measure product-market fit；Signs of achieving product-market fit；Product-market fit assessment metrics |

## 各题最近距离（Day 8 定拒答规则用）

| 题号 | 类型 | A 原问题 | B 改写后（取最小） |
|---|---|---|---|
| Q01 | 库内 | 0.353 | 0.395 |
| Q02 | 库内 | 0.348 | 0.402 |
| Q03 | 库内 | 0.353 | 0.375 |
| Q04 | 库内 | 0.413 | 0.401 |
| Q05 | 库内 | 0.359 | 0.386 |
| Q06 | 库内 | 0.364 | 0.369 |
| Q07 | 库内 | 0.367 | 0.347 |
| Q08 | 库内 | 0.404 | 0.404 |
| Q09 | 库内 | 0.336 | 0.343 |
| Q10 | 库内 | 0.362 | 0.359 |
| Q11 | 库内 | 0.328 | 0.368 |
| Q12 | 库内 | 0.353 | 0.341 |
| Q13 | 库内 | 0.374 | 0.336 |
| Q14 | 库内（偏弱） | 0.353 | 0.358 |
| Q15 | 库内（偏薄） | 0.316 | 0.310 |
| Q16 | 库内 | 0.316 | 0.309 |
| Q17 | 库内 | 0.299 | 0.307 |
| Q18 | 库内 | 0.392 | 0.438 |
| Q19 | 库内 | 0.406 | 0.363 |
| Q20 | 库内 | 0.371 | 0.293 |
| Q21 | 库外·半相关 | 0.413 | 0.449 |
| Q22 | 库外·半相关 | 0.439 | 0.494 |
| Q23 | 库外·半相关 | 0.435 | 0.366 |
| Q24 | 库外·半相关 | 0.424 | 0.442 |
| Q25 | 库外·半相关 | 0.386 | 0.475 |
| Q26 | 库外·无关 | 0.531 | 0.577 |
| Q27 | 库外·无关 | 0.522 | 0.552 |
| Q28 | 库外·无关 | 0.547 | 0.542 |

本次大模型用量：输入 93362 token，输出 8289 token（以账单为准）