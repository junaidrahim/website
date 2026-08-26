---
kind: technical
status: cancelled
title: Redset Dataset for Big Data is Dead
created: 2026-05-10
updated: 2026-08-06
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/redset-dataset-for-big-data-is-dead.md
---

# Redset Dataset for Big Data is Dead

https://x.com/junaidrahxm/status/1824485974149411035

Talk about the whole big data is dead going over the dataset Francene talked about in DuckCon which proves the whole point about big data not being that big and actually can fit into simlper hosts

- Redshift Files - https://motherduck.com/blog/redshift-files-hunt-for-big-data/
- Download the redset dataset

- Histogram on
  - QUERY_SIZE
  - SCAN_SIZE

- Are there any other questions i would like to answer using this dataset ?
  - its a list of queries and their stats
  - Average number of tables read/write per query, histogram here.
  - Average number of joins, scans, aggregates ? all of this is probably mentioned in the paper

Motherduck already has a pretty good blog post about it, all I can do here is just regurgitate the same thing over and over again, maybe reading the paper might add some unique insight, but that won't.

- Paper: https://assets.amazon.science/24/3b/04b31ef64c83acf98fe3fdca9107/why-tpc-is-not-enough-an-analysis-of-the-amazon-redshift-fleet.pdf
- Dataset: https://github.com/amazon-science/redset

Maybe visualise this using evidence dev.
