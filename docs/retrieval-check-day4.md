# Day 4 检索人工评估

判断标准：**相关**=能直接回答问题；**部分相关**=沾边但不能回答；**无关**=答非所问


## 问：怎么给 AI 产品定义成功指标？

### 1. 距离 0.382 | Beyond vibe checks: A PM’s complete guide to evals | 文章 | -

## **Looking ahead**
As AI products become more complex, the ability to write good evals will become increasingly crucial. Evals are not just about catching bugs; they help ensure that your AI system consistently delivers value and delights your users! Evals are a critical step in going from prototype to production with generative AI.

I would love to hear from you: How are you currently evaluating your AI products? What challenges have you faced? Leave a comment👇

Leave a comment

### **📚 Further study**
1. A conversation with OpenAI’s CPO Kevin Weil, Anthropic’s CPO Mike Krieger, and Sarah Guo
2. Peter Yang + Aman: The AI Skill That Will Define Your PM Career in 2025 | Aman Khan (Arize)
3. DeepLearning.ai course on evals with Andrew Ng
4. Prompt optimization guide: <https://arize.com/course/prompt-optimization/>
5. Arize eval hub (free!): <https://arize.com/llm-evaluation>
6. Peter Yang + Scott White: Exclusive: Inside the Best AI Model for Coding and Writing | Scott White (Anthropic)

*Thank you, Aman!*

**判断：** （相关 / 部分相关 / 无关）

### 2. 距离 0.389 | Aishwarya Naresh Reganti + Kiriti Badam | Aishwarya Naresh Reganti + Kiriti Badam | 00:17:41

Lenny Rachitsky (00:17:41): So let me give you a few more examples of this kind of progression that you recommend. And the reason I'm spending so much time here is this is a really key part of your recommendation to help people build more successful AI products. This idea of start slow with high control and low agency and then build up over time once you've built confidence that it's doing the right sort of work. So a few more examples that you shared in your post that I'll just read. So say you're building a coding assistant, V1 would be just suggest inline completion and boilerplate snippets. V2 would be generate larger blocks like tests or refactors for humans to review. And then V3 is just apply the changes and open PRs autonomously. And then another example is a marketing assistant. So V1 would be draft emails or social copy, just like here's what I would do.
Lenny Rachitsky (00:18:26): V2 is build a multi-step campaign and run the campaign. And V3 is just launch it A/B tested auto-optimize campaigns across channels. Awesome. Yeah. And again, just to summarize where we're at, just to give people the advice we've shared so far. One is just important to understand AI products are different. They're non-deterministic. And you pointed out, and I forgot to actually mirror back this point, both on the input and the output. The user experience is non-deterministic.People will see different things, different outputs, different chat conversations, different maybe UI if it's designing the UI for you. And also the output obviously is going to be non-terministic. So that's a problem and a challenge. And then-

**判断：** （相关 / 部分相关 / 无关）

### 3. 距离 0.395 | The AI paradox: More automation, more humans, more work | Dan Shipper | Dan Shipper | 00:48:00

Dan Shipper (00:48:00): and I didn't really want to go in and try to understand the code base, to be honest. And I think that's a really important thing when we think about benchmarks is AI is a broadly distributed technology that any human can use. And when we are benchmarking against humans, AI against humans, we're actually really always talking about one human using AI versus another human using AI 'cause AI doesn't use itself. It may be able to in this slightly somewhat recursive way, but in any real use case, there's always a human pretty close to it making sure that it's working.
Lenny Rachitsky (00:48:37): Okay. I want to try to wrap up our first bucket. There's so much to talk about. I made a little list of things that I think people should do based on your predictions to be successful. We'll talk about this at the end too, but just a few things. One is start using Codex or Claude Code more and more for the work you're doing and especially the browser, use tools inside of it. Two is allow agents to use your products. If you're building a SaaS tool, make it easy for agents to be a user essentially. Three is start thinking about some Slack bot that you can work with, like try out tools. I know Slack has their own Slack bot that I think is really good too and I haven't played with it, but people really like it. So look for, I guess, a tool that could become the AI agent within your company.
Lenny Rachitsky (00:49:24): Buy SaaS stock ASAP, not investment advice.
Dan Shipper (00:49:32): I think that's totally right. My slight tweak is when you're thinking about building your software for agents, the current model is I'm building a CLI that an agent uses, but they're using it in a sort of like they're being... I delegated to task the agent and the agent's using the CLI. And where I think it's going is you and the agent are using the app together. The agent's probably using the CLI, but you're using the web interface and they both need to be in sync. And that is, I think, a new challenge that's really interesting.

**判断：** （相关 / 部分相关 / 无关）

### 4. 距离 0.401 | An AI glossary | 文章 | -

Evals are often described by top product leaders as the most critical, yet overlooked, skill for building successful AI products:

Don’t miss this excellent guest post by Aman Khan that teaches you how to craft evals for your product.

### **Inference**
Inference is when the model “runs.” When you ask ChatGPT a question and it generates a response, that’s it doing inference.

### **MCP (model context protocol)**
MCP is a recently released open standard that allows AI models to interact with external tools—like your calendar, CRM, Slack, or codebase—easily, reliably, and securely. Previously, developers had to write their own custom code for each new integration.

MCP also gives the AI the ability to take *actions* through these tools, for example, updating customer records in Salesforce, sending messages in Slack, scheduling meetings in your calendar, or even committing code to GitHub.

It’s still early in the definition of AI protocols, and there are other competing proposals, like A2A from Google and ACP from BeeAI/IBM.

Here’s a really nice in-depth explanation of MCP:

### **Gen AI (generative AI)**
Gen AI refers to AI systems that can create new content, such as text, images, code, audio, or video. This is opposed to models that just analyze or classify data, such as spam detection, fraud analysis, or image recognition models.

### **GPT (generative pre-trained transformer)**
“GPT” captures the three key elements behind how state-of-the-art LLMs like ChatGPT 4.1, Claude Opus 4, Llama 4, and Grok 3 work:

1. **Generative:** The model doesn’t just classify or analyze—it can generate new content.
2. **Pre-trained:** It first learns general language patterns by being trained on massive amounts of text (as described above) and can then be fine-tuned for more specific tasks.
3. **Transformer:** This refers to the breakthrough architecture (described above) that allows the model to understand context, relationships, and meaning across language.

**判断：** （相关 / 部分相关 / 无关）

### 5. 距离 0.406 | The 100-person AI lab that became Anthropic and Google's secret weapon | Edwin Chen (Surge AI) | Edwin Chen | 00:42:35

Edwin Chen (00:42:35): And then there's this other notion of evals where you're trying to measure the model's progress like, okay, yeah, I have five different candidate checkpoints and I want to pick the one that's best in order to release it to the public. So going to run all these evals on these five different checkpoints in order to decide which one is best.
Lenny Rachitsky (00:42:51): Awesome.
Edwin Chen (00:42:51): Yeah, and now we have RL environments, so this is kind of like a hot new thing.
Lenny Rachitsky (00:42:55): Awesome. So what I love about this business journey is just there's always something new. There's always this like, okay. We're getting so good at just all this beautiful data for companies and now they need something completely different. Now we're setting up all these virtual machines for them and all these different use cases.
Edwin Chen (00:43:08): Yep.
Lenny Rachitsky (00:43:08): And it feels like that's a big part of this industry you're in, it's just adapting to what labs are asking for.
Edwin Chen (00:43:13): Yeah. So I really do think that we are going to need to build a suite of products that reflect a million different ways that humans learn. Like for example, think about becoming a great writer. You don't become great by memorizing a bunch of grammar rules. You become great by reading great books, and you practice writing, and you get feedback from your teachers and from the people who buy your books in a bookstore and leave reviews. And you notice what works and what doesn't. And you develop taste by being exposed to all of these masterpieces and also just terrible writing. So you learn through this endless cycle of practicing reflection, and each type of learning that you have, again, these are all very different methods of learning to become a great writer, so just in the same way that... it's a thousand different ways that the great writer becomes great, I think there's going to be a thousand different ways that AI need to learn.

**判断：** （相关 / 部分相关 / 无关）


## 问：How do you define success metrics for AI products?

### 1. 距离 0.401 | The 100-person AI lab that became Anthropic and Google's secret weapon | Edwin Chen (Surge AI) | Edwin Chen | 00:42:35

Edwin Chen (00:42:35): And then there's this other notion of evals where you're trying to measure the model's progress like, okay, yeah, I have five different candidate checkpoints and I want to pick the one that's best in order to release it to the public. So going to run all these evals on these five different checkpoints in order to decide which one is best.
Lenny Rachitsky (00:42:51): Awesome.
Edwin Chen (00:42:51): Yeah, and now we have RL environments, so this is kind of like a hot new thing.
Lenny Rachitsky (00:42:55): Awesome. So what I love about this business journey is just there's always something new. There's always this like, okay. We're getting so good at just all this beautiful data for companies and now they need something completely different. Now we're setting up all these virtual machines for them and all these different use cases.
Edwin Chen (00:43:08): Yep.
Lenny Rachitsky (00:43:08): And it feels like that's a big part of this industry you're in, it's just adapting to what labs are asking for.
Edwin Chen (00:43:13): Yeah. So I really do think that we are going to need to build a suite of products that reflect a million different ways that humans learn. Like for example, think about becoming a great writer. You don't become great by memorizing a bunch of grammar rules. You become great by reading great books, and you practice writing, and you get feedback from your teachers and from the people who buy your books in a bookstore and leave reviews. And you notice what works and what doesn't. And you develop taste by being exposed to all of these masterpieces and also just terrible writing. So you learn through this endless cycle of practicing reflection, and each type of learning that you have, again, these are all very different methods of learning to become a great writer, so just in the same way that... it's a thousand different ways that the great writer becomes great, I think there's going to be a thousand different ways that AI need to learn.

**判断：** （相关 / 部分相关 / 无关）

### 2. 距离 0.404 | The 100-person AI lab that became Anthropic and Google's secret weapon | Edwin Chen (Surge AI) | Edwin Chen | 00:59:44

Edwin Chen (00:59:44): And yeah, I think it's really relevant to what we do because it's very hard and difficult to measure and define whether something is genuinely advancing humanity. It's very easy to measure all these proxies instead like clicks and likes. But I think that's why our work is so interesting. We want to work the hard, important metrics that require the hardest types of data and not just the easy ones. So I think one of the things I often say is you are your objective function. So we want the rich, complex, objective functions and not these simplistic proxies. And our job is to figure out how to get the data to match this.
Edwin Chen (01:00:12): So yeah, we want data, we want metrics that measure whether AI is making your life richer. We want to train our systems this way. And we want tools that make us more curious and more creative, not just lazier. And it's hard because, yeah, humans are kind of inherently lazy so AI software deals are the easiest way to get engagement, make all your metrics fall up. So I think this question about choosing the right objective functions and making sure that we're optimizing towards them and not just these easy proxies is really important to our future.
Lenny Rachitsky (01:00:37): Wow. I love how what you're sharing here gives you so much more appreciation of the nuances of building AI, training AI, the work that you're doing.
Lenny Rachitsky (01:00:45): From the outside, people could just look at Surge and companies in the space of, okay, cool. They're just creating all this data, feeding it to AI. But clearly there's so much to this that people don't realize, and I love knowing that you're at the head of this, that someone like you is thinking through this so deeply.

**判断：** （相关 / 部分相关 / 无关）

### 3. 距离 0.407 | The 100-person AI lab that became Anthropic and Google's secret weapon | Edwin Chen (Surge AI) | Edwin Chen | 00:57:52

Lenny Rachitsky (00:57:52): Along that thread, I know you have a very strong thesis on just why this work matters to humanity and why this is so important, talk about that.
Edwin Chen (00:58:01): I'll get a bit philosophical here, but I think the question itself is a bit philosophical, so bear with me. So the most straightforward way of thinking about what we do is we train and evaluate AI. But there's a deeper mission that I often think about, which is helping our customers think about their dream objective functions. Like yeah, what kind of model do they want their model to be? And once we help them do that, we'll help them train their model to reach their north star and we'll help them measure that progress. But it's really hard because objective functions are really rich and complex. It's kind of like the difference between having a kid and asking them, "Okay, what test do you want to pass? Do you want them to get a high score on SAT and write a really good college essay?" That's a simplistic version versus what kind of person do you want them to grow up to be? Will you be happy if they're happy no matter what they do or are you hoping they'll go to a good school and be financially successful? And again, if you take that notion, it's like, okay, how do you define happiness? How do you measure whether they're happy? How do you measure whether they're financially successful? It's a lot harder than something measuring whether or not you're getting a high score on the SAT, and what we're doing is we want to help our customers reach, again, their dream north stars and figure out how to measure them. And so I talked about this example of what you want models to do when you're asking them to write 50 different evaluations. Do you just continue them for 50 more or do you just say, "No, just move on because this is perfect enough." And the broader question is, are we building these systems that actually advance humanity? And if so how do we build the data sets to train towards that and measure it? Are we optimizing for all of these wrong things, just systems that suck up more and more of our time and make us lazier and lazier?

**判断：** （相关 / 部分相关 / 无关）

### 4. 距离 0.408 | Aishwarya Naresh Reganti + Kiriti Badam | Aishwarya Naresh Reganti + Kiriti Badam | 00:47:13

Aishwarya Naresh Reganti (00:47:13): And we had to shut down the product because we were doing so many hot fixes and there was no way we could count all the emerging problems that were coming up. And there's also quite some news online. Recently, I think Air Canada had this thing where one of their agents predicted or hallucinated a policy for a refund, which was not part of their original playbook, and they had to go by it because legal stuff. And there have been a ton of really scary incidents. And that's where the idea comes from. How can you build so that you don't lose customer trust and you don't end up, or your agent or AI system doesn't end up making decisions that are super dangerous to the company itself. At the same time, build a flywheel so that you can improve your product as you go. And that's where we came up with this idea of continuous calibration, continuous development.
Aishwarya Naresh Reganti (00:48:08): The idea is pretty simple, which is we have this right side of the loop, which is continuous development, where you scope capability and curate data, essentially get a data set of what your expected inputs are and what your expected outputs should be looking at. This is a very good exercise before you start building any AI product because many times you figure out that a lot of the folks within the team are just not aligned on how the product should behave. And that's where your PMs can really give in a lot more information and your subject matter experts as well. So you have this data set that you know your AI product should be doing really well on. It's not comprehensive, but it lets you get started. And then you set up the application and then design the right kind of evaluation metrics. And I intentionally use the term evaluation metrics, although we say evals because I just want to be very specific in what it is because evaluation is a process, evaluation metrics are dimensions that you want to focus on during the process.

**判断：** （相关 / 部分相关 / 无关）

### 5. 距离 0.409 | The 100-person AI lab that became Anthropic and Google's secret weapon | Edwin Chen (Surge AI) | Edwin Chen | 00:16:21

Edwin Chen (00:16:21): So long story short, I think there's all these different factors, and certainly the data is a big part of it, but it's also like what is the objective function that you're trying to optimize your model towards?
Lenny Rachitsky (00:16:30): That is so interesting. The taste of the person leading this work will inform what data they ask for, what data they feed it. But it's wild it shows the value of great data. Anthropic got so much growth and win from essentially better data.
Edwin Chen (00:16:49): Yeah, exactly.
Lenny Rachitsky (00:16:50): And I could see why companies like yours are growing so fast. There's just so much... And that's just one vertical. That's just coding, and then there's probably a similar area for writing. I love that it's... It's interesting that AI, it feels like this artificial computer binary thing, but it's like taste. Human judgment is still such a key factor in these things being successful.
Edwin Chen (00:17:09): Yep, exactly. Again, going back to the example I said earlier, certain companies, if you ask them what is good poem, they will simply robotically check off all of these instructions on our list.
Edwin Chen (00:17:20): But again, I don't think that makes for good poetry, so certain frontier labs, the ones with more taste in sophistication, they will realize that it doesn't reduce to this six set of checkboxes and they'll consider all of these kind of implicit, very subtle qualities instead, and I think that's what makes them better at this at the end of the day.
Lenny Rachitsky (00:17:38): You mentioned benchmarks. This is something a lot of people worry about is there's all these models that are always... Basically, it feels like every model is better than humans at every STEM field at this point, but to a regular person, it doesn't feel like these models are getting that much smarter constantly. What's your just sense of how much you trust benchmarks and just how correlated those are with actual AI advancements?

**判断：** （相关 / 部分相关 / 无关）
