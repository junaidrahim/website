---
title: "Search Is Set Intersection"
date: "2025-11-16T18:30:46+05:30"
summary: "I was building an inverted index at work and fell into the roaring bitmaps rabbit hole. Notes on how they make posting lists hundreds of times smaller, in memory and on disk."
description: "I was building an inverted index at work and fell into the roaring bitmaps rabbit hole. Notes on how they make posting lists hundreds of times smaller, in memory and on disk."
toc: true
readTime: true
autonumber: false
math: true
draft: false
---

I was implementing a domain-specific inverted index at work a few months back. The tokenisation was boring, the ranking was boring, the interesting problem was storing the values -- millions of sets of document IDs that had to live in memory and on disk cheaply.

An inverted index is just a map. Keys are tokens, values are the sets of IDs of the documents that contain them.

```text
"apple"  -> {1, 4, 10}
"banana" -> {1, 10, 16}
```

Query for documents containing "apple banana" and the answer is the intersection of the two sets, {1, 10}. OR compiles to a union, NOT to a difference. Every boolean query over an inverted index is set algebra over integers.

Which collapses the whole design into one question: how do you store a set of integers so that it's small on disk and fast to intersect ?

That question sent me down a rabbit hole that ended at roaring bitmaps. Most of what follows I learnt from Vikram Oberoi's excellent primer[^1] and the two papers behind the format[^2].

## Arrays and Bitmaps

There are two obvious ways to store a set of integers.

The first is a sorted array. {1, 4, 10} becomes [1, 4, 10], four bytes per ID as 32-bit integers. Small when the set is small, and intersecting two sorted arrays is a linear merge.

The second is a bitmap. Allocate one bit per possible document ID, set the bit if the document is present.

```text
set {1, 3, 5}

position: 0 1 2 3 4 5 6 7
bitmap:   0 1 0 1 0 1 0 0
```

Bitmaps are lovely for operations. Intersection is a bitwise AND, and the CPU does that 64 bits at a time in a single instruction -- 64 membership checks at once. This is the bit-level parallelism that made bitmap indexes popular in databases in the first place.

But bitmap storage scales with the universe, not with the set. Say the index holds 10 million documents and a word appears in 1000 of them. The plain bitmap is 10 million bits, 1.25 MB, for one word. The sorted array is 4 KB.

And the degenerate case is grim --

```text
storing {1, 1000000000} as a plain bitmap

position 1:               1
positions 2..999999999:   0   <- ~125 MB of zeroes
position 1000000000:      1
```

Two integers. 125 MB.

You'd think sorted arrays just win then. They don't. Flip the density -- a term appearing in half of those 10 million documents costs 20 MB as an array and still 1.25 MB as a bitmap, and the bitmap intersects massively faster.

Sparse data wants arrays. Dense data wants bitmaps. A real inverted index is both, in different places.

## Roaring Bitmaps

The core move of roaring bitmaps: don't pick one representation for the whole set, pick one per chunk. (The papers never bother to explain the name, by the way. I checked.)

Partition the 32-bit integer space into chunks of 2^16 values sharing the same high 16 bits. Every chunk that actually contains values gets a container, and the containers live in an array sorted by those high bits -- the first-level index. Locating an integer means splitting it in half:

```text
N = 131075  (hex 0x0002_0003)

high 16 bits: 0x0002 -> container key 2
low 16 bits:  0x0003 -> value 3, inside container 2
```

Inside a container you only store 16-bit values, the key already carries the upper half. And each container independently picks whichever of three representations is cheapest for its density.

**Array container.** A sorted array of 16-bit integers, used while the chunk holds at most 4096 values. Two bytes per value.

**Bitmap container.** A plain 2^16-bit bitmap, 8 KB flat, used once the chunk crosses 4096 values.

**Run container.** Added in the follow-up paper. Stores runs of consecutive integers as (start, length) pairs, 2 + 4r bytes for r runs. Classic run-length encoding, built for data like "documents 100000 through 105000 all match".

Why 4096 ? Because 4096 × 2 bytes = 8192 bytes -- exactly the size of one bitmap container. That's the precise crossover where the sorted array stops being cheaper, and it hands the structure a clean invariant: no container ever spends more than ~16 bits per integer it stores.

The threshold isn't tuned, it's derived.

Array and bitmap containers convert into each other automatically as values come and go. Run containers don't -- you call `runOptimize()` explicitly, usually right before serializing, and each container keeps the run encoding only if it beats both alternatives.

This is what storing {1, 2, 3, 1000, 65536, 65537, 131072} looks like --

```text
keys:       0x0000            0x0001     0x0002
            |                 |          |
containers: array             array      array
            [1, 2, 3, 1000]   [0, 1]     [0]
```

Seven integers, 14 bytes of container payload. The degenerate {1, 1000000000} set becomes two one-element array containers, a few dozen bytes instead of 125 MB. And that 10-million-document posting list with 1000 matches lands around 2 KB instead of 1.25 MB -- roughly 600x smaller.

Older compressed bitmaps (WAH, Concise, EWAH) got decent compression by running RLE over the entire bitmap, but that kills random access -- checking whether one integer is in the set means decompressing from the start. Roaring stays randomly accessible: binary search the keys, then look inside a single container.

## Set Operations

Back to "apple banana". Intersecting two roaring bitmaps starts at the key level, walk both sorted key arrays, and only when a key exists on both sides do you touch the containers underneath. Chunks present on one side contribute nothing to an intersection, so they're skipped without reading a single value.

If your two posting lists live in disjoint ranges of the ID space, the intersection is over before it starts.

When keys match, it's container versus container, and every pairing has its own routine.

Two arrays intersect like the merge step of merge sort. Unless one is over 64 times smaller than the other, then it gallops -- take the next value from the small array, seek into the big one with doubling steps, finish with a binary search.

An array against a bitmap probes each array value against the bitmap, one bit test per candidate. The result can't be bigger than the array you started with, so it's always an array.

Two bitmaps intersect as 1024 word-wise ANDs, and the result's cardinality decides the output type -- above 4096 it stays a bitmap, otherwise the set bits get extracted into an array container.

That last case hides a pretty neat detail. How does the result know its own cardinality without a second pass ?

The papers lean on hardware. x86 ships `popcnt`, an instruction that counts the set bits in a 64-bit word at a throughput of roughly one per cycle, so the AND loop accumulates the count as it goes, essentially for free. The 2014 paper calls these bit-count instructions "a key ingredient" in roaring's performance. Explicit SIMD vectorisation came later, in the 2018 CRoaring paper, the original numbers came from popcnt-class tricks alone.

Unions are the same machinery with the polarity flipped. Bitmap OR bitmap stays a bitmap since cardinality only grows, array OR array merges unless the result would cross 4096 and upgrade itself.

## On Disk

An index that only lives in memory is half an index.

The serialized format is a published spec[^3], little-endian and language-independent -- a bitmap written by the Java library can be read by CRoaring, the Go port, the Rust port, even a Postgres extension. The layout looks like the following

```text
+---------------------------------------------+
| cookie  (12346 = no runs, 12347 = has runs) |
+---------------------------------------------+
| descriptive header                          |
|   per container: 16-bit key                 |
|                  16-bit cardinality - 1     |
+---------------------------------------------+
| offset header                               |
|   32-bit byte position of each container    |
+---------------------------------------------+
| container payloads                          |
|   2-byte arrays | 8 KB bitmaps | run pairs  |
+---------------------------------------------+
```

(Cardinality minus one, because 65536 doesn't fit in 16 bits.)

The offset header is the part that matters for an index. You can memory-map the file and jump straight to one container without deserializing anything around it -- the spec is explicitly designed for random access without materializing the bitmap in memory. The Java library ships `ImmutableRoaringBitmap` for exactly this, queries run directly against mmap'd bytes. Posting lists stay on disk, the OS page cache does the caching, and a query only ever touches the containers it intersects.

You can tell this thing was designed by people who ship. Roaring bitmaps sit inside Apache Lucene (and therefore Solr and Elasticsearch)[^4], Druid, Spark, Hive, ClickHouse, Pinot, Netflix Atlas, InfluxDB, and Google's Procella -- the SQL engine behind YouTube. A SIGMOD 2017 study that benchmarked bitmap compression schemes ended on the least ambiguous sentence I've read in a paper: "Use Roaring for bitmap compression whenever possible. Do not use other bitmap compression methods."

## In Conclusion

I went in looking for a clever compression algorithm and came out with something better -- a data structure that refuses to commit.

There is no single best way to store a set of integers. Density decides, and density changes every 65,536 values. Roaring splits the space, looks at each chunk, and lets the data pick its own encoding, then re-picks after every operation.

**Partition, then decide.**

My index at work is a lot smaller and dumber than Lucene. Roaring still cut its footprint by orders of magnitude, because the trick doesn't care about scale, it cares about shape.

Search is set intersection. The rest is picking your containers well.

[^1]: Vikram Oberoi, [A primer on Roaring bitmaps](https://vikramoberoi.com/posts/a-primer-on-roaring-bitmaps-what-they-are-and-how-they-work/) -- genuinely one of the better explainers I've read, this post is my compressed trail through it.

[^2]: Chambi, Lemire, Kaser, Godin, [Better bitmap performance with Roaring bitmaps](https://arxiv.org/abs/1402.6407) (2014), and Lemire, Ssi-Yan-Kai, Kaser, [Consistently faster and smaller compressed bitmaps with Roaring](https://arxiv.org/abs/1603.06549) (2016) -- the second one added run containers.

[^3]: The [RoaringFormatSpec](https://github.com/RoaringBitmap/RoaringFormatSpec) on GitHub.

[^4]: Honest caveat: Lucene does *not* use roaring for its on-disk posting lists -- those use Frame of Reference, blocks of 256 delta-encoded bit-packed doc IDs, built for the sequential iteration posting lists actually see. The roaring-style sets power the filter cache, where cached doc ID sets need fast random access and fast intersection. Same 4096-per-block threshold, one deviation: very dense blocks store the doc IDs that are *missing*, a negated array container. See [Frame of Reference and Roaring Bitmaps](https://www.elastic.co/blog/frame-of-reference-and-roaring-bitmaps) on the Elastic blog.
