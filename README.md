# Lenny AI-PM RAG

给初级产品经理用的「AI 产品」问答知识库：中文提问，检索 Lenny's Podcast / Newsletter 的英文访谈稿，
用中文回答，并附来源（标题 + 嘉宾 + 日期 + 时间戳）。

不做"又一个知识库"，而是做一个**会自己判断"要不要查资料"的助手**（Agentic RAG）——
检索只是 Agent 手里的一个工具，不是产品本身。

## 进度（Day 1–5）

| 环节 | 状态 |
|---|---|
| 需求与边界规则（PRD） | ✅ 库内作答 / 库外明确拒答 / 闲聊不检索 |
| 数据勘察（60 篇全量） | ✅ 规模、字段覆盖、链接覆盖 |
| 清洗 + 切块 | ✅ 2,806 个带元数据的块，清洗可审计 |
| 向量索引 | ✅ bge-m3（1024 维）+ Chroma，余弦距离 |
| 检索 | ✅ 中文原问题单路向量检索（MVP） |
| 提问改写 / BM25 / RRF | ⚠️ 已实现并评测过，**暂不启用**（结论见 `docs/day5-summary.md`） |
| 回答生成 + 界面 | ⬜ 未做 |

现状一句话：**检索可跑、可评测；问答链路和 UI 还没接。**

## 关键数字

- 数据：60 篇（50 播客 + 10 newsletter），86.6 万词，约 115 万 token
- 清洗：863,301 → 816,864 词（-5.4%）；广告 5 家 28 段 4,149 词
- 切块：2,806 块，中位 315 词（70–398），目标 300 / 上限 375 / 重叠 ≤80
- 无原文链接的块占 27.3%（引用降级为"标题+嘉宾+日期+时间戳"）
- 检索 Hit@5 60%（20 道库内题，v2 口径），距目标 80% 还有差距

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
  devlog/day-01~05.md         每日开发日志
src/
  explore_data.py             数据勘察
  check_fields.py             字段覆盖核查
  check_links.py              链接覆盖核查
  prepare_data.py             清洗 + 切块（含广告识别）
  validate_chunks.py          质量校验（规则一改就整跑）
  build_index.py              bge-m3 向量化入库 Chroma（断点续跑）
  retrieval.py                检索（baseline / 改写+BM25+RRF）
  eval_retrieval.py           评测 + 生成抽检材料
  diagnostics/                排查与探针脚本
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
```

模型：对话 `deepseek-ai/DeepSeek-V3.2`，向量 `BAAI/bge-m3`（1024 维），均走硅基流动。

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
