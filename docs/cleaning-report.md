# 清洗与切块报告（由 src/prepare_data.py 自动生成）

## 参数
- 目标块大小 300 词，上限 375 词，重叠上限 80 词

## 清洗前后
- 清洗前总词数：863,301
- 清洗后总词数：816,864（减少 5.4%）

## 各规则清理量
- 赞助商口播(词)：4,149
- 边界重复(词)：736
- newsletter结尾(词)：520
- 行内链接：372
- [inaudible]：249
- 图片行：157
- 边界重复(处)：54
- 结尾outro(段)：50
- 赞助商口播(段)：28
- 视频嵌入行：12
- 告别语行：10
- 超长段被拆分：10

## 切块结果
- 块总数：2,806
- 块词数 最小/中位/最大：70 / 315 / 398
- 超过上限的块：9
- 无原文链接的块：767（27.3%）

## 被删除的赞助商口播（全部，供人工复核）
- amol-avasare 00:57:00-00:58:00 删188词/留头0尾0 | supporting sponsor, Vanta. Vanta helps over 15,000 companies, like Cur
- benedict-evans 00:37:04-00:37:04 删175词/留头0尾0 | supporting sponsor Vanta. Vanta helps over 15,000 companies like Curso
- boris-cherny 00:01:47-00:01:47 删12词/留头36尾0 | word from our wonderful sponsors.
- brian-halligan 00:01:32-00:01:32 删99词/留头0尾0 | word from our wonderful sponsors. Applications break in all kinds of w
- brian-halligan 00:37:10-00:37:49 删161词/留头0尾0 | today's sponsor, WorkOS. If you're building software for enterprises, 
- caitlin-kalinowski 00:43:38-00:44:19 删175词/留头0尾0 | supporting sponsor, Vanta. Vanta helps over 15,000 companies like Curs
- cat-wu 00:45:40-00:45:40 删175词/留头0尾0 | supporting sponsor Vanta. Vanta helps over 15,000 companies like Curso
- dan-shipper-2 00:45:52-00:46:51 删176词/留头0尾44 | supporting sponsor, Vanta. Vanta helps over 15,000 companies like Curs
- dr-becky-kennedy 00:45:16-00:46:00 删248词/留头0尾0 | Your marketing website sets the tone for your brand and is the one tou
- emmanuel-ameisen 00:27:40-00:27:40 删117词/留头0尾0 | supporting sponsor is DX. Now that everybody at your company is finall
- eric-ries-2 00:44:29-00:45:10 删175词/留头0尾0 | supporting sponsor, Vanta. Vanta helps over 15,000 companies like Curs
- evan-spiegel 00:33:33-00:34:14 删175词/留头0尾0 | supporting sponsor Vanta. Vanta helps over 15,000 companies like Curso
- jeetu-patel 00:01:15-00:01:58 删166词/留头121尾0 | word from our wonderful sponsors.
- jeetu-patel 00:02:57-00:03:55 删229词/留头0尾0 | Your marketing website sets the tone for your brand. It is the one tou
- jenny-wen 00:01:20-00:01:20 删12词/留头141尾0 | word from our wonderful sponsors.
- jessica-fain 00:02:11-00:02:11 删13词/留头0尾0 | word from our wonderful sponsors.
- jessica-fain 00:46:07-00:46:07 删137词/留头0尾0 | You know what we don't love talking about? SOC 2. That's where Vanta c
- josh-woodward 00:30:47-00:30:47 删117词/留头0尾0 | supporting sponsor is DX. Now that everybody at your company is finall
- keith-rabois 00:41:33-00:42:15 删175词/留头0尾0 | supporting sponsor Vanta. Vanta helps over 15,000 companies like Curso
- lazar-jovanovic 00:49:57-00:50:36 删161词/留头0尾0 | today's sponsor, WorkOS. If you're building software for enterprises, 
- mark-pincus 00:47:28-00:47:28 删175词/留头0尾0 | supporting sponsor Vanta. Vanta helps over 15,000 companies like Curso
- molly-graham-2 00:41:12-00:41:12 删118词/留头0尾0 | supporting sponsor is DX. Now that everybody at your company is finall
- nikhyl-singhal-2 00:47:20-00:48:00 删187词/留头18尾0 | supporting sponsor Vanta. Vanta helps over 15,000 companies like Curso
- sam-lessin 00:45:50-00:46:39 删204词/留头0尾0 | today's sponsor, WorkOS. If you're building software for enterprises, 
- sherwin-wu-v2 00:01:11-00:01:11 删12词/留头43尾0 | word from our wonderful sponsors.
- simon-willison 00:47:19-00:47:43 删174词/留头0尾0 | supporting sponsor, Vanta. Vanta helps over 15,000 companies like Curs
- tony-fadell 00:47:30-00:48:00 删186词/留头0尾0 | supporting sponsor Vanta. Vanta helps over 15,000 companies like Curso
- zevi-arnovitz 00:37:23-00:38:01 删207词/留头0尾0 | Your marketing website sets the tone for your brand and is the one tou

## 超长发言含广告触发词（未自动处理，待人工复核）
- boris-cherny 00:01:47 未找到广告结尾标志，按关键词处理，请复核
- brian-halligan 00:01:32 未找到广告结尾标志，按关键词处理，请复核
- jenny-wen 00:01:20 未找到广告结尾标志，按关键词处理，请复核
- jessica-fain 00:02:11 未找到广告结尾标志，按关键词处理，请复核
- sherwin-wu-v2 00:01:11 未找到广告结尾标志，按关键词处理，请复核

## newsletter 结尾截断明细（核对用）
- 74词 | '## Hiring? 👀\n\nI run a white-glove recruiting service specializing in s'
- 31词 | '**If you’re finding this newsletter valuable, share it with a friend, '
- 31词 | '**If you’re finding this newsletter valuable, share it with a friend, '
- 31词 | '**If you’re finding this newsletter valuable, share it with a friend, '
- 76词 | '**If you’re finding this newsletter valuable, share it with a friend, '
- 108词 | '## 📣 Join Lenny’s Talent Collective 📣\n\nIf you’re hiring, [join Lenny’s'
- 31词 | '**If you’re finding this newsletter valuable, share it with a friend, '
- 76词 | '## Hiring? 👀\n\nI’ve got a white-glove recruiting service specializing i'
- 31词 | '**If you’re finding this newsletter valuable, share it with a friend, '
- 31词 | '**If you’re finding this newsletter valuable, share it with a friend, '