---
title: "Engineers need Superterminals"
date: "2026-10-19T18:58:16+05:30"
summary: "Engineers used to hate context switching, and now that's all engineering is."
description: "Engineers used to hate context switching, and now that's all engineering is."
toc: true
readTime: true
autonumber: false
math: true
draft: true
---

> All of this is downstream of believing in [this](https://x.com/thorstenball/status/2101305394190557466?s=20) world of software engineering.

I have been trying to come up with a unified theory of how engineering tools are about to change and what kind of tools I would like to use personally. 

I recently switched jobs and moved into a team where my role is more of research engineering, with that change, I find myself doing a lot of experiments and trying to evaluate and argue about research directions which eventually become features in a product/system.

I now have access to almost unlimited tokens at my disposal. With agents, the job has shifted, and we need tools to help support that.

I also join meetings, give presentations, discuss issues with my colleagues, talk to customers, look at transcripts of customer calls I was not a part of, attend architecture meetings, RFC discussions etc. All of this while trying to manage a fleet of agents that are sustainably pushing research and system implementations in an aligned direction.

## Obsession with Text Buffers

Software engineering tools evolved around the text editor, everything was done to make sure you could add code in a file. JetBrains, Vim, Sublime, Visual Studio, VS Code, Zed etc. 

Even the early versions of cursor were built around the text buffer of a file, so you could see the changes AI was making to your file. Thanks to claude code, for the first time we moved on to a workflow where most of the time you are not even reading the code. 

Well, we are all splitting our terminals to run claude code sessions in different worktrees. That’s probably the most primitive way most software engineers are working, they are looking at multiple chat windows where AI is doing work.

If you are a bit more sophisticated and you care about your tools, you probably have an ADE (agentic dev environment) something like superset, conductor, orca, herdr etc. And these interfaces are primarily designed around two primary actions, you need to create a worktree and then spawn an agent in it. We also have notifications so when an agent needs you, this tool gives you a notification, clicking on which will take you to the session, where you can inspect the chat and then proceed further. A lof of engineers run some version of this setup, which is a great place to start, and then you add a few MCPs to bring in context from different SaaS tools.

It’s an interesting time to observe the advances in these tools because they are all trying to solve for a major shift in our work pattern, of going from reading code to reading agent transcripts and outputs (and perhaps reviewing code at the end).

If you are yourself trying to multiplex, you need the agents to start and only go to them once they have finished a task, in betweek you need to context switch to something else.

I feel looking at an agent do work is a waste of time and an anti-pattern. If you are looking at the agent just do work, it mostly means you don’t have enough confidence in the work it’s doing or you don’t have enough guard rails that’d stop the agent from doing something harmful, something on the tunes of deleting a full dev k8s cluster just because it was trying to clean something up.

Right now most of my time goes into setting up these agents for success and then going back when the agents have finished to verify the proof they have produced to claim that the work is done, sprinkled with the ocassional code review to ensure quality. If you are just working on a single thing as an engineer, then this does not bother you that much. You write a bunch of prompts, get an agent to make a plan, sign off on the plan and let the agent cook for 30 min, in those 30 min you perhaps scroll X, reply on slack or do something like this, by the and, your agent has made some code changes and ran some tests, it dumped all the test results maybe in a local sqlite file or a JSON file for you to take a look. 

The agent pings you, says that it’s done, you look at the JSON file, maybe ask it to plot some charts or some HTML UI to viz that JSON file. You look at it from multiple angles, things make sense, you ask it to create a PR and then you send it to your team for approval (which is also a waste of time at this point but the world moves slowly).

This is really convenient to manage if you are just working on a single task at a time, if you are multiplexing, you have 7/8 agents going at the same time working across multiple initiatives. You quickly have this situation where your whole day is just jumping from worktree to worktree, looking at different reports and analyzing work. Testing things and then back to your central context place to write more to drive the next set of agents. 

These multiple initiatives that you are working on, some of them are perhaps product focused, some are research focused, some are just like throwaway exploration that an agent is doing so that you can use it to understand the further direction you want to take. It’s a good mix of all this. 

I know a lot of people live an extreme of this way of working by running 100s of agents with automated loops that spawn themselves and keep working endlessly. But a lot of times even the loops need some maintenance because the underlying problem has shifted, or maybe you have discovered a new source of data that needs to be used to influence the loop or something. So you are always in this mode of writing material to influence agents so they can do their work.

## Bloomberg Terminals

As something who is trying to get more and more done using AI as much as they can, I have found some interesting parallels between our engineering and the trading world. 

The bloomberg terminal is a tool used by all of the big banks and hedge funds to basically look at market data. It costs around \$30k USD per year, and it’s a darling tool for most professional traders who do trade for a living.

You have probably seen it in movies like the big short, the margin call, even alex wang has a [bloomie](https://x.com/alexandr_wang/status/2105052032126292279?s=20). 

There is a lot of commentary on whether the price is justified or not and things like that. There have also been a lot of pointless attempts to vibe code a free alternative to it but most people who try to do it completely miss the point of how much work goes behind making that black and yellow app work.

The real work that makes the bloomberg terminal useful is the mountain of work bloomberg does as a tech company to unify and serve all the data feeds that exist in the finance universe, this involves everything from news data, weather data, tickers for every single financial instrument on the planet and things like that.

I learned about the bloomberg terminal when I watched the big short in high school and had just made a zerodha account to trade in the indian markets. 

Now as a research engineer I appreciate it even more. You see, the bloomberg terminal is the best sort of inspiration we have for what kind of tools we should be building for the software engineers of the future.

- Before: information was scarce and local. Your edge was relationships, being physically on the floor, and hearing news first. The job was about voice, reading the tape and knowing the right dealer.
- Bloomberg era: information got standardized and spread out. The edge moved to analysis and to the network on the terminal. The terminal became a status symbol at roughly $25–30k a year per seat.
- Today: execution is largely automated. Human traders handle large, illiquid or complex trades, manage the algorithms, and still use Bloomberg chat for OTC negotiation. The edge now comes from data, models, latency and risk management.

Coming back to the bloomberg terminal, there is a few reasons I am deeply inspired by it because it enables this sort of lightning fast experience when it comes to analyzing a lot of information quickly to make decisions.

In the bloomberg terminal, you can hit a few keystrokes and be looking at the stock price of something like \$NVDA, hit a few more and you are looking at the bar chart of their quarterly earnings report, hit a few more and you are able to co-relate it with the stock prices of their suppliers.

When traders live in that world, why can’t we build tools that allow me to quickly spawn a new worktree + an agent in a few keystrokes, and then look at the 5xx error percentage of that service in staging and in prod in another few keystrokes, and then also look at customer tickets related to that error in a few more keystrokes, all without leaving my terminal, all of this brought to me in a consistent visual interface so I don’t have to look at a new kind of purple html file for every data ask I have around a task.

It’s basically data-driven decision making at the speed of keystrokes with a meta-harness that is able to unify data feeds and give information to you and your agents super fast.

This system can also work upstream from like a central context layer or coordination layer like linear or notion. 

In this scenario, where by eliminating the primary workload of opening a text buffer and writing code, module by module, we need a new set of primitives that support this new way of working which is a bit more integrated than just having a terminal split 16 ways, and then a slew of code editor windows that need to be opened and closed all the time along with a bunch of HTML or BI reports and sqlite files that are constantly created and re-created from scratch because all of your agents are doing everything on their own. 

You need a tool that fits all of this and something that also allows for some kind of self-extension by the way of plugins, and you can vibe code your own set of plugins that can help you basically process a lot of information at once.

Because, in my opinion, the bottleneck is not the code review anymore, it’s basically staying on top of all the work that your agents are doing. It’s easy to claim that “oh just re-engineer all of your work to look like a hill climbing task” but the reality is that not everything is that easy to turn into a verifiable domain, there will always be things that you will have to step in and apply judgement or review the judgement the agent is performing on your behalf.

And with more and more reps you can turn a larger percentage of your work that looks like pure hill-climbing.

- talk about what Michelle hashimoto is doing with superlogical and rex and how they are also heading into the same direction.



## Messy Middles

Building a fully autonomous dark software factory is a bit of a long shot because you still are not as involved, and fully automating it to run in the dark might not be the right way.

I feel more and more of our work would keep falling in this messy middle where you slowly turn initiatives into good, approved hill climbing loops and then let them run semi-supervised, I don’t see a lot of merit to completely keep a team out of the loop for a software factory. 

This vision is a lot more anti-(chat-as-the-only-agent-interface) than it is anti-(software-factory). And I am talking about professional software engineering work, I think everyone should try to hack a software factory for their personal projects where you can quickly churn out quick projects to maybe control your home lights or things like that. It’s a good personal project to do, so that you know why commiting to them at your work is a bad idea. 



## Closing

- Talk about how this sort of folds under the idea of structured prototyping, that maybe once all the dust has settled, we’d just be left with design engineers focusing more on the visual and emotional outcomes of our software products and research engineers who would be focusing more on the operational, data eng and functional outcomes. And both will just use ai heavily.



My motivating question with all these experiments is always to ponder, can I carry the work of an entire division by myself (and a lot of tokens) without compromising quality. Do I have that amount of technical depth, customer empathy and business acumen to understand the constraints and deliver the outcomes.

Because that's the level all of need to start operating to ensure we are valuable in this new world.



You need a manager for infinte minds. You need a superterminal.



## Superterminals

A superterminal has the following things

- Client / Daemon separation. 
- Ability to start multiple shells and organize them. It's better if it's hierarchical.
  - Herdr does workspaces
  - Ghostty does windows
- Ability to read files quickly. Markdown files preferrably

* A plugin eco-system that can be used to create custom views of things
* So at the end you have this system that you can 
* A meta-harness that is native to this and is able to view things happening in every shell session in the tool.
* The idea is, because you are able to run so many agent sessions at the same time, you need a way to quickly visualise all the information these agents are generating. So having an endlessly extensible plugin system that you can create these sort of blocks in is very valuable (because you can vibe code them on the fly)



Amdahl's law -- <https://x.com/arpit_bhayani/status/2113611314543407606?s=20>

There are two products in the market that come close to this

Tern and Rex (by superlogical)

---

Notes on trading systems history

| Date | Event | Source(s) | Notes |
|---|---|---|---|
| c.1680 / 1698 | Jonathan's Coffee House, Exchange Alley, London. In 1698 John Castaing publishes a price list "at Jonathan's Coffee House." | [S37] | LSEG dates its own founding to 1698. The c.1680 opening date appears only in secondary sources (Wikipedia), so treat it as *needs a source*. |
| 1773 | "New Jonathan's" / "The Stock Exchange" opens in Sweeting's Alley. | [S37] | |
| 17 May 1792 | Buttonwood Agreement: 24 brokers set commissions and agree to deal with each other. Trading carries on in coffeehouses. | [S38] | NYSE also dates its formal constitution to 8 Mar 1817. |
| 3 Apr 1848 | Chicago Board of Trade founded "as a cash market for grain". | [S44] | CFTC says forward contracts began "almost immediately". Futures came later (1859/1865/1877 are the candidate dates). |
| Apr 1850 | Paul Julius Reuter flies stock prices by carrier pigeon between Aachen and Brussels, the gap between the German and Franco-Belgian telegraph lines. | [S39] [S41] [S5] | The 1851 London office follows the Dover–Calais cable [S40]. The "April" date comes from a Reuters article this environment could not fetch (HTTP 401). The year 1850 is firm. |
| 15 Nov 1867 | Edward Calahan's stock ticker, built for the Gold and Stock Telegraph Co. | [S43] [S5] [S38] | NYSE: the ticker narrowed "the gap between Wall Street and Main Street". |
| 1871 | Edison's Universal Stock Printer adds a unison mechanism that keeps every ticker on a line in sync. | [S43] [S5] | The "~1869" part of the brief is **UNVERIFIED**. The Edison Papers give 1871 for the Universal. |
| 1878 | Telephones installed at the NYSE. | [S38] | |
| 1960 | Quotron, the first electronic desk quote system. NYSE replaces its human Quotation Department with an automated quotation system the same year. | [S5] [S38] [S46] | Nuance: Britannica says Quotron I *printed* quotes on demand [S46], while IEEE says "electronic screens" [S5]. To be safe, write "push-button desk quotes". |
| 1969 | Telerate founded (bond and commercial-paper prices on screens). By 1985 it fed 24,000 screens in 41 countries. | [S47] | Secondary, but contemporaneous press. |
| 1969 | Instinet: "The Instinet Communication System, the market's first ECN, goes live." | [S48] [S49] | "First ECN" is Instinet's own claim. The 10-K confirms "founded in 1969". |
| 8 Feb 1971 | NASDAQ launches as an automated **quotation** system. Trades were still agreed by phone. | [S50] [S51] [S52] | Not an exchange until Jan 2006 [S51]. The SEC says NASDAQ had "limited automated execution functionality until… SuperMontage in 2002" [S52]. |
| 1973 | Reuter Monitor Money Rates Service: FX rates on terminals, as fixed exchange rates are abandoned. | [S40] [S42] | TR's own page lists it under "1970s". The 1973 year comes from Britannica. |
| 1981–82 | Michael Bloomberg starts Innovative Market Systems (1981). Merrill Lynch invests $30M for 30% and takes the first 22 terminals in 1982. | [S5] | *Defer to the Bloomberg stream.* One secondary source puts IMS's formation in March 1982, so the founding date is contested. |
| 1980s | Reuters Monitor Dealing Service: FX dealers "conclude trades over video terminals, a world first." | [S40] | TR gives no exact year (commonly cited as 1981). |
| 1986 | London "Big Bang": "computerised trading replacing the old pit-style trading floor." | [S37] | |
| 1996–97 | SEC Order Handling Rules (adopted 1996) open NASDAQ to ECNs. Archipelago founded Dec 1996 and its ECN launches Jan 1997 "as one of the first four qualified ECNs". Island ECN (Datek spin-off) founded 1996. | [S52] [S53] | Island's founding year comes only from secondary sources (*needs a source*). Instinet bought Island in Sep 2002 [S49]. |
| 1996 / 1998 | Tradeweb founded in 1996. Its first electronic marketplace (multi-dealer RFQ for US Treasuries) goes live in 1998. | [S59] [S60] | |
| Apr 2000 | MarketAxess incorporated (electronic corporate-bond trading). | [S61] | |
| Sep 2000 – 9 Apr 2001 | US decimalization phased in, finishing by 9 Apr 2001. | [S54] | |
| 2001–02 | ArcaEx, "the first open all-electronic stock exchange in the United States", approved Oct 2001 and trading from Mar 2002. | [S53] | |
| 1 Jul 2002 | FINRA (then NASD) TRACE: reporting and public dissemination of corporate-bond trades begins. | [S58] | |
| Jun 2005 → Oct 2007 | Reg NMS adopted 9 Jun 2005. Rules 610/611 phased in from 16 Oct 2006, with full compliance by 8 Oct 2007. | [S52] [S56] | *Time-sensitive:* on 11 Jun 2026 the SEC **proposed rescinding Rule 611** (trade-through) and 610(e) [S57]. |
| 22 Mar 2006 → 6 Oct 2006 | SEC approves NYSE Hybrid Market. NYSE begins phasing in automated execution on 6 Oct 2006. | [S55] [S52] | The NYSE's own history page says Hybrid "launched" in 2005 [S38]. The SEC order date is better. |
| Jan 2005 → Oct 2009 | NYSE's share of volume in NYSE-listed stocks falls from 79.1% to 25.1%. Execution time for small orders falls from 10.1 s to 0.7 s. | [S52] | Strong single-chart evidence of electronification. |
| 2010 | SEC: HFT estimates "typically are 50% of total volume or higher". | [S52] [S62] | The most authoritative dated estimate found. I found no newer SEC or academic figure. *Time-sensitive.* |
| 6 May 2010 → 10 Jun 2010 | Flash Crash, followed by SEC approval of single-stock circuit breakers (pilot). | [S73] [S74] | |
| 3 Nov 2010 | SEC adopts Rule 15c3-5 (Market Access Rule): pre-trade risk controls are mandatory and "naked" access is banned. | [S62] | Compliance by 14 Jul / 30 Nov 2011 [S71]. |
| 31 May 2012 | SEC approves Limit Up–Limit Down and tighter market-wide circuit breakers (7/13/20%), implemented by 4 Feb 2013. | [S74] | |
| 27 Jun 2012 | First LIBOR settlement (Barclays, CFTC $200M). Traders sent requests to submitters by email and "through electronic 'chats' over an instant messaging system." | [S65] | Regulators do not name the platform. |
| 1 Aug 2012 | Knight Capital: a dormant "Power Peg" path is triggered on 1 of 8 servers. In ~45 min, 212 customer orders become millions of child orders and Knight loses >$460M. | [S71] [S72] | |
| 16 Oct 2013 | SEC's first enforcement action under Rule 15c3-5: Knight pays $12M. | [S72] [S71] | |
| Dec 2013 | JPMorgan, Deutsche Bank and others ban multi-dealer chat rooms. Bloomberg launches a Compliance Center for IB. | [S69] | Secondary source (Forbes contributor), consistent with FT/Reuters headlines seen in search. |
| Feb–Mar 2014 | NASDAQ adds an optional, free exchange "Kill Switch" (Rule 6130). | [S75] | CME Globex has a kill switch too [S76]. |
| 12 Nov 2014 | FX: FCA fines five banks £1.1bn, CFTC >$1.4bn, OCC $700M. FCA starts an industry-wide remediation programme. | [S66] | |
| 4 Feb 2015 → 2 Jul 2015 | CME closes most futures pits: open outcry was "just one percent" of futures volume. S&P 500 futures and most options pits stay open. | [S45] | |
| 20 May 2015 | DOJ: Citi, JPM, Barclays and RBS plead guilty over "The Cartel" chat room, with >$2.5bn in criminal fines. UBS pleads guilty over LIBOR. | [S67] [S68] | The three individual "Cartel" traders were **acquitted** in Oct 2018 [S77]. |
| 27 Sep 2022 | SEC fines 16 firms >$1.1bn for off-channel (unrecorded) messaging. | [S70] | Regulators now push chat *onto* recorded platforms. |
| 2025 | US IG corporate bonds: just under 50% electronic. HY: 32%. | [S64] | *Time-sensitive*, industry estimate. |
| 2022 | FX: about 60% of trades electronic. "Voice" (which BIS defines to include messaging platforms) is the rest. | [S63] | 2025 Triennial not checked. |
