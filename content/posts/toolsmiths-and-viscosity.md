---
title: "Toolsmiths and Viscosity in Software Teams"
date: "2024-10-02"
summary: "The toolsmithss tip the scales and reduce viscosity in software teams. Encourage them."
description: "The toolsmiths tip the scales and reduce viscosity in software teams. Encourage them."
toc: true
readTime: true
autonumber: false
math: true
draft: false
---

I've been thinking a lot about the relationship between **toolsmiths** and **viscosity** in teams that ship software. If you're reading this, you probably work in one of these teams, or better -- *manage one of these teams*.

## Viscosity

What do I mean by viscosity ? 

Viscosity in software teams refers to the resistance or difficulty in making changes to their systems. With time, even with planning and being mindful about tech debt, it's natural that the viscosity in your teams will go up.

If you're an individual contributor who prefers moving fast, it becomes really frustrating to see this viscosity grow to a point that it becomes harder to ship something than to build something. It becomes annoying to see all this friction get in the way. 

It is also ironic that if you make decisions that are too indexed on shipping fast, you get to a highly viscous state even faster. You accrue debt faster, you don't write docs. You introduce tightly coupled components, you prefer introducing a rigid manual process than investing time in automation. You don't worry about the developer experience of new services. Every engineer knows doing all this comes back to bite us, but we do it anyway to get things to prod.

> "Yeah let's just document a new process that requires the dev to make this config change in 6 places to make sure this works."

Reducing viscosity is not always straight-forward, but you do notice it going up, and then at some point, someone in the team gets frustrated and decides to build a tool.

## The Toolsmith

That's my favourite character, the **toolsmith**. 

Who is a toolsmith ? The traditional definition is someone who forges, dresses, hardens, and tempers tools. 

In a software team, these are the people who raise their hand for --

- Building automations
- Optimising CI pipelines
- Working on dev-ex and dev-env enhancements
- Writing tools for custom analyses
- Arguing about documentation and knowledge management
- Scaling testing infrastructure
- Improving telemetry and observability
- Evangelising tools for performance analysis 
- etc.

You can probably think of a few in your team who you would attribute to as *the toolsmiths*, people who have a burning passion for using and building the right set of tools to help the team ship faster.  

## A Rebellion (sometimes)

In some teams, mostly in startups, the whole "*let me write a tool for this*" is an act of rebellion. This being a rebellion comes a surprise to some folks who have always been at big tech companies, you probably have more tools at your disposal than you can keep track of, and can easily prioritise building some tooling to get your work done.  

But being skeptical here makes sense for startups, the priority is to ship features and get revenue, can't waste too much time building layers of internal tooling, it's pointless. Toolsmiths here can use a healthy dose of asking -- [but does it help you ship ?](https://thorstenball.com/blog/2020/08/25/but-does-it-help-you-ship/)

Different teams treat this act of rebellion by the toolsmith differently, some teams give them a lot of freedom to innovate. Most scale-up tech companies go through cycles of shipping, facing increased viscosity, unleashing toolsmiths to address it and then going back to shipping again. 

Amazon is a good example of this cycle, they built AWS to solve their own viscosity, just that the rebellion of the toolsmiths there lead by [Matt Round](https://www.cloudzero.com/blog/matt-round-interview/)  spawned a money printing engine for Amazon :)

I am deeply enamoured by companies like stripe, google and meta who make it a priority to make sure that their engineers have world class tools at their disposal to create what they want. Sometimes even smaller tech companies build and open-source some amazing tools -- for example [statsd](https://github.com/statsd/statsd) by Etsy. [Weather union](https://www.weatherunion.com/) by Zomato is also a good example.

## Encouragement

One of the effective ways to combat viscosity in your team is to encourage and allow your toolsmiths to innovate. 

Their focus on creating and improving tools can significantly impact your team's efficiency and ability to move faster. Preferring tooling over process works, especially if your team is growing. The easiest way to enforce a process is to invest in tooling.

By empowering your toolsmiths, you're investing in the long-term agility of your team. While it may seem like a short-term trade-off to entertain the rebellion, the reduced viscosity will pay dividends and you will have more satisfied developers in the long run.