---
title: "Atlan's Backend Internship Experience"
date: "2022-06-06"
summary: "I wanted to do a follow up article discussing backend engineering intern role at Atlan – how the internship went, what I learnt, and what can you expect from interning at here."
description: "I wanted to do a follow up article discussing backend engineering intern role at Atlan – how the internship went, what I learnt, and what can you expect from interning at here."
toc: true
readTime: true
autonumber: false
math: true
draft: false
---

A few weeks ago, I wrote about my [interview experience for the backend engineering intern role at Atlan](/posts/atlan_backend_internship_interview). I wanted to do a follow up article discussing the real thing – how the internship went, what I learnt, and what can you expect from interning here.

I started my internship on 8th June 2021. I had just finished my 2nd year of engineering.

It’s been a year since my first day at Atlan, one year is a long time to reflect over, if I listed down every single thing floating in my head about the past year, you would close the tab out of boredom, so I’ll summarise it in terms of **work**, **people and culture**, **lessons learnt** and **looking forward**.

## Work

Donut is our onboarding bot, it guides you through your first week. This is what my first day looked like at Atlan.

![](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9092cbd-79f7-4efd-96db-1af84feea9d0_1466x814.png)


### What is Atlan ?

[Atlan](https://atlan.com/) is a collaborative workspace for Data teams. Engineering teams have Github, Sales teams have Hubspot, Design teams have Figma, but there’s no home for data teams. A place where they can collaborate and get work done.

In simple words, Atlan connects to various databases and BI tools in your data stack and pulls in all the metadata, on top of that metadata we offer a ton of collaborative features that help you with data discovery, lineage, data quality, documentation etc. You can read more about it [here](https://prukalpa.medium.com/) and [here](https://atlan.com/about/).

### What did I work on ?

After joining, I was a part of the platform team, this is the team responsible for building the services that make up the Atlan platform. This platform powers the product and the integrations that help users connect to various metadata sources on Atlan. I started my internship with the platform orchestration team, this is the team responsible for two broad things –

- building out the ecosystem of integrations on Atlan
- developing and documenting the tools to build these integrations

My contributions at work has revolved around these two themes, building SQL and BI integrations and working on all the necessary tooling to make it easier to build integrations. This involved mostly working with Argo Workflows, Kubernetes, Apache Atlas, Python, JS, Kotlin and SQL. And YAML, lots of argo workflow YAML.

I had joined when we were half way there building the next iteration of the product, I witnessed the rollout of my integrations on customer production instances and got a chance to learn from all the bugs and customer issues that came up next.

This is one of the reasons why I wanted my internship to be at least 6 months, building something, witnessing all the edge cases in prod and then fixing them while communicating correctly what went wrong was something I really wanted to go through.

## People and Culture

{{< x user="swamusing" id="1527638653878476800" >}}

I always keep coming back to this wonderful tweet by my colleague for the people vibe. Working at Atlan has been pretty amazing – remote first, flexible hours, weekends are respected, high trust and ownership, all meetings are open by default.

I was never treated like an “intern” as such, I was treated and trusted just like a full-time employee from day 1. This trust on me since day 1 was a huge boost to my motivation to show up daily and try my best, even when things got hard.

Internships here have a good mix of mentorship and ownership. You will be trusted with delivering important things but there are people to help you out and guide you if you get stuck. And you get the freedom to come up with bold ideas and run with them.

The quarterly meet-ups with the team were pretty fun too. We usually fly out to a new city for a week or two and work together out of a WeWork.

{{< x user="junaidrahxm" id="1507296041166848000" >}}

Also another sweet perk of interning here 🥹

{{< x user="junaidrahxm" id="1435267762796969985" >}}

Atlan put up a pic of everyone in the company on the NASDAQ building in Times Square as a token of appreciation.

## Lessons Learnt

I’ll do quick one-liners for all the small and big lessons I’ve learnt over my last one year here.

- Squash your commits.
- DAGs are amazing.
- Never run. Always debug.
- Review and Iterate.
- Over-communicate. No matter what.
- Writing is how you build clarity. Write more.
- Invest time in building good dev tooling. So worth it.
- Take Action. Ideas are not worth shit if not executed well.
- Don’t be afraid of that codebase. If code is magic then you are a magician too.
- Using indexed array operators `[]` is the easiest way to break prod. Use `.get` pls.
- Engineering is creative work. You will have sparks of creative genius every once in a while. DO NOT LET THEM GO. Grab a pen/keyboard. It’s worth it.
- Try to spend at least 4 hours a day in flow state. Mute everything. Slack can wait. This is what you do consistently to improve as an engineer.
- Metadata is a bitch, it will come back down that TCP socket in shapes you can’t even imagine. Use a try catch. Design good error handling.
- The upside to knowing multiple programming languages is immense. Especially when working at a polyglot company.
- Good tests are a lot harder to write than you think. It’s not just slapping a test per function and you’re good to go.
- Software is a team sport. All-stars don’t help much in the long run. It’s all about what you can move as a team.
- Listen to customers. Go on that call. Listen to that zoom recording. Your code isn’t worth shit if it does not solve someone’s problem.
- Communication is a lot less about what you say and a lot more about what the other side heard. TCP vs UDP.
- Slow down. Understand the problem. Do not make that hot-fix. It’ll just come back to haunt you later.
- You can’t do amazing work if you don’t take care of yourself. Workout, Sleep, Eat right.
- Spending some time daily to reflect and write is worth it.
- The difference between junior and senior is now all about mindset and impact they create. Go after that mindset.
- Don’t get emotionally attached to your code. It’s meant to die, it’s meant to evolve.
- Own your L’s. Own your shit. Startups are all about people who say they’ll get it done and then actually get it done. Be that guy.

## Looking Forward

Atlan is solving an interesting problem in the data industry and the past year has been one crazy year of growing in all aspects of being an engineer. I have a much deeper sense of the problems that interest me. I have a much deeper sense of the kind of work I want to do.

I’m driven by people who believe in good engineering. Who believe in good engineering design. Who think and draw and discuss before they touch their keyboard. Atlan is a wonderful place to start your career if you’re into that kind of engineering.

Super grateful to all my mentors - [Amit](https://www.linkedin.com/in/amitprabhu4/), [Mukund](https://www.linkedin.com/in/tripathimukund/), [Varun](https://twitter.com/bankavarun), [Anshul](https://twitter.com/unshulmehta), [Louis](https://twitter.com/louisnoww) just to name a few. Thank you so much for all the love and lessons.

I have my final year of college left. I started my journey as a full time engineer this month.

It’s still day 1.

{{< x user="junaidrahxm" id="1400065390949011462" >}}


