---
title: "A Good Day’s Work Looks Different Now"
date: "2026-10-23"
summary: ""
description: ""
toc: false
readTime: true
math: false
draft: false
---

> Originally submitted for [the pragmatic engineer essay contest](https://blog.pragmaticengineer.com/how-software-engineering-is-changing-an-essay-challenge/).

In January 2026, our founder announced in the engineering-wide Slack channel that \~zero “hand-crafted” code would be
allowed from that day forward at Atlan.

The next time any of us wrote code by hand, we’d have to explain ourselves for the grave sin we had just committed. This
was an org-wide mandate with the only exception being legacy systems that required some manual effort to fix intricate
bugs, but if you were working on a new system at Atlan, you could not write code for it by hand. We were told to treat
the act of writing code by hand with the same seriousness as we would a SEV1 incident: we would sit down and review the
exact circumstances that had stopped us from using agentic tools to build and/or improve that particular system or
product.

If you made someone read the above paragraph in 2023, they would probably feel a chill run down their spine.

It was a few weeks after we had all returned to work from the Christmas break. I had spent the past few weeks
vacationing and celebrating New Year in Vietnam with my friends. While I was there, the world was witnessing what went
on to be known as the “Opus 4.5” moment of AI.

During that holiday season, a good number of founders and engineering leaders had spent their time at home tinkering
with Claude Code paired with the newly released Opus 4.5 model and had come to the conclusion that software engineering
had finally reached a point of inflection: that almost all engineering work could be done well with the help of agents,
and they were right.

Our ban on “hand-crafted” code was the point of criticality after a long set of initiatives to experiment, explore and
almost white-knuckle AI adoption across the company.

I had spent the past five years at the company growing from an intern to a senior engineer. My first reaction was that
the announcement seemed obvious, because by then, for most of us, using agents was the default way to write code. It was
a bold and welcome change. In the coming few weeks, it slowly dawned on me that the world we knew as engineers was about
to die and a new world order was being set in our industry.

This article is about the story of a company that willingly underwent a massive AI transformation, fully bought into the
hype and showed radical openness when it came to disrupting itself and figuring out the AI-native way of operating
almost every function. I was right in the middle of that roller-coaster ride, and wanted to write about the human
aspects of being an IC during this transition, about what it felt like to find meaning in my work again along with some
technical lessons I picked up along the way. It’s a story about feeling the rug pulled out from under you every week but
still finding joy and fascination in doing technical work and establishing a new definition of what a good day’s worth
of work looks like now.

As you will see, during the transition I played a key role in trying to drum up excitement around AI in the company, sat
on committees that made decisions about company-wide procurement and the developer evangelism that followed. And it’s
about reflecting on that excitement and at the same time struggling to find meaning in what I did.

I moved on from Atlan in April 2026 and transitioned into a more AI research role. That decision was separate from the
transition I describe here. After five years doing similar work at the same company, I was bored and wanted to try
something different. I wanted to do more research-adjacent work on agentic platforms and data analysis agents. I've had
time since then to reflect on those years and write this memoir.

I came into Atlan in 2021 as an intern. I was a sophomore at college pursuing my engineering degree in computer science.
Atlan, back then, was primarily a data catalog product. The bread and butter of the platform was to fetch metadata from
every tool in the modern data stack and build a 360-degree pane of glass for your data estate. On top of this metadata,
it offered features like data governance and end-to-end data lineage.

I joined as the second engineer in the orchestration team, tasked with building connectors and the underlying developer
platform to empower other engineers to build connectors. Over the next year, I mostly wrote Argo Workflows and Python
scripts to do metadata ETL. This was the hockey stick growth phase of the company.

My first task ever was to build a connector that could extract metadata from PostgreSQL databases and write it back to
our metadata store. This involved writing fairly complex SQL queries that queried and joined data from PostgreSQL’s
information schema and some other pg_* tables. This task alone took me around three weeks to ship to completion.

Atlan’s engineering culture during my early years was one of merit and earned trust, nothing radically different from
tech startups of our size. You had to be in the trenches and ship consistently to earn your stripes and if you got
results, you would be trusted with higher scope and stakes, regardless of pedigree or seniority.

Earning trust in the team looked a lot like consistently demonstrating sound technical knowledge via sustained deep work
that led to good production-ready code. Some of the most celebrated engineers and architects were the ones who had
immense capability to do deep work and iteratively chip away at the right set of problems.

The vibe in general was of growing together as a team and actively engaging in giving feedback to your peers so that the
team could win. “Software engineering is a team sport” was a phrase that was thrown around often. The leadership and
managers always preferred staffing teams with people who focused on making sure everyone in the team played to their
strengths and was given enough support and feedback. My first two years were a really magical time when I was able to
pick really interesting problems, solve them, learn from them and at the same time feel that I belonged in a team of
people who genuinely were rooting for me to do great things.

We had an engineering commandment which went “coding is not engineering”. It basically meant that a single person in a
team writing clever code is never going to help us achieve our goals. It encouraged us to zoom out and always think
about the bigger implications of the system and architectural choices we were making.

This was one of the reasons there was no one of the archetype of
“rude-genius-coder-who-fixes-everything-by-staying-up-at-night” in the upper ranks in engineering. The leadership
preferred genuinely helpful and collaborative senior engineers who would rather win as a team and not ride on the high
of their own vanity. Another cultural aspect of engineering was an obsession with measurable customer impact. Most
appraisal and promotion conversations were always done based on impact, very similar to how Meta does it. We did not
like doing rewrite-in-Rust kinds of projects just for the sake of it.

Deep work was really encouraged. We tried to make sure everyone got enough distraction-free time where they had the
space to lock in and work on their problems. We tried not to have too many meetings and not to context switch too much.
I remember having multiple 1:1s with my managers about how to control my context switching. We understood that
firefighting all the time was the easiest way to wear out engineers and we tried our best to reduce excessive
firefighting.

I basically spent two years obsessing over protecting my deep work slots. Getting distracted basically meant my impact
and growth would decline.

By 2023, we had a few hundred customers, the current version of our product had found PMF and we were growing steadily.
OpenAI had launched ChatGPT in November 2022.

OpenAI launched the ChatGPT API in March 2023. A month or so later, I saw a thread from my founder Varun talking about
how he had spent the weekend experimenting with it by building a simple RAG workflow on top of a markdown dump of some
of our internal support documents on Notion. He had casually remarked that we should look out for developments in AI
because it felt near magical to see the LLM understand internal company context and answer questions.

At that time, the only AI-assisted code tool we were all dabbling with was GitHub Copilot. I remember bragging about
just writing a lengthy comment and generating a full module just from code comments in my standup. As ChatGPT grew in
popularity and we got access to it inside the company, the standard practice became to paste snippets of code into the
chat window and ask it questions or have it generate small pieces of code for us. ChatGPT at that time felt more like a
writing tool than something you could use for serious engineering work.

Soon enough, by August 2024, I was part of a small cohort of engineers who were asked to evaluate a bunch of AI-assisted
IDEs like Cursor, Tabnine, GitHub Copilot (with the chat) etc. and give our reviews so that we could procure seats
accordingly for all of engineering. This cohort consisted of a mix of engineers from all teams, frontend, backend,
infrastructure, etc., so that we could get a range of opinions.

This was the first time when I spent some time setting up Cursor in a way that I could do all of my BAU tasks using it
and it honestly blew my mind. I was hooked. Their tab completion was magical. The ability to do CMD+K and highlight a
block of code and suggest a change in English honestly felt like a step function change in productivity. You still
needed to go to individual files and write out targeted, granular instructions to make changes.

Once we greenlit Cursor, it did not have immediate adoption. There were some power users who were using it to the
fullest, sharing .cursorrules files along with tips and tricks on how to use it for different types of tasks. I was part
of this cohort. I had already started using it to make meaningful progress on all of my features and bug fixes. At this
point I did feel like I was losing a bit of touch with my raw ability to write code, but it did not feel existential in
any way. I was still deciding how to structure modules, which classes went where and things like that. Using Cursor then
felt more like being able to ask AI to implement code which followed established patterns. As time went on, engineers
did find the time to read up, set up their working environments differently and start using tools like Cursor.

After looking at Cursor’s success in the engineering org, and after both the founders had played enough with AI in
general in their personal time, the leadership was increasingly getting convinced that we would need some top-down push
in the company to catalyse AI adoption, because the productivity gains from it were hard to ignore.

One of the cultural landmarks of this whole AI transformation journey was the AI productivity challenge that ran in Q1
of 2025. The rules were very simple: you post in a Slack channel about a tip/hack/workflow that gave you a nice
productivity boost using AI, you get points for Slack reactions, comments etc. This runs for a quarter. The person with
the most points wins a sweet iPad. The point was to offer an incentive for people to find productivity hacks in their
day to day and post about them so everyone could learn from it. If folks find your tip helpful, you get points.

Along with this challenge, we also set up a company-wide LiteLLM instance that allowed AI access for any employee to
almost all the models in the market, no cap on budgets.

This challenge spread across the company like wildfire. Folks from every department were participating in it and all
kinds of tips and tricks were flowing here and there. Everything from AI notetaking apps, meeting notes to feature
flows, managing multiple agents, writing skills to orchestrate a set of things. Writing copy, analyzing customer intel,
debugging production failures. It felt like everyone’s first priority was to figure out how to use AI to solve
something. This was the first catalyst that encouraged people to go all in for changing how they work day to day. Before
this, AI was a topic in enthusiast circles discussing tricks in DMs but this challenge lit a fire in the company and AI
became a common conversation topic.

What followed alongside the AI productivity challenge was the reinstating of demo days. We used to do this every Friday
when we were a small engineering team. As the department grew and as more processes came up, naturally shipping had
slowed down and we did not really have something to demo every week. We had moved to a more monthly demo cycle. But
after the AI push, we wanted to shrink shipping cycles and encourage everyone to try building something with AI.

So we had people from every department building something fun and silly to get a taste of building software with AI. I
remember this one HR rep who built a nice trivia game about NFL players. Another one built a coffee timer. In a few
months, almost everyone in the company had run Claude Code and understood how radically simple it was to build software
now with AI.

I was part of the team responsible for designing the onboarding structure for the incoming class of new interns we had
every year. Atlan was a fully remote company and it was really hard to onboard interns in a remote setup, so to
jump-start the process, we would fly out the new set of interns for an onboarding offsite, where senior engineers from
every team would also join us and spend the week working with the interns in person to onboard them, explain how our
systems worked and end the week with a fun hackathon. It was one of the most exciting weeks for me every year. We all
loved having long conversations with the new interns to understand their aspirations and use all that knowledge to map
them to the right teams so they could be set up for success.

I remember writing a memo in 2025 to rethink our onboarding completely to make it as AI native as possible. They were
going to be operating in a company that was fundamentally trying to use agents as much as possible.

In comparison, we had spent a good chunk of the week in the 2024 version of this onboarding just talking about our
existing systems, how to succeed as an intern at the company and a few small sessions on how to use editors like Cursor.

In 2025 we spent a considerable amount of time talking about how to look at problems and design agentic systems to solve
them. We spoke about RAG systems, about verifiability, about evals etc. And this was a clear direction we all committed
to make sure that all the incoming engineers were being given the correct expectations for what was about to come.

By this time, I had started work on something which was going to become a year-long story of migration and burnout. It
was a new service meant to replace an old set of workflows that took care of the L part of our ETL stack. We wanted
something flexible enough that you could dump Parquet files in an S3 path, point the service at that path, and let it
chug along. It would diff those files against the current state of the workflow and write the results to our metadata
store.

I used Cursor and Claude Code to generate a lot of the code and was able to finish the actual service in a few weeks.
This was before Opus 4.5. After that came a long slog of careful rollouts, plugging intricate bugs and edge cases, and
going through the hell of testing it again and again.

There were bugs around Parquet schemas and how corruption was handled. The models I was using were not very good at
getting the try-catch blocks and error handling right, and I had not spent enough time hunting down those issues either.
There were performance problems because parts of the service had not been parallelized enough. All these small paper
cuts became visible once we started running it against the variety of data you encounter in a production ETL service.

The generated tests were also extremely narrow. The model would generate a function and a unit test for that function,
without really taking into account how it fitted into the rest of the system or what needed to be tested together. We
slowly added more tests and plugged those gaps, but it took time. This service sat directly in our regular write path. A
failure there could lead to a SEV1 or even a SEV0 outage.

It was difficult because it felt like all the interesting parts of this project had been taken away from me. The agent
had done its job mostly guessing things almost correctly, and I was stuck with the boring parts of going through the
tail end of all the edge cases. Spending so much time in QA almost burnt me out. In all my naivety, I had not spent
enough time building the verification scaffolding or planning the rollouts in a way that agents could help investigate
and fix the bugs that came up.

We also had to wait for the models to get good enough. By January 2026, we had set up a skill that could take a Temporal
workflow URL, use the Temporal API to download the logs, and investigate the failure. We had spent time improving error
tracking and assigning proper error codes. When a workflow failed, it would report a detailed error with instructions
for an agent on how to fix it.

That was usually enough for an agent to follow, make the change, and create a PR with tests. By the time I handed over
the project, we could give the skill a workflow URL and let it work through the failure. Getting there had taken a lot
longer than generating the service in the first place.

Another project that went through such a rug-pull was our Application SDK. Our internal ETL platform used Argo
Workflows, which meant engineers had to write their workflows in YAML. Wrangling all that YAML was annoying, and you
needed a cluster just to test things. This really pissed off a lot of people.

I think the SDK effort started towards the end of 2023. The idea was to move to Temporal so we could write workflows as
code, and build a thin wrapper around its SDK. We wanted engineers to be able to define dataframe-like operations
easily, with ergonomic APIs for connecting to other Atlan services. We also wanted to expand the number of connectors we
offered by getting third-party developers and system integrators to build them. For that to work, we needed a mature SDK
that made building a connector straightforward.

By the time our SDK was ready, a lot of the code was already being written by agents, even with the models available
before Opus 4.5. So the effort became about making the SDK very easy for agents to use. We designed it so that there was
only one way to accomplish a particular task and followed agent-friendly design patterns.

As the SDK went into production and people started using it, we also started wondering how much of it we would need if
model capabilities kept improving. Our thinking was that the models already knew how to use Temporal's SDK. An agent
could read the documentation for a source, set up a small test environment and start building a connector directly.

In 2026, we started an internal project to make that whole pipeline headless. You could spawn an agent in a sandbox,
give it access to the credentials and documentation for a tool, and let it build, run, test and validate a connector in
a loop. Agents were getting capable enough to build simple connectors within a few hours and handle things like errors,
edge cases and scaling. A lot of the engineering effort went into setting up that loop and writing the markdown files
that explained what had to be done and what the end product should look like. I remember one engineer taking on that
initiative with her swarm of agents.

There was a related project around generating test data. For something like a Snowflake connector to be production
ready, you need to test it against an instance populated with different kinds of data. We built an agentic system that
could take a use case or test case and populate a Snowflake, BigQuery or Redshift instance accordingly. That took care
of a lot of the testing work needed to make sure a connector was ready for production.

This changed how we thought about expanding our connector coverage. We had planned to give system integrators a good SDK
so they could build connectors for us. Now we could also set up agents to work on connectors all night, with multiple
attempts running at the same time. The SDK had started as a way to make things easier for engineers. Those engineers
started using agents, the agents kept getting better, and we ended up rethinking the whole way we wanted to build
connectors.

There was also Mothership, an internal agent platform built by colleagues I was friends with. I was not personally
involved in building it. The idea was that you could mention Mothership in Slack and give it a task. It would clone a
repository, do the work and send you a PR. It started off fairly simply, spawning a Claude Code session in a cloned
repo, and later gained more sandbox capabilities. It was an experiment in what collaborative coding through Slack could
look like.

All these projects were attempts to rethink how we worked as agents became more capable.

It was heart-warming to see so many of my colleagues get on board and be ready to embrace this change head on. It took a
certain kind of person who was ready to let go of ideas that had formed so much of their sense of self-worth and craft
to embrace this new world with open arms. I saw engineers who were revered for the quality of their code reviews openly
say and discuss the death of code reviews with AI in the picture. When the whole AI push started from the top, in a
month or two, almost everyone was on board ready to experiment, learn and be candid about the shortcomings and discuss
solutions.

In all honesty, we ourselves were going through an existential crisis as there were a lot of opinions that data catalogs
like ours wouldn’t really be useful in a few years if we didn’t understand AI well and position our product for this
changing industry landscape. The AI tailwind could be genuinely game changing for us and we wanted to experiment and
learn and stay ahead of our competitors as much as possible.

All of the engineers had grown in their careers believing that the world rewarded expertise. It was nice to see people
keep their personal egos aside and focus on how they could reinvent themselves to be in service of the larger mission of
the company. How quickly people took this on board and were open to learning and changing was deeply inspiring.

A few weeks after that, in the weekly demo calls, I was presenting an internal site which you could use to browse the
Cursor rules set up by other teams easily. I opened that presentation by pulling some data on Cursor usage and made a
claim by saying something like “6 out of 10 engineers in the company are using Cursor daily”. After the call, I was
added to a group DM by a few EMs to discuss what we could do to understand and encourage the rest of the 40% who had not
really gotten on board with this new way of coding. It had already been around 8 months since using tools like Cursor
had been encouraged.

That moment quickly became one of the starting points of what I would call a sort of witch hunt across the engineering
org to find engineers who were reluctant to embrace this new age of tools and had not really restructured their day to
day work to leverage AI as much as possible. This followed a phase of token usage tracking and a push from managers to
use AI as much as possible. People were brought into calls for instructions and tutorials on how to use these tools, and
to discuss their reservations.

It was becoming increasingly clear that the new direction of engineering culture at Atlan would be one of AI-native
engineering. I remember a few very senior engineers who specialized in frontend work leaving because the leadership
wanted them to become more full-stack and take on a broader scope as the coding agents could do most of the frontend
work. But they insisted that they wanted to specialize and go deeper in their frontend expertise. This was one of those
moments where we all collectively realised that raw technical expertise might not be the most valued thing anymore.

With more and more push from the top to embrace AI, it was natural to see a rise of virtue signalling when it came to AI
usage. It mattered more to appear to be someone who uses and embraces AI rather than be someone who creates a lot of
customer value using AI.

There was a period of a few months where people understood that given the witch hunt happening across the org, it was
paramount that you constantly post in common channels about how you have automated so much using AI. Every other week we
had a lot of people talking about skills and workflows of how AI had been used to make a narrow function fully agentic.

There was also a general disregard for the architectural cohesion of the underlying software that made the workflow
possible. If the agent had to read logs and traces from random places and do some funny things to get the data to make a
decision, that sort of thing was overlooked because it was more important to put that message out on Slack to give the
impression of being someone who is very AI-savvy.

AI nativity was increasingly discussed in promotion conversations and there was a new kind of engineer now that was
valued more, so it made sense to partake in the virtue signalling to make sure they were constantly in the AI chatter in
the company. It was more important to convince all the EMs that you were AI native than it was to make technically sound
long-term decisions that would allow more agents to leverage the infrastructure we already had.

Engineers preferred one-shotting features that were assigned to them via layers of sophisticated context engineering and
evaluation-driven development, then doing calls about the process and writing long Slack messages announcing their
triumph of delivering something in days that would have taken months in the old world of doing engineering.

In that moment, the virtue signalling did feel selfish and annoying, but in hindsight considering the pressure all of us
were under, it was fine. We were all quick to learn that this virtue signalling was a bit hollow without actually seeing
this software function in prod and waiting enough time to understand the quality. We counted our chickens before they
hatched, but all of us were riding that high of optimism that we wanted to believe that software engineering, in
general, as a whole was fully solved and we did not have to involve ourselves in the bottom-tier of the details and all
of us could be like swarm orchestrators and take on bigger and bigger projects.

Around October 2025, everywhere online and also in our company, unfortunately, we started seeing signs of major AI
psychosis start to set in.

We tried to jump on every new AI trend as soon as possible. Clawdbot was one of these. I think we picked it up around
November 2025, before it was called OpenClaw. Someone in the company had made a reusable Helm chart for it. So any team
could set up its own claw, give it a bunch of markdown files and have it turn up in Slack. A week or so later, every
team had one going through the Linear backlog and looking at workflow failures and errors.

Man, what a mess that was. We had an army of roughly 10–15 claws talking to each other in our shared Slack. Claws were
pinging other claws, which created a whole new set of problems. Most of the time the clankers were confidently reading
partial signals, raising unnecessary alarms and making a mess everywhere in Linear and Slack. I remember a claw bot
asking me for updates very aggressively. Scolding a claw to mind its tone was not something that was on my bingo card
for the year. With time we figured out how to drill some sense into these claws and at least keep them from flooding
every work product with slop.

As a result, all of us became very aware of the gaps that came up in production from software that was built using this
new way of working.

Learning to build good evals emerged as an important skill that all engineers learnt by burning their fingers when the
edge cases missed by the agent were encountered in production.

A good example of this was the popularity app built by a colleague in March 2026. They wrote extremely long markdown
files explaining what needed to be built and let an agent work through them. In about two days, they had an
implementation that passed the tests.

Popularity is a very verifiable problem. You take a bunch of SQL queries, parse them, figure out which tables were used
and assign popularity scores using a logarithmic function. This lets customers understand which tables are used the most
in their warehouse. We had historical data on S3 for almost every customer, so there was plenty of data we could point
an agent at and ask it to build a verification harness.

But before we had really worked through all that verification, we were quick to announce the result on Slack. We had
built a new popularity system in two days, when the previous system had taken almost six months to build and make stable
in production. We all shared in that optimism. It made us feel invincible that we could ship fairly complex software
this quickly.

There was still a lot of QA and testing to do. The new system had its own long stretch of stability issues, usually gaps
that the agent had missed. It felt like the waterbed theory of computational complexity: the effort we saved in building
the thing shifted to verifying it and plugging those holes. We came out ahead net-net, but the two-day implementation
was only part of the work.

Another project I followed through colleagues was the five-hour MTTR effort. I was not involved in this one either. It
started with support-ticket triage: could an agent gather enough context around a ticket and get it to the right owners?
The team then wanted to reuse Mothership to take a Zendesk ticket through reproduction, bug fixing and eventually
release.

My understanding is that they eventually got most tickets through to a PR, with human review and approval still
required. By the time that system was fully in production, I had left the company. Five hours was the target behind the
initiative.

We all realised very quickly that the org had calcified around its processes. Handovers worked a certain way, and data
silos had formed around the communication patterns. One of the first things a team had to do when trying to make its
work AI-native was to make all that state queryable. This sounds a lot simpler in theory than it turned out to be. Most
of our engineering context sat in separate tools, and agents had to connect to multiple MCPs to gather it.

In the migration service, this meant making workflow logs available through the Temporal API and adding detailed error
codes and instructions. We had to do that work before an agent could reliably investigate a failure. You really need to
make those surfaces queryable, or you end up with fancy demos without much long-term durability.

A lot of articles conveniently put aside this human aspect of working while the rug underneath your feet is pulled
almost every week while trying to keep up with the releases of new models and tools. This is something I really wanted
to discuss in this article.

Despite what people believe, a lot of engineers like to think of themselves as artisans who are also building cathedrals
so that millions of people around the world could use the fruits of their labour and do something productive.

How much AI has disrupted other industries is still up for debate, but one thing AI has unequivocally disrupted is
generating code. It’s so good at generating code that most problem spaces where AI is not productive are rethought as
spaces where everything can be modeled as code. If generating animation is just generating code, let’s get AI to
generate that instead of learning how to do a bunch of clicks around a complicated UI.

But not a lot of people talk about the human experience of navigating this tsunami of change, loss of self-worth and
still picking ourselves up and learning new things to ensure that we can be productive in a new world and push the
frontier even ahead.

I started enjoying engineering again after Opus 4.5. That was when I could start doing the multi-worktree, multi-agent
thing, split my terminals eight different ways and take on several things at once. I was involved in a few more projects
by then. I could have an agent doing bug fixes on one side, another doing performance profiling and writing reports,
while I worked on something else.

They had gotten accurate enough that I could trust them more and focus on the bigger picture. Working with an agent that
did the menial labour but still needed me to check so many things had been really annoying. I could not get to the point
of running five, six, seven initiatives at the same time because I was still spending so much time checking the work.
After Opus 4.5, that started becoming possible.

I started thinking more about whether I was engineering things in a way that would give agents enough context to make
decisions. Could the system produce useful context as it ran? Could the agent get the information it needed? The work we
had done on error tracking and instructions in the migration service was part of that.

I remember in February 2026, when we decided to make the final push to roll that service out across the fleet, I could
monitor workflows across hundreds of customers at the same time. Every night, agents would go through the workflow
history, look for issues and write reports. They would have those reports ready for me every morning. That made it much
easier to make a release, aggressively track what was happening with the service and build confidence quickly.

This was the same service whose rollout had almost burnt me out. By then, I could follow what was happening across the
fleet and still make progress on other projects. The agents were capable enough to take on more of the work, and I could
look at a broader set of problems.

I had spent years protecting my deep work slots because context switching made it so hard to get anything done. Now I
had five or six things going on at once and, somehow, I was enjoying it. I could look at different kinds of problems and
actually make progress on them in the same day. That felt good, especially after spending so long trying to get that one
service stable.
