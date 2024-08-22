---
title: "Scalable Data Pipelines with DuckDB - DuckCon #5"
date: "2024-08-15"
toc: false
readTime: true
autonumber: false
math: false
draft: false
---

Presented in person at [DuckCon #5 in Seattle](https://duckdb.org/2024/08/15/duckcon5.html).

## Links

- **Slides**: https://pitch.com/v/a-quack-at-building-scalable-data-pipelines-with-duckdb-t2dhzd
- **Code**: https://github.com/junaidrahim/duckdb-with-argo-wf
- **Recording**: Not published yet.

## Submitted Proposal

The team at Atlan is building a collaborative workspace for modern data teams that offers functionality like metadata cataloguing, governance and lineage amongst others. Ingesting metadata from various sources and generating aggregate insights is one of the core functionalities of Atlan's platform.

A lot of atlan's product use-cases involves performing heavy analytical/aggregate processing in data pipelines to power features like table/column popularity from SQL queries, end-to-end data lineage, reporting/alerting on data movement etc.

In this talk Junaid will present how the engineering team at Atlan has leveraged DuckDB with Argo Workflows to design and run k8s native analytical data pipelines processing ~165 million metadata assets daily and generate popularity insights from ~200 million SQL queries a month.

In this proposed architecture, the data pipelines are written as argo workflows that are multi-node DAGs with each node creating a pod in the k8s cluster. It also has features to use a cloud object store like S3 or GCS as an artifact repository to which all the steps can write their output files and the following steps can pick them up as inputs.

Each of these pods run a container which initialises a local DuckDB database, loads the relevant input data from S3 as tables and then runs the SQL queries to process the data. The results are stored as parquet files on S3 to be picked up by the next step in the DAG.

This architecture enables us to run very lean and memory efficient data pipelines and breaking up the pipeline with it's outputs into different steps helps performing fan-out or fan-in patterns dynamically if necessary with chunked parquet files.

Post-run analysis and debugging also becomes easy as developers can just run SQL notebooks against the cloud object store from their laptops directly leveraging the excellent parquet and object store support present in DuckDB.

We have used DuckDB to decrease the runtime of our pipelines by ~50% replacing our older architecture that used in-memory apache spark. We propose this talk to present this solution to the DuckDB and the data engineering community so more teams are encouraged to leverage DuckDB in their analytical data pipelines.


