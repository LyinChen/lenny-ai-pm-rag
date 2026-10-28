# 清洗与切块报告（由 src/prepare_data.py 自动生成）

## 参数
- 目标块大小 300 词，上限 375 词，重叠上限 80 词

## 清洗前后
- 清洗前总词数：863,301
- 清洗后总词数：818,177（减少 5.2%）

## 各规则清理量
- 赞助商口播(词)：1,976
- 边界重复(词)：761
- newsletter结尾(词)：433
- 行内链接：375
- [inaudible]：249
- 图片行：158
- 边界重复(处)：56
- 结尾outro(段)：50
- 赞助商口播(段)：24
- 视频嵌入行：12
- 广告续段(段)：12
- 超长段被拆分：10
- 告别语行：8

## 切块结果
- 块总数：2,811
- 块词数 最小/中位/最大：70 / 315 / 398
- 超过上限的块：9
- 无原文链接的块：770（27.4%）

## 被删除的赞助商口播（全部，供人工复核）
- amol-avasare 00:57:00 删36词/留0词 | 删: That is so cool. I am so excited to tell you about this season's supporting spon
- benedict-evans 00:37:04 删175词/留0词 | 删: I am so excited to tell you about this season's supporting sponsor Vanta. Vanta 
- boris-cherny 00:01:47 删12词/留36词 | 删: Let's get into it after a short word from our wonderful sponsors.
- brian-halligan 00:01:32 删99词/留0词 | 删: Let's get into it, after a short word from our wonderful sponsors. Applications 
- brian-halligan 00:37:10 删82词/留21词 | 删: The answer is they're all powered by today's sponsor, WorkOS. If you're building
- brian-halligan 00:37:49 续段删58词 | They're essentially Stripe for enterprise features. Visit WorkOS.com to get star
- caitlin-kalinowski 00:43:38 删32词/留0词 | 删: I am so excited to tell you about this season's supporting sponsor, Vanta. Vanta
- cat-wu 00:45:40 删175词/留0词 | 删: I am so excited to tell you about this season's supporting sponsor Vanta. Vanta 
- dan-shipper-2 00:45:52 删157词/留0词 | 删: I am so excited to tell you about this season's supporting sponsor, Vanta. Vanta
- dan-shipper-2 00:46:51 续段删63词 | Learn more at vanta.com/lenny. And as a listener of this podcast, you get $1,000
- emmanuel-ameisen 00:27:40 删117词/留0词 | 删: This season's supporting sponsor is DX. Now that everybody at your company is fi
- eric-ries-2 00:44:29 删114词/留0词 | 删: I am so excited to tell you about this season's supporting sponsor, Vanta. Vanta
- eric-ries-2 00:45:10 续段删61词 | Vanta automates compliance and risk management with over 35 security and privacy
- evan-spiegel 00:33:33 删114词/留0词 | 删: I am so excited to tell you about this season's supporting sponsor Vanta. Vanta 
- evan-spiegel 00:34:14 续段删61词 | Vanta automates compliance and risk management with over 35 security and privacy
- jeetu-patel 00:01:15 删12词/留121词 | 删: Let's get into it after a short word from our wonderful sponsors.
- jeetu-patel 00:01:58 续段删154词 | Applications break in all kinds of ways. Crashes, slowdowns, regressions, and th
- jenny-wen 00:01:20 删12词/留141词 | 删: Let's get into it after a short word from our wonderful sponsors.
- jessica-fain 00:02:11 删13词/留0词 | 删: Now, let's get into it after a short word from our wonderful sponsors.
- josh-woodward 00:30:47 删117词/留0词 | 删: This season's supporting sponsor is DX. Now that everybody at your company is fi
- keith-rabois 00:41:33 删66词/留0词 | 删: I am so excited to tell you about this season's supporting sponsor Vanta. Vanta 
- lazar-jovanovic 00:49:57 删36词/留21词 | 删: The answer is they're all powered by today's sponsor, WorkOS. If you're building
- lazar-jovanovic 00:50:19 续段删46词 | WorkOS turns those deal blockers into drop-in APIs with a modern developer platf
- lazar-jovanovic 00:50:36 续段删58词 | They're essentially Stripe for enterprise features. Visit workos.com to get star
- mark-pincus 00:47:28 删175词/留0词 | 删: I am so excited to tell you about this season's supporting sponsor Vanta. Vanta 
- molly-graham-2 00:41:12 删118词/留0词 | 删: This season's supporting sponsor is DX. Now that everybody at your company is fi
- nikhyl-singhal-2 00:47:20 删91词/留18词 | 删: I am so excited to tell you about this season's supporting sponsor Vanta. Vanta 
- nikhyl-singhal-2 00:48:00 续段删96词 | ... their organization, their business, and not to mention their customer data. 
- sam-lessin 00:45:50 删54词/留21词 | 删: The answer is they're all powered by today's sponsor, WorkOS. If you're building
- sam-lessin 00:46:19 续段删59词 | Whether you're a seed stage startup trying to land your first enterprise custome
- sam-lessin 00:46:39 续段删70词 | WorkOS allows you to build like the best with delightful APIs, comprehensive doc
- sherwin-wu-v2 00:01:11 删12词/留43词 | 删: Let's get into it after a short word from our wonderful sponsors.
- simon-willison 00:47:19 删66词/留0词 | 删: I am so excited to tell you about this season's supporting sponsor, Vanta. Vanta
- simon-willison 00:47:43 续段删108词 | Every security leader that I talk to is feeling the increasing weight of protect
- tony-fadell 00:47:30 删91词/留0词 | 删: I am so excited to tell you about this season's supporting sponsor Vanta. Vanta 
- tony-fadell 00:48:00 续段删95词 | ... Organization, their business, and not to mention their customer data. Becaus

## 超长发言含广告触发词（未自动处理，待人工复核）

## newsletter 结尾截断明细（核对用）
- 74词 | '## Hiring? 👀\n\nI run a white-glove recruiting service specializing in s'
- 31词 | '**If you’re finding this newsletter valuable, share it with a friend, '
- 31词 | '**If you’re finding this newsletter valuable, share it with a friend, '
- 31词 | '**If you’re finding this newsletter valuable, share it with a friend, '
- 76词 | '**If you’re finding this newsletter valuable, share it with a friend, '
- 21词 | '**If you’re finding this newsletter valuable, share it with a friend, '
- 31词 | '**If you’re finding this newsletter valuable, share it with a friend, '
- 76词 | '## Hiring? 👀\n\nI’ve got a white-glove recruiting service specializing i'
- 31词 | '**If you’re finding this newsletter valuable, share it with a friend, '
- 31词 | '**If you’re finding this newsletter valuable, share it with a friend, '