---
title: "[Rejected] Building ETL Workflows with Temporal - Temporal Replay 2025"
date: "2024-12-19"
summary: "Building Durable and Testable ETL Workflows with Temporal"
description: "Building Durable and Testable ETL Workflows with Temporal"
toc: true
readTime: true
autonumber: false
math: true
draft: false
---

> NOTE: This talk was rejected for Temporal Replay 2025.

- Submitted CFP Link: https://www.papercall.io/speakers/nishchith/speaker_talks/285120-building-durable-and-testable-etl-workflows-with-temporal

## Overview

Developing ETL workflows is a minefield of challenges, from schema drifts to performance bottlenecks. In this talk, we explore how Temporal's durable execution primitives enable developers to solve the challenges of building reliable and testable ETL pipelines.

## Abstract

Building reliable ETL pipelines is a challenge in modern data systems. While the premise seems straightforward — extract, transform, and load data — the reality is far more complex. Data engineers frequently grapple with schema changes that break pipelines, performance bottlenecks caused by massive data volumes, and upstream data sources that fail in subtle ways.

Traditional solutions for ETL require duplicated work to add sophisticated retry mechanisms and durability primitives. This leads to fragile systems that are expensive to maintain and difficult to evolve. Temporal proves to be an excellent choice for building ETL pipelines by addressing these challenges directly.

## What You'll Learn

In this talk, we explore how Temporal's durable execution framework provides elegant solutions to ETL-specific challenges. We dive deep into how features like activity heartbeats and child workflows help perform data processing reliably.

### Key Topics Covered

**Schema Drifts and Data Quality**  
Using Temporal's signal and query handlers to manage and communicate evolving schemas in workflows.

**Mature Concurrency to Prevent Abuse**  
Using Temporal's worker concurrency configurations to optimize resource utilization and prevent abuse.

**Error Handling and Retries**  
Temporal's retry policies configured for different failure scenarios, plus heartbeat mechanisms to ensure long-running workflows stay healthy and detect stuck or failed processes in real-time.

**Observability Challenges**  
Leveraging Temporal's out-of-the-box OpenTelemetry (OTEL) support to observe workflows and build alerting flows.

**Unit and E2E Testing**  
Temporal's testing frameworks support multiple levels of validation, from unit testing individual workflow components to E2E testing complete workflows in CI/CD pipelines.

**Security and PII Data**  
Using Temporal's secret management and encryption capabilities to handle sensitive data like credentials and PII securely.

**Maintenance and Evolution**  
Temporal's polyglot SDK support and code-first approach make it easier to version pipeline logic while providing a mature developer experience.

## Live Demo

The talk includes a live demonstration covering:

**Running an ETL Workflow**

- Data fetching and processing
- Simulating failure scenarios and recovery using Temporal's durable state management

**Testing Workflow**

- Setting up unit tests for activities using the Temporal SDK
- End-to-end testing on GitHub Actions using Temporal CLI

We conclude with a discussion on how Temporal's testing framework enables comprehensive validation, from unit tests to end-to-end scenarios, all integrated seamlessly with modern CI/CD practices.

## Who Should Attend

This talk is suitable for:

- Backend engineers working on data processing workflows
- Data engineers building ETL pipelines
- Engineering leaders evaluating orchestration solutions
- Teams looking to move beyond traditional fragile ETL solutions to robust data pipelines

**Ideal Experience Level**: Mid-level to senior backend engineers, especially those working with ETL workflows, data pipelines, or other durable task orchestration challenges. Engineers familiar with orchestration tools or workflow engines but new to Temporal will find immense value in this talk.

## Prerequisites

- Familiarity with databases
- Familiarity with GitHub Actions or any CI/CD systems

## Speakers

**Nishchith Shetty**  
Nishchith works with the Platform team at Atlan, building the next generation of the ETL platform. He was one of the early engineers at Atlan and helped implement and scale the federated query engine using Apache Calcite. Previously presented at ArgoCon North America.

**Junaid Rahim**  
Junaid is part of the team responsible for building pipelines that pull metadata from all major databases, data warehouses, and BI tools in the modern data stack. He has been an early engineer at Atlan where he helped implement and scale the ETL Platform. Previously presented at ArgoCon Europe and DuckCon North America.

---

_Atlan is a control plane for humans of data to discover, trust, and collaborate on data assets by bringing in metadata from various sources. Just like GitHub is for engineering teams and Figma is for design teams — Atlan is for data teams to collaborate._
