# 评审员抽检（请盲评，先别看大模型的判断）

标准：相关=能直接回答；部分相关=沾边但不够；无关=答非所问。在“你的判断：”后面填写。

## [#1] 问题：AI 产品的交互流程设计，有哪些容易踩坑的地方？
来源：《Aishwarya Naresh Reganti + Kiriti Badam》 00:45:43

Lenny Rachitsky (00:45:43): We've been talking for almost an hour already, and we haven't even covered your extremely powerful software development workflow for building AI products that you two developed that you teach in your course, that you basically combined all the stuff we've been talking about into a step-by-step approach to building AI products. You call it the continuous calibration, continuous development framework. Let's pull up a visual to show people what the heck we're talking about, and then just walk us through what this is, how this works, how teams can shift the way they build their AI products to this approach to help them avoid a lot of pain and suffering.
Aishwarya Naresh Reganti (00:46:18): Before we go about explaining the life cycle, a quick story on why Kiriti and I came up with this is because there are tons of companies that we keep talking to that have the pressure from their competitors because they're all building agents. We should be building agents that are entirely autonomous. And I did end up working with a few customers where we built these end-to-end agents. And turns out that because you start off at a place where you don't know how the user might interact with your system and what kind of responses or actions the AI might come up with, it's really hard to fix problems when you have this really huge workflow, which is taking four or five steps, making tons of decisions. You just end up debugging so much and then kind of hot fixing to the point where at a time we were building for a customer support use case, which is the example that we give in the newsletter as well.

你的判断：

## [#2] 问题：做 AI 产品的时候，产品经理和研发工程师要怎么配合才顺畅？
来源：《How Anthropic’s product team moves faster than anyone else | Cat Wu (Head of Product, Claude Code)》 00:02:16

Cat Wu (00:02:16): I feel very lucky to work with Boris. He's been an amazing thought partner. He's our tech lead. He's very much the product visionary, and he is great at setting, "This is what the product needs to be in three months, six months from now. This is what the AGI-pilled version of the product is," and a lot of my role is figuring out, okay, what is the path from where we are today to that vision three to six months from now? And I spend more of my time on the cross-functional, so making sure that our marketing team, sales team, finance, capacity, et cetera, are bought in on the plan and that we're all rowing the same direction and that once the feature is ready, that there aren't any blockers to shipping it.
Cat Wu (00:03:00): I think in many ways it works well because we kind of mind meld, but it is actually remarkably blurry of a line. I think we're 80% mind meld, and then there's this 20% of things that maybe I care a lot more about than Boris, so I'll drive those and 20% work he cares a lot more than me and he just drives those.
Cat Wu (00:05:03): I think before AI, technology shifts were a lot slower, so you could plan on these six to 12 month time horizons, and because you were shipping features at a bit of a slower rate, there was a lot more emphasis on coordinating with all the other partner teams to make sure that their shipping features that unblock your features because code at that time was very expensive to make. I think now with AI and with how much that has accelerated engineering and with how quickly the model capabilities are improving, the timelines for a lot of our product features have gone down from six month to one month and sometimes to one week or even one day. And with that, we actually need to make sure that products ship quite quickly.

你的判断：

## [#3] 问题：产品经理日常工作里，怎么用 AI 提高效率？
来源：《This CPO regrets that product management exists | Tom Verrilli (CPO of Whatnot)》 00:35:22

Lenny Rachitsky (00:35:22): So following that thread a little bit, what are some of the ways that AI has enabled you and/or your team to move faster and be more productive other than prototyping, which is the very clear benefit of AI for PMs and product teams? What else? What are maybe in the top three of, wow, this has really unlocked our productivity and the quality of what we do?
Tom Verrilli (00:35:43): I mean, the first one I think by a country mile is data science. We use Hex threads internally at Whatnot. I'm sure there are other comparable products, but I think it's almost hard to remember time as a PM before you had tooling like that where you could genuinely start pulling very nuanced cohorts of data where you could grab an individual user where you've heard a report. Actually understand, let's pull logs, help me understand exactly what this user did and saw. How many other users look like this? What would impact be? And then all of a sudden you can build pretty meaningful sensitivity models or forecasts of what might happen, regression models, et cetera, really, really, really quickly, which is incredibly powerful.
Tom Verrilli (00:36:25): The other thing that we've found is it helps us move much more quickly with shipping things because you can spot regressions and weird knock-on effects of two products into mixing more quickly than you used to be able to. And I think in really large complicated systems, that's always one of the things that ends up slowing you down of release trends and all of that versus if you build the right AI tool, you can spot regressions really quickly, which basically lets people just go.
Tom Verrilli (00:36:50): So I don't know what the future of data science looks like. But I think as a product manager, I've spent less time in the last year talking to a data scientist than I ever have in my career, even though I've probably spent 10 times more time in data and understanding actually how the product's working than I ever have in my career. So that one I think is really powerful.

你的判断：

## [#4] 问题：AI 功能的需求文档和普通功能的 PRD 有什么不同？
来源：《A guide to AI prototyping for product managers》 

Each AI tool will have very different outcomes based on their default settings and how specific you are. Here’s the exact same example with the same prompts using v0:

### Common use cases and prompt templates
Here are a few good templates you can use to get started with each of the tools I’ve highlighted:

#### **Task #1:** Build a prototype from an existing Figma design
**Prompt:**

`Build a prototype to match this design. Match it exactly. Use Tailwindcss.`

`Match styles, fonts, spacing, and colors.`

`[Include a single screenshot from Figma]`

**Tool:** Bolt

**Example:** Deployment manager

#### **Task #2:** Build a prototype from scratch with good UI design defaults
**Prompt**

`Build a prototype for [x].`

`This tool should:
- [Behavior 1]`

`- [Behavior 2]`

`- [Behavior 3]`

`Implement a simple initial iteration that meets these exact requirements.`

**Tool:** v0

**Example:** Sales calculator

#### **Task #3:** Build a dashboard to visualize data
**Prompt:**

`Build a prototype for [x].`

`Use Python and Streamlit.`

**Tool:** Replit

**Example:** Product analytics dashboard

#### **Task #4:** Convert a hand-drawn mockup to a prototype
**Prompt:**

`Convert the hand-drawn sketch to a functional prototype. Focus on frontend functionality.`

`Make it in the style of [product you like].`

**Tool:** v0

**Example:** Netflix-inspired blog

#### **Task #5:** Convert a PRD to prototype
**Prompt:**

`Implement a prototype to match the features in this PRD. Follow the exact specifications in the document. Focus on front end functionality -- do not include a server or database. Use Tailwindcss

[Copy/paste PRD. Include any relevant images]`

**Tool:** Bolt

**Example:** 2-factor authentication UI

#### **Task #6:** Build your personalized productivity tool
**Prompt:**

`Build a tool that does [x].

This tool should:
- [Behavior 1]`

`- [Behavior 2]`

`- [Behavior 3]`

**Tool:** Replit

**Example:** Substack image resizer

## **Solving prototyping problems—without knowing how to code**
Building your initial prototype is one thing. But one of the most common frustrations with AI prototyping is the errors the AI makes along the way toward a functional version. If you try to do anything even slightly complex, you’re likely to hit a wall. Knowing how to code becomes a superpower for debugging, but there are other approaches non-technical builders can use to still get great results.

你的判断：

## [#5] 问题：一个做传统产品的 PM，要怎么转型成 AI 产品经理？
来源：《Product manager is an unfair role. So work unfairly.》 

I believe the future of product management looks like Tal Raviv. He’s an individual contributor (IC) PM who leverages AI tools and a suite of productivity systems to get more done with fewer resources (and management layers). Throughout his more than 10-year career, Tal has actively chosen to stay an IC and, over that time, has honed a set of productivity practices that give him tremendous leverage and impact—beyond what many traditionally believe ICs can achieve**.**In other words, he’s become a “super-IC.”Below, Tal shares seven of the unique productivity tactics that have gotten him to where he is today—and might help you become a super-IC too.

*Tal was an early PM at Patreon, Riverside, Wix, and AppsFlyer. For more from Tal, check out his 63 free video tutorials on using AI agents at work, his other popular guest post on building your AI thinking partner, and his episode on Lenny’s Podcast. You can also book Tal for an AI build sprint with your team.*

Product management is unfair. We’re expected to be on both a maker *and* a manager’s schedule. Nothing is planned around “PM capacity.” We can’t hire or fire but are expected to make things happen (and fast). We are the cushion for organizational dysfunction. Any PM reading this could add a dozen more reasons.

And this is in the best-case scenario—assuming you’re on an empowered product team with a clear strategy, inside a business that’s growing.

Unfortunately, it’s only going to get harder from here. In the past few years, we’ve seen the “great flattening” of tech: rising expectations of fewer ICs to own larger swaths of the product and manage multiple teams while staying hands-on. Rapid advances in AI are only accelerating expectations of what one PM can handle.

“Fairness” isn’t coming.

The good news is that great PMs are making it work.In this newer, flatter tech industry, PMs who thrive will be the ones who build their own systems, methodologies, and tools to make the job work for *them*, not the other way around. They’ll start working “unfairly” today to lead successful teams without sacrificing their own well-being.

你的判断：

## [#6] 问题：想推进一个 AI 功能，要怎么跟领导争取开发资源？
来源：《OpenAI Codex lead on the new shape of product work | Andrew Ambrosino》 00:40:36

Andrew Ambrosino (00:40:36): I welcome the moving of goalposts because that means we're making product progress. There have been a lot of explorations here around autonomously developed software. A lot of harness engineering stuff, a lot of different explorations on like, "Okay, well, what if you came in overnight and did garbage collection of the code base to clean it up?" One thing that I think all models suffer with right now is just they usually increase complexity.
Andrew Ambrosino (00:41:01): If research is listening at any company, please make the models better at deleting code. But that becomes a problem right now when you try to put development completely on autopilot and it's both on the human side and the code base side. So feature requests. How do you teach a model which features to build, which ones to ignore, which ones to group together and reframe a little bit? How do you teach to model how to build the right abstractions?
Andrew Ambrosino (00:41:31): All of this is getting better. I don't think we're at place yet where we're like, "We're just going to set up a loop that's like improve the app." And listens to Twitter and listens to Slack and listens to email. We're not there yet, but we're trying to make it happen.
Lenny Rachitsky (00:41:49): Do you think we'll get there? Do you think we'll get to a place where it's just like grow, win?
Andrew Ambrosino (00:41:54): Slash goal, make money, make me a billion dollars.
Lenny Rachitsky (00:41:58): Win the market.
Andrew Ambrosino (00:41:58): I don't know, man. I am not in the business of saying never or always or whatever.
Lenny Rachitsky (00:42:05): Yeah. How are you using AI in your work as product leader, eng leader?
Andrew Ambrosino (00:42:10): Yeah.
Lenny Rachitsky (00:42:11): What are some ways that you use it that maybe people may not be aware they can use AI for?
Andrew Ambrosino (00:42:15): Yeah, I think I have the best job in the world right now. But one of the things that makes it very fun is that when we were developing the original Codex app, the goal for me personally was to make it the thing that I wrote the code with. I was like, "I need to make this so good at development that I can build the Codex app with this." And the Codex app at that time was a development tool.

你的判断：

## [#7] 问题：老板想看个 AI 功能的 demo，我没有研发资源，怎么自己快速做出来？
来源：《Anthropic’s first technical PM on token maxing, the jagged edge, and living in the future | Dianne Penn》 00:51:40

Diane Penn (00:51:40): It's not necessarily easy for someone to agree or be able to see what a good or great AI product or AI feature could look like if they haven't kind of experienced building themselves. So I do feel pretty strongly that if you're a manager, you have to be hands-on; you have to spend a portion of your time actually shipping. You have to kind of walk in the shoes of your teams. And I always try to carve out a portion of time to actually own one to two work streams when we have models in order to keep my theory of mind, keep my sense of how the models are moving, how quickly it's improving, so I can help the team make decisions and make better decisions.
Lenny (00:52:35): So what I'm hearing here is no matter where you are in the ladder of hierarchy at a company, if you're not building yourself, if you're not actually talking to cloud, talking to Codex, building stuff, you're not going to make it.
Diane Penn (00:52:46): And you should have fun working with this technology. I think that's the other piece. I think the folks that would be most successful, regardless of their level, are people who love working with AI and are exploring and experimenting. And carving out the time, not just for the experimentation, but actually hands-on shipping end-to-end, getting the user feedback, I think has to be fundamental for everyone.

你的判断：

## [#8] 问题：Duolingo 当年是怎么把用户增长重新做起来的？
来源：《How Duolingo reignited user growth》 

### **Phase 2: Referrals**
Feeling burned after our gamification effort, we completely pivoted away from improving retention and put together a new product team focused on acquiring new users, called the Acquisition Team. At the time, Uber was doing well with user acquisition and had reputedly grown largely because of its referral program. Inspired by this, we created a referral program similar to Uber’s. The reward was a free month of our premium subscription, Super Duolingo (at the time, it was called Duolingo Plus). Seemed like a pretty good offer to us!

We implemented the feature and hoped our second attempt would be more successful. Instead, new users increased by only 3%. It was positive, but not the type of breakthrough we needed. Still, the team doubled down and pushed through, shipping iterations to the referral program and making some other bets, but no avail.

While the team continued to iterate, it became clear to me that we had to find a different approach to tackle our growth problem.

### **Time to regroup**
The aftermath of these back-to-back failures in only a few months was a period of reflection for me about making better product bets.

In hindsight, it became clear why the Gardenscapes moves counter was not a good fit for our product. When you are playing Gardenscapes, each move feels like a strategic decision, because you have to outmaneuver dynamic obstacles to find a path to victory. But strategic decision-making isn’t required to complete a Duolingo lesson—you mostly either know the answer to a question or you don’t. Because there wasn’t any strategy to it, the Duolingo moves counter was simply a boring, tacked-on nuisance. It was the wrong gamification mechanic to adopt into Duolingo. I realized that I had been so focused on the similarities between Gardenscapes and Duolingo that I had failed to account for the importance of the underlying differences.

你的判断：

## [#9] 问题：做 AI 产品的时候，产品经理和研发工程师要怎么配合才顺畅？
来源：《Product manager is an unfair role. So work unfairly.》 

I believe the future of product management looks like Tal Raviv. He’s an individual contributor (IC) PM who leverages AI tools and a suite of productivity systems to get more done with fewer resources (and management layers). Throughout his more than 10-year career, Tal has actively chosen to stay an IC and, over that time, has honed a set of productivity practices that give him tremendous leverage and impact—beyond what many traditionally believe ICs can achieve**.**In other words, he’s become a “super-IC.”Below, Tal shares seven of the unique productivity tactics that have gotten him to where he is today—and might help you become a super-IC too.

*Tal was an early PM at Patreon, Riverside, Wix, and AppsFlyer. For more from Tal, check out his 63 free video tutorials on using AI agents at work, his other popular guest post on building your AI thinking partner, and his episode on Lenny’s Podcast. You can also book Tal for an AI build sprint with your team.*

Product management is unfair. We’re expected to be on both a maker *and* a manager’s schedule. Nothing is planned around “PM capacity.” We can’t hire or fire but are expected to make things happen (and fast). We are the cushion for organizational dysfunction. Any PM reading this could add a dozen more reasons.

And this is in the best-case scenario—assuming you’re on an empowered product team with a clear strategy, inside a business that’s growing.

Unfortunately, it’s only going to get harder from here. In the past few years, we’ve seen the “great flattening” of tech: rising expectations of fewer ICs to own larger swaths of the product and manage multiple teams while staying hands-on. Rapid advances in AI are only accelerating expectations of what one PM can handle.

“Fairness” isn’t coming.

The good news is that great PMs are making it work.In this newer, flatter tech industry, PMs who thrive will be the ones who build their own systems, methodologies, and tools to make the job work for *them*, not the other way around. They’ll start working “unfairly” today to lead successful teams without sacrificing their own well-being.

你的判断：

## [#10] 问题：一个做传统产品的 PM，要怎么转型成 AI 产品经理？
来源：《Why LinkedIn is turning PMs into AI-powered \"full stack builders” | Tomer Cohen (LinkedIn CPO)》 00:38:49

Tomer Cohen (00:38:49): Now everybody talks a big game about fine-tuning but again, two years ago, fine-tuning was something that the product folks thought the engineering team was supposed to do. No, it's the whole organization. In fact, you can build a whole strategy just on data collection and fine-tuning and your product will see tremendous success or you can delegate it and it will never happen. So in many ways that was bringing into the fold, in our phase one, which really started around 2016 for me and every team I went to, the AI component was the area I spent most of my time on. I hired people for that. Product leaders, I spent most of my, back to how do I spend my resources, most of my resources there. And it was my top priority all the way from strategy to talent. And ultimately with the last couple of years we've seen this metamorphosis of AI and this incredible new wave and we've done a pretty big change there as well over the last two years.
Lenny Rachitsky (00:39:49): I love this. So I took some notes on what you're talking about. So the big message that I'm taking away so far is as a product leader, you need to think about things that you thought the engineering leader had to think about or the ML engineer was thinking about things like what is the objective of our algorithm? What are the features that we're building into it? What is the data collection strategy? How are we fine-tuning it? As a PM, you should be asking these questions.
Tomer Cohen (00:40:13): In fact, you should go all the way to infrastructure. You can have massive lifts in your product outcomes and goals if you probably enhance your infrastructure. How many product people talk about the infrastructure they have? Not many. Influencers, those are things ultimately your goal is to win with your products and build a much more experience to your members and customers. Literally just changing the infrastructure on top of what you build. That could be the biggest lever than you building another button or experience for your members on the top of it.

你的判断：

## [#11] 问题：产品经理日常工作里，怎么用 AI 提高效率？
来源：《This CPO regrets that product management exists | Tom Verrilli (CPO of Whatnot)》 00:13:18

Tom Verrilli (00:13:18): It's certainly easier to move fast with AI tooling if you've got well-honed judgment. You can pull data now on a Hex thread that is basically what it would take a week, two weeks with an Amazon L7 data scientist in 2017. And so if you're empowered and have good judgment, you can basically make really quick decisions and just keep people moving, which is extraordinary.
Tom Verrilli (00:13:41): But more than just AI, I think it's also a lot of those ratio pushes also came with a bunch of other cultural pushes like hire great people and get out of their way, bottoms up roadmaps, and all of those pieces where I think there's been a bit of a cultural shift in tech over the last little while, which is like actually top-down's pretty good because folks at the top, generally speaking, can make quick decisions and remove all of this alignment debate. They have probably more macro context than most folks. And assuming that they are genuinely in touch with ground truth and are good enough, it's actually a really efficient model to be able to have senior leadership involved in a lot of those decisions, which means it's not just the tooling that makes them efficient, but you can have one very senior PM across more things and they can be more efficient than having three relatively entry level PMs. But certainly AI makes all of that a lot easier again.
Lenny Rachitsky (00:14:34): So just to coming back to the broad premise, which I think is very important to clarify, this point about regretting product management exists isn't saying we don't want or think PMs are useful. It's that it is better to not assume we need a PM in every place. And it is great to enable other functions to do the PM work. And also just PMs take away the reps from people being able to do the things that PMs do. And if they can do that work, they can actually execute better, build better products for people.

你的判断：

## [#12] 问题：老板想看个 AI 功能的 demo，我没有研发资源，怎么自己快速做出来？
来源：《How to close $100K+ enterprise deals, step by step | Jen Abel》 00:37:41

Lenny Rachitsky (00:37:41): So some people listening to this may sound like a lot of work. I imagine that this is what separates companies and products that win deals versus not. You could have a better product, you could have a better price, a lot of things, but just not executing in this way through the sales process is probably shooting yourself in the foot.
Jen Abel (00:38:00): Or you're stuck at you just sold the enterprise on a $15,000 solution, which goes ... How do you expand that? The whole game is expansion. If you're not going from 100k or 250k to 350 or 500 the following year, it's not an enterprise motion.
Lenny Rachitsky (00:38:17): Okay. So just to quickly summarize we're at, step one, landing the meeting, then running the intro call. Then there's this follow-up intro call, which you pointed out as often ignored and a big opportunity to improve the demo. I love the way you described the demo. It's this carrot that you're holding that you can use a little bit to extract more. And then there's step four, is prepping the pitch and framing the demo. Is there more to share there?
Jen Abel (00:38:43): No, I think we're at the point where it's like, okay, now you're running a big demo, right?
Lenny Rachitsky (00:38:47): Okay, cool. Yeah, step five.
Jen Abel (00:38:50): Now you have all of the people involved in the demo. You might have somebody that's involved from their AI team that's going to support some rollout. You might have somebody ... You want all of the people involved in this decision at that table for the demo. That's how important it is to not rush it, okay? So now you're running the demo. Before that demo on one of those calls, who are all these people? What do they care about and what should I avoid? The person that you've now built this relationship with can give you all of the intel. At this point, they want this to go forward. Now this is a great star for them of, "I found this amazing tool. It's going to solve our problems and now I get to put my name on it alongside one or two other people," right?

你的判断：
