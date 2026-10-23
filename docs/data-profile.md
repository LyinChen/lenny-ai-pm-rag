# 数据画像
## 规模
- 文件数：60（播客 50 / newsletter 10）
- 总词数：866,202；估算 token：约 115 万
- 单篇长度：最短 1,150（state-of-the-product-job-market-in-2025）
  最长 25,594（jason-m-lemkin）；平均 14,436
- 预计块数（512 token/块）：约 2,256

## 元数据字段
- 播客：title, date, type, guest, post_url, description, word_count
  （部分文件另有 youtube_url, video_id, channel，字段不统一，待全量核查）
- newsletter：title, subtitle, date, type, post_url, word_count
- 引用链接：youtube_url（有则用）否则 post_url

## 噪音
- 播客：开场摘要、结尾 outro、[inaudible] 标记、25 分钟边界处的重复句
- newsletter：图片行、文末招聘/订阅 CTA、行内超链接

## 内容结构
- 播客稿：每段有说话人标签 + 时间戳；一个 speaker turn 为一段，
  通常几十到一百多词，长回答可达数百词
- 话题转换：由主持人的过渡语标记，边界清晰
- 噪音：开场宣传/订阅 CTA、newsletter 推广、赞助商口播（如 Framer）、
  寒暄、书籍/产品推广

## 引用链接覆盖（全量核查）
| 情况 | 篇数 |
|---|---|
| 只有 post_url | 33 |
| 只有 youtube_url | 13 |
| 两者都有 | 0 |
| 都没有 | 14（23%） |

## 引用规则
- 有 youtube_url → 用它；否则有 post_url → 用它；否则无链接
- 链接不全时，最低保证展示：标题 + 嘉宾 + 日期 + 时间戳
- 不自行拼接链接（编错的链接比没有更伤可信度）
- 无链接的文档在界面上标注"暂无原文链接"

## 对 Day 3 的影响
- 切块要保留：title, guest, date, type, youtube_url，
  以及每块的说话人和起始时间戳
- 需要清洗：把 frontmatter 转成元数据；移除开场宣传和赞助商口播
- 不清洗：寒暄（量小、误删风险大，MVP 阶段忽略）