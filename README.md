# Lenny AI-PM RAG

给初级产品经理用的「AI 产品」问答知识库：中文提问，检索 Lenny's Podcast / Newsletter 的英文访谈稿，
用中文回答，并附来源（标题 + 嘉宾 + 日期 + 时间戳）。

不做"又一个知识库"，而是做一个**会自己判断"要不要查资料"的助手**（Agentic RAG）——
检索只是 Agent 手里的一个工具，不是产品本身。

## 进度（Day 1–6）

| 环节 | 状态 |
|---|---|
| 需求与边界规则（PRD） | ✅ 库内作答 / 库外明确拒答 / 闲聊不检索 |
| 数据勘察（60 篇全量） | ✅ 规模、字段覆盖、链接覆盖 |
| 清洗 + 切块 | ✅ 2,806 个带元数据的块，清洗可审计 |
| 向量索引 | ✅ bge-m3（1024 维）+ Chroma，余弦距离 |
| 检索（MVP） | ✅ 中文原问题单路向量检索 |
| 提问改写 / BM25 / RRF | ⚠️ 已实现并评测过，**不启用**（见 `docs/day5-summary.md`） |
| 精排（rerank） | ⚠️ 已实现并做过零评审体检，**Day 7 不接**（触发条件见 `docs/devlog/day-06.md`） |
| 检索稳定性 | ⚠️ 正常抖动在第 5–6 名；曾出现"100 名外"，**未查明**，已加向量自检 |
| 回答生成 + 界面 | ⬜ 未做 |

现状一句话：**检索可跑、可评测、可复现；回答链路和界面还没接。**

## 关键数字（截至 Day 6）

- 数据：60 篇（50 播客 + 10 newsletter），原始统计 866,202 词，清洗前正文 863,301 词（两个口径差 2,901 词）
- token：**估算，非账单实测**。按 1.57 token/词反推，清洗前约 136 万、清洗后约 128 万；早期"词数÷0.75"的 115 万口径已废弃
- 清洗：863,301 → 816,864 词（-5.4%）；其中赞助商口播 5 家 28 段 4,149 词，其余为转写噪音与文末推广
- 切块：2,806 块，中位 315 词（70–398），目标 300 / 上限 375 / 重叠 ≤80
- 无原文链接：767 块，占 27.3%（引用降级为"标题 + 嘉宾 + 日期 + 时间戳"）
- 检索（Day 5，A 版＝原问题单路向量）：Hit@5 60%（20 道库内题，块级口径、v2 标准），距 80% 目标差 20 个百分点；v2 标准未做人工抽检，此数字只作内部参考
- 精排（Day 6）：池 20 位移体检，15/20 已知相关块保住、6/10 已知无关块被清出；但新进前 5 的 46 个块未评，"新块更好"未证明。每题约 9,500 token、0.48 秒
- 进池率（Day 6，8 个已知好块）：池 20 = 5/8、30 = 5/8、50 = 6/8、100 = 7/8（8 个块为看过排名后挑选，有选择偏差，只作体检）
- 稳定性（Day 6）：同题重算 8 次、同一向量查库 5 次，位次稳定在第 5–6 名（余弦最小 0.999959）；曾出现"100 名外"，18 次复测未再现，未解决，已加自检

## 已知问题（下一步要解决的）

1. **检索准度不够**：Hit@5 60%，距 80% 差 20 个百分点；Q01 / Q07 / Q08 / Q14 / Q19 五道题在所有方案下都没有"能直接用的块"。
2. **半相关挡不住**：Q21–Q25 的最近距离（0.386–0.440）与库内题（0.299–0.414）重叠，光靠 0.47 阈值拒不了，需要第二道判断。该阈值仅基于 28 个样本，是临时值。
3. **引用体验不齐**：27.3% 的块没有原文链接，只能降级到"标题 + 嘉宾 + 日期 + 时间戳"，不能拼链接。
4. **"100 名外"未查明**：表现为一段时间内连续失败，之后不复现；现有自检只能防单次抽风，防不住持续降级。

## 目录

```
docs/
  PRD.md                      需求定义、边界规则、验收指标
  data-profile.md             数据画像（全量核查）
  cleaning-report.md          清洗 + 切块报告（脚本自动生成）
  ai-kb-launch-methodology.md Day 1–3 的方法论与可复用模板
  eval-questions.md           30 道评测题单（A/B/C/D 期望行为）
  day5-summary.md             Day 5 评测口径、结论与决定
  day5-results-v1.md / v2.md  两轮评测结果（口径不同，不可直接比）
  day6-results.md             Day 6 精排位移体检（零评审，会被 rank_check 覆盖）
  day6-results-partial.md     Day 6 单题试跑稿（不作结论）
  devlog/day-01~06.md         每日开发日志
src/
  explore_data.py             数据勘察
  check_fields.py             字段覆盖核查
  check_links.py              链接覆盖核查
  prepare_data.py             清洗 + 切块（含广告识别）
  validate_chunks.py          质量校验（规则一改就整跑）
  build_index.py              bge-m3 向量化入库 Chroma（断点续跑）
  retrieval.py                检索（query_vector 自检 / baseline / 改写+BM25+RRF）
  rerank.py                   精排打分（Day 7 备选，不接主线）
  pool_rate.py                进池率（只查向量，不花钱）
  rank_check.py               位移体检（零评审，会覆盖 docs/day6-results.md）
  check_jitter.py             稳定性探针（8 次重算 + 5 次同向量）
  check_rank_consistency.py   位次口径对照（前 100 / 前 300）
  debug_steps.py              四步对照，排除 import / 缓存 / 探针
  debug_q19.py                Q19 专项排查
  eval_retrieval.py           评测 + 生成抽检材料（会覆盖 day5-results.md 与 judge-spotcheck.md）
  llm.py                      模型调用封装
  diagnostics/                一次性排查与探针脚本
```

`data/`、`chroma_db/`、`.env` 均不入库；`docs/judge-spotcheck.md`、`docs/retrieval-check-day4.md`
含访谈原文片段，同样不入库，由脚本本地再生成。

## 数据来源与版权

免费 starter pack，来自
[LennysNewsletter/lennys-newsletterpodcastdata](https://github.com/LennysNewsletter/lennys-newsletterpodcastdata)：
10 篇 newsletter + 50 期播客转写稿，纯 markdown。
完整版（373 篇 newsletter / 322 期播客）见 [lennysdata.com](https://www.lennysdata.com)。

本仓库**不转存原数据**：`data/raw` 是原仓库的克隆，已在 `.gitignore` 中排除；
需要复现时自行 clone，用法见原仓库 README。

## 复现

```bash
# 1. 环境（Python 3.11+，本地用的是 3.13）
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 2. 密钥
echo 'SILICONFLOW_API_KEY=sk-xxx' > .env

# 3. 原始数据
git clone https://github.com/LennysNewsletter/lennys-newsletterpodcastdata.git data/raw

# 4. 清洗 + 切块 → data/processed/chunks.jsonl、docs/cleaning-report.md
python src/prepare_data.py
python src/validate_chunks.py

# 5. 建库 → chroma_db/（约 256 万 token，可中断后重跑）
python src/build_index.py

# 6. 评测（会产生 API 费用，约 10 万 token / 一轮）
python src/eval_retrieval.py

# 7. 检索体检（Day 6；不花钱、不调评审）
python src/pool_rate.py                             # 8 个已知好块的位次与进池率
python src/check_jitter.py Q19 boris-cherny-0045    # 稳定性：8 次重算 + 5 次同向量
python src/rank_check.py                            # 位移体检（会覆盖 docs/day6-results.md）
```

**所有命令都在仓库根目录执行**——`chroma_db` 是相对路径，在 `src/` 里跑会报 `collection does not exist`。

模型：对话 `deepseek-ai/DeepSeek-V3.2`，向量 `BAAI/bge-m3`（1024 维），精排 `BAAI/bge-reranker-v2-m3`，均走硅基流动。

## 评测口径（重要）

Day 5 跑过两套"相关"标准，数字**不可混用**：

| | v1 | v2 |
|---|---|---|
| 标准 | 段落能直接回答问题 | 入门 PM 读完能拿到可直接用的做法或明确结论 |
| Hit@5（A→B） | 60% → 60% | 60% → 50% |
| 严格 P@5 | 22% → 21% | 20% → 20% |
| MRR | 0.44 → 0.42 | 0.43 → 0.34 |

- A = 中文原问题 + 向量检索；B = 改写 3 个英文问法 + 向量 + BM25 + RRF
- 结论：B 没赢，且一次改了三个变量无法归因 → MVP 回到 A
- 没有标注口径的块级数字只作内部参考，不对外引用；验收以回答级行为通过率为准
