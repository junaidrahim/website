---
title: "The Prophecy of the Answering Machine"
date: "2026-08-11T00:00:00+05:30"
summary: "A short history of the recurring computer-science dream: a machine that can answer every question."
description: "A short history of the recurring computer-science dream: a machine that can answer every question."
toc: true
readTime: true
autonumber: false
math: false
draft: false
---

> This post is a **work in progress**.

I love conversational analytics, it kinda feels magical when you ask a talk-to-data agent questions and it's able to
compose a SQL query or search documents to precisely answer your question.

All computer scientists have had a fantasy, and that is to build a machine that can answer every question in the
universe. We've had multiple narrow solutions like search engines, Wikipedia, Siri etc.
(`todo: come up with more examples here`) for this but the most significant leap came with LLMs and AI in general.

In my head, this fantasy to build this machine stems from our primal instinct to look up at the sky and ponder, and to
ask questions.

The definition of AGI keeps changing, but answering questions is a subset of the current accepted definition of "being
able to do all economically viable work".

Funnily enough, if you study the history of data systems, you'll always find traces of efforts to build this answering
machine.

| Year              | Milestone                                  | Research strand                    | What it added to the answering machine                                                                                                                                                                                                                                               |
| ----------------- | ------------------------------------------ | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1958**          | Luhn’s “Business Intelligence System”[^1]  | Organizational information systems | Proposed an automated system that would ingest, retrieve, distribute, and furnish information on demand inside an organization.                                                                                                                                                      |
| **1961**          | BASEBALL[^2]                               | Natural-language database access   | Answered restricted ordinary-English questions over stored baseball records and explicitly imagined executives, commanders, and scientists questioning computers directly.                                                                                                           |
| **1966**          | ELIZA[^3]                                  | Conversational interface           | Demonstrated how strongly a textual dialogue could suggest intelligence, despite relying on scripted transformations rather than broad knowledge.                                                                                                                                    |
| **1970**          | Codd’s relational model[^4]                | Database architecture              | Separated logical querying from physical storage, allowing future users to work with data without understanding its internal machine representation.                                                                                                                                 |
| **1973**          | LUNAR[^5]                                  | Natural-language database access   | Let lunar geologists query Apollo sample data in ordinary English, supported by a carefully bounded vocabulary and domain model.                                                                                                                                                     |
| **1974**          | Relational support for non-programmers[^6] | Database accessibility             | Made the “casual user” an explicit database-design objective and proposed formal or informal language interfaces over relational data.                                                                                                                                               |
| **1982**          | Chat-80[^7]                                | Natural-language database access   | Established a strikingly modern pipeline: English question → logical representation → query planning → execution → answer.                                                                                                                                                           |
| **1999**          | TREC-8 Question Answering track[^8]        | Open-domain question answering     | Shifted the retrieval objective from returning ranked documents to returning actual answers over a large document collection.                                                                                                                                                        |
| **2003**          | Neural probabilistic language model[^9]    | Neural language modeling           | Learned distributed word representations and sequence probabilities together, laying groundwork for models that acquire linguistic regularities rather than relying only on handcrafted rules.                                                                                       |
| **2010–11**       | IBM Watson and DeepQA[^10]                 | Open-domain question answering     | Combined question analysis, retrieval, candidate generation, evidence scoring, and ranking at sufficient breadth and speed to defeat leading _Jeopardy!_ champions.                                                                                                                  |
| **2013**          | Power BI Q&A[^11]                          | Natural-language BI                | Brought natural-language questions to business data while documenting its dependence on a curated data model, synonyms, data quality, and ambiguity handling.                                                                                                                        |
| **2017**          | The Transformer[^12]                       | Neural architecture                | Replaced recurrence with attention in a highly parallelizable architecture, enabling the training scale behind modern large language models.                                                                                                                                         |
| **2018-2020**     | GPT-1[^13], GPT-2[^14], GPT-3[^15]         | Generative pretraining             | Showed that one Transformer language model pretrained on unlabeled text could transfer to many language-understanding tasks with relatively small task-specific adaptations.                                                                                                         |
| **November 2022** | ChatGPT[^16]                               | Product convergence                | Combined broad pretrained knowledge, instruction following, RLHF, dialogue-specific training, conversational state, and an accessible interface. It fulfilled the interface prophecy, while its plausible false answers revealed that the source-of-truth problem remained unsolved. |

The earlier systems were narrow because their semantics were explicit: they depended on schemas, vocabularies, logical
forms, join graphs, and curated data models. Large language models became broad by making much of that knowledge
implicit in model weights.

[^1]:
    Hans Peter Luhn, “A Business Intelligence System,” _IBM Journal of Research and Development_ 2, no. 4 (1958):
    314–319. [IBM PDF](https://www.ibm.com/watson/assets/pdfs/ibmrd0204H.pdf).

[^2]:
    Bert F. Green Jr., Alice K. Wolf, Carol Chomsky, and Kenneth Laughery, “BASEBALL: An Automatic Question-Answerer,”
    _Western Joint Computer Conference_ (1961): 219–224.
    [Paper](https://web.stanford.edu/class/linguist289/p219-green.pdf).

[^3]:
    Joseph Weizenbaum, “ELIZA—A Computer Program for the Study of Natural Language Communication Between Man and
    Machine,” _Communications of the ACM_ 9, no. 1 (1966): 36–45. [DOI](https://doi.org/10.1145/365153.365168).

[^4]:
    E. F. Codd, “A Relational Model of Data for Large Shared Data Banks,” _Communications of the ACM_ 13, no. 6 (1970):
    377–387.
    [IBM Research](https://research.ibm.com/publications/a-relational-model-of-data-for-large-shared-data-banks).

[^5]:
    William A. Woods, “Progress in Natural Language Understanding: An Application to Lunar Geology,” _AFIPS National
    Computer Conference_ 42 (1973): 441–450. [DOI](https://doi.org/10.1145/1499586.1499695).

[^6]:
    E. F. Codd and C. J. Date, “Interactive Support for Non-Programmers: The Relational and Network Approaches,”
    _SIGFIDET_ (1974).
    [IBM Research](https://research.ibm.com/publications/interactive-support-for-non-programmers-the-relational-and-network-approaches).

[^7]:
    David H. D. Warren and Fernando C. N. Pereira, “An Efficient Easily Adaptable System for Interpreting Natural
    Language Queries,” _American Journal of Computational Linguistics_ 8, nos. 3–4 (1982): 110–122.
    [ACL Anthology](https://aclanthology.org/J82-3002/).

[^8]:
    Ellen M. Voorhees and Dawn M. Tice, “The TREC-8 Question Answering Track Evaluation,” _Eighth Text REtrieval
    Conference_ (1999): 83–105. [NIST proceedings](https://trec.nist.gov/pubs/trec8/t8_proceedings.html).

[^9]:
    Yoshua Bengio, Réjean Ducharme, Pascal Vincent, and Christian Jauvin, “A Neural Probabilistic Language Model,”
    _Journal of Machine Learning Research_ 3 (2003): 1137–1155. [JMLR](https://www.jmlr.org/papers/v3/bengio03a.html).

[^10]:
    David Ferrucci et al., “Building Watson: An Overview of the DeepQA Project,” _AI Magazine_ 31, no. 3 (2010): 59–79.
    [IBM Research](https://research.ibm.com/publications/building-watson-an-overview-of-the-deepqa-project); see also
    IBM’s [history of the 2011 _Jeopardy!_ result](https://www.ibm.com/history/watson-jeopardy).

[^11]:
    Microsoft Power BI Team, “Live Now! Q&A with Your Data,” December 18, 2013.
    [Power BI Blog](https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Live-Now-Q-A-with-your-Data/ba-p/5174356).

[^12]:
    Ashish Vaswani et al., “Attention Is All You Need,” _Advances in Neural Information Processing Systems_ 30 (2017).
    [NeurIPS](https://papers.nips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html).

[^13]:
    Alec Radford, Karthik Narasimhan, Tim Salimans, and Ilya Sutskever, “Improving Language Understanding by Generative
    Pre-Training,” OpenAI, 2018.
    [Paper](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf).

[^14]:
    Alec Radford et al., “Language Models are Unsupervised Multitask Learners,” OpenAI, 2019.
    [Paper](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf).

[^15]:
    Tom B. Brown et al., “Language Models are Few-Shot Learners,” _Advances in Neural Information Processing Systems_ 33
    (2020). [OpenAI](https://openai.com/index/language-models-are-few-shot-learners/).

[^16]: OpenAI, “Introducing ChatGPT,” November 30, 2022. [OpenAI](https://openai.com/index/chatgpt/).
