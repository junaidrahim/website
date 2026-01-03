---
title: "Roaring Bitmaps in Inverted Indexes"
date: "2025-11-16T18:30:46+05:30"
summary: "How roaring bitmaps are a very good way to optimise inverted indexes"
description: "How roaring bitmaps are a very good way to optimise inverted indexes"
toc: true
readTime: true
autonumber: false
math: true
draft: false
---


- https://vikramoberoi.com/posts/a-primer-on-roaring-bitmaps-what-they-are-and-how-they-work/
  - Two Papers
    - https://arxiv.org/pdf/1402.6407
    - https://arxiv.org/pdf/1603.06549

The whole point of this blog is to show that how roaring bitmaps are a very good way to optimise inverted indexes.

### Outline

- What's an inverted index.
- What are roaring bitmaps
  - Will need some research here.
- How roaring bitmaps make it cheaper to store inverted indexes -- both in memory and on disk.

## Understanding Roaring Bitmaps from First Principles

### The Problem: Storing Sets of Integers

Let's start with a simple problem: how do you efficiently store and query sets of integers?

Consider a search engine that needs to track which documents contain specific words:

- Word "database" appears in documents: {1, 5, 42, 100, 5000, 10000}
- Word "index" appears in documents: {2, 5, 99, 100, 4999, 10000}

### Traditional Approach: Simple Bitmaps

A bitmap uses one bit per possible value:

- Bit position = integer value
- Bit value: 1 if present, 0 if absent

```
Example: Set {1, 3, 5}
Position: 0 1 2 3 4 5 6 7
Bitmap:   0 1 0 1 0 1 0 0
```

#### The Problem with Simple Bitmaps

For large universes, bitmaps waste massive space:

- Universe of 1 billion integers = 1 billion bits = ~125MB
- Even if storing only 10 values!

```
Storing {1, 1000000000} in a bitmap:

Position 0: 0
Position 1: 1  <-- First value
Position 2-999999999: 0 (wasted space!)
Position 1000000000: 1  <-- Second value

Total: 125MB to store just 2 integers
```

### Enter: Roaring Bitmaps

Roaring bitmaps solve this by partitioning the universe and using different storage strategies based on density.

#### Core Insight: Partition by High Bits

Split 32-bit integers into:

- High 16 bits: Container key
- Low 16 bits: Value within container

```
Number: 131,075 (0x20003 in hex)
High 16 bits: 0x0002 (container 2)
Low 16 bits: 0x0003 (value 3 in container)
```

#### Three Container Types

Each container can store up to 65,536 values (2^16) using the most efficient format:

```
Container Decision Tree:

Number of elements in container?
├─ < 4,096 elements ──> Array Container
│                       (sorted array of 16-bit integers)
├─ ≥ 4,096 elements ──> Bitmap Container
│                       (65,536 bits = 8KB)
└─ All 65,536 values ─> Run Container
                        (for consecutive sequences)
```

### Visual Example

Let's store the set {1, 2, 3, 1000, 65536, 65537, 131072}:

```
Step 1: Partition by high 16 bits

Container 0 (0x0000): {1, 2, 3, 1000}     → Array Container
Container 1 (0x0001): {0, 1}              → Array Container
Container 2 (0x0002): {0}                 → Array Container

Step 2: Roaring Bitmap Structure

┌─────────────────────────────────────────┐
│          Roaring Bitmap Header          │
├─────────────────────────────────────────┤
│ Container Count: 3                      │
├─────────────────────────────────────────┤
│ Container Keys: [0, 1, 2]              │
├─────────────────────────────────────────┤
│ Container Types & Pointers              │
└─────────────────────────────────────────┘
           │         │         │
           ▼         ▼         ▼
    ┌──────────┐ ┌──────┐ ┌──────┐
    │Array: 4  │ │Array:│ │Array:│
    │[1,2,3,   │ │ [0,1]│ │ [0]  │
    │ 1000]    │ └──────┘ └──────┘
    └──────────┘
```

### Operations Efficiency

#### Union (OR)

Merge containers with same key, copy others:

```
A = {1, 1000, 65536}
B = {2, 1000, 131072}

Container view:
A: Container 0: [1, 1000], Container 1: [0]
B: Container 0: [2, 1000], Container 2: [0]

Union process:
Container 0: [1, 1000] ∪ [2, 1000] = [1, 2, 1000]
Container 1: [0] (from A only)
Container 2: [0] (from B only)

Result: {1, 2, 1000, 65536, 131072}
```

#### Intersection (AND)

Only process containers that exist in both:

```
Intersection process:
Container 0: [1, 1000] ∩ [2, 1000] = [1000]
Container 1: No match in B, skip
Container 2: No match in A, skip

Result: {1000}
```

### Memory Savings Example

Storing web crawler results for 10 million URLs:

- Average 1000 URLs contain each word
- Traditional bitmap: 10M bits = 1.25MB per word
- Roaring bitmap: ~2KB per word (500x smaller!)

```
Traditional Bitmap (word "database"):
[0|0|1|0|0|0|0|1|0|0|0|0|0|0|1|...] × 10 million = 1.25MB

Roaring Bitmap:
Container 0: Array[15, 97, ...]  (8 bytes)
Container 5: Array[200, 847, ...] (12 bytes)
...
Total: ~2KB
```

### Implementation Sketch

```python
class RoaringBitmap:
    def __init__(self):
        self.containers = {}  # key -> container

    def add(self, value):
        high = value >> 16
        low = value & 0xFFFF

        if high not in self.containers:
            self.containers[high] = ArrayContainer()

        container = self.containers[high]
        container.add(low)

        # Convert to bitmap if too many elements
        if container.cardinality() > 4096:
            self.containers[high] = container.to_bitmap()
```

### Why "Roaring"?

The name comes from RoaringBitmap's ability to efficiently "roar" through large datasets - it's optimized for:

- Fast sequential access
- Cache-friendly operations
- SIMD instruction support
- Excellent compression ratios

### Key Advantages

- **Space efficient**: Adapts storage to data density
- **Fast operations**: Leverages CPU cache and SIMD
- **Serialization friendly**: Compact on-disk format
- **Industry proven**: Used by Apache Lucene, Druid, Spark

The combination of partitioning and adaptive containers makes roaring bitmaps ideal for:

- Search engine inverted indexes
- Database bitmap indexes
- Analytics engines
- Time-series databases

---

I was implementing a domain specific inverted index at work and discovered roaring bitmaps as a very optimised way to store document IDs in the index.

Wanted to write this post talking about roaring bitmaps and how they optimise on-disk storage for bitmaps.

Let me illustrate the problem I was trying to solve.

- "apple" -> 1,4,10
- "banana" -> 1,10,16

documents with "apple banana" = set intersection

Map where keys are tokens and the values are sets,

One cheaper way to represent a set is to use a bitmap where a bit being set indicates that presence of that index id.

But sparse bitmaps with large ranges can quickly become inefficient from a storage pov.

that's where roaring bitmaps come in, where instead of storing bitmaps in a flat array of bits, we partition the space into different containers and then use different compression techniques to compress those containers

- Partitioning
  - Array Container
  - BitMap Container
  - Run Container (uses run length encoding for compression)
  - Some notes in the paper indicate how they use specific x86 instructions to count the number of bits set to 1
- File Layout
- Talk about how the set operations are optimised
