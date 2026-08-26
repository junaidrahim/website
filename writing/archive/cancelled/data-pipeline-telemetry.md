---
kind: technical
status: cancelled
title: Data Pipeline Telemetry
created: 2026-05-10
updated: 2026-06-27
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/data-pipeline-telemetry.md
---

# Data Pipeline Telemetry

- What is a good holistic structure to do telemetry for data pipelines ?
- https://www.ibm.com/think/insights/a-data-observability-model-for-data-engineers

Row level telemetry for vectorized operations

```python
# vector pipeline
def pipeline(daft.DataFrame) -> daft.DataFrame:
	df.with_column("x", some_transform(df["y"]))

def process(records: List[Any], f: Callable) -> List[Any]:
	result = []
	for r in records:
		result.append(f(r))

	return result
```

It's so wild that when I was reading and processing JSON files by the line vs thinking in daft dataframes -- the need for observability is so different.

Now I want to think of the observability as a side-effect state update of the vector operation, instead of doing it.

Data quality metrics.

I have some deep research items on this, will get back once the backlog is almost clear.
