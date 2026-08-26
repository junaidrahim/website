---
kind: technical
status: cancelled
title: Data Correctness
created: 2026-05-10
updated: 2026-06-19
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/data-correctness.md
---

# Data Correctness

This can be a good blog post.

Notes around the idea of correct metadata, or data correctness in general, qualitative initiatives in making sure that data generated is correct.

This also spills over to the whole data quality domain.

- What is the scope of correctness ?
  - Assuming a single record is under observation
    - It goes through the following cycle
    - Unserialised -> Serialised -> Verified
      - Both these steps need verification.
  - Shape should be right
    - Can all data be key-value data ?
      - If yes, then all data can be represented as tables.
        - DataFrame API
      - If yes then all the keys should be present with acceptable values
        - Acceptable values are defined in some spec/schema
      - Anything can be framed as key-value data in a logical representation, physical representation is usually more aligned to the storage architecture.
      - And when arguing about correctness, we mostly talk in logical representations.
  - Values should be right
    - Scalar correctness -- values should be correct in isolation
    - Relational correctness -- values should be correct in relation to some other values

### How wild can schemas be ?

- Is there a way to define schemas that can outline correctness parameters, both scalar and relational correctness, in the schema itself ?
  - SQL DDL is pretty solid in this case

### Relational Algebra and Relational Calculus

- A full math subdomain about how data is supposed to be modelled and dealt with
- The tldr of Codd's work was to build systems where you can specify what data you want without specifying how to get it.
- This decoupled query execution from query definition. Let the engineers worry and argue about query execution. The data consumer should just be worried about what data they want.
- Codd's book about relational model and algebra would be interesting

---

2026-06-19

Cancelled. This is just data quality, a very well understood topic in the industry, and does not need to become a standalone blog post.
