---
kind: technical
status: archived
title: You Don't Know JSON
created: 2026-05-09
updated: 2026-05-09
migrated_from:
- /Users/junaidrahim/Obsidian/Everything/Notes/blogs/you-dont-know-json.md
source_status: idea
resolved_by: content/posts/you-dont-know-json.md
---

# You Don't Know JSON

JSON parsing is such a pain, have faced a lot of issues with python as well. Some articles that might help

- [https://bishopfox.com/blog/json-interoperability-vulnerabilities](https://bishopfox.com/blog/json-interoperability-vulnerabilities) (read pt 4 here)
- https://seriot.ch/projects/parsing_json.html
- http://james.newtonking.com/archive/2009/07/29/json-standard-business-card


---

## Draft: The JSON Spec Is Ambiguous (And That's Everyone's Problem)

**Status:** Draft v1
**Target Audience:** Backend/platform engineers, especially those working with multi-service architectures
**Estimated Length:** 1500-2000 words

---

### Hook

You've used JSON a thousand times. You've probably never read the spec. Neither have most library authors — and that's why no two parsers behave the same way.

---

### 1. The Myth of "Simple JSON"

JSON looks simple: objects, arrays, strings, numbers, booleans, null. Six characters of syntax. What could go wrong?

The problem: six different documents define it.
- RFC 4627 → RFC 7159 → RFC 8259 (IETF evolution)
- ECMA-404 (the "canonical" standard)
- ECMAScript (JavaScript's take)
- JSON5, HJSON (supersets with "helpful" extensions)

Nicolas Seriot tested dozens of parsers against a comprehensive test suite and found that no two libraries exhibit the same behaviour. Edge cases and maliciously crafted payloads cause bugs, crashes, and denial of services — mainly because JSON libraries rely on specifications that evolved over time and left many details loosely specified or not specified at all.

---

### 2. Where the Spec Is Silent (or Shrugs)

Four categories of deliberate ambiguity:

#### 2a. Duplicate Keys

RFC 8259 says keys "SHOULD" be unique — not "MUST". That single word choice creates a vulnerability class.

> "When the names within an object are not unique, the behavior of software that receives such an object is unpredictable. Many implementations report the last name/value pair only. Other implementations report an error or fail to parse the object, and some implementations report all of the name/value pairs, including duplicates."
> — RFC 8259

Three parsers, three outcomes:
- Parser A: first-key wins
- Parser B: last-key wins  
- Parser C: throws error

#### 2b. Number Representation

The spec explicitly punts on precision:

> "This specification allows implementations to set limits on the range and precision of numbers accepted."
> — RFC 8259

What's "safe"? Integers in the range `[-(2^53)+1, (2^53)-1]`. Anything outside is implementation-defined.

Worse: Python's `json.dump` will happily emit `NaN` and `Infinity` by default — values that aren't valid JSON at all. Set `allow_nan=False` or your "JSON" will break compliant parsers.

Numbers like `1E400` or `3.141592653589793238462643383279` indicate potential interoperability problems — the producing software expects more precision than most consumers provide.

#### 2c. String Encoding

String encoding was only explicitly required to be UTF-8 in the 2017 revision of the specification. Before that? Implementation-defined.

Handling of:
- Unpaired surrogates (`\uD800` without a low surrogate)
- NUL bytes in strings
- Escape sequence variations

...varies wildly across parsers.

#### 2d. Comments & Trailing Commas

Not in any JSON spec. But JSON5 and HJSON accept them. Some "lenient" parsers in strict-mode languages accept them too.

Attackers can craft payloads that exploit inconsistent support for comments:
```json
{"qty": 1, "extra": 1/*, "qty": -1, "extra2": 2*/}
```

Parser A (no comment support): syntax error
Parser B (comment support): `{"qty": 1, "extra": 1}`
Parser C (lenient): `{"qty": -1}` after stripping "comments"

---

### 3. Why This Matters: Real Attack Scenarios

BishopFox surveyed 49 JSON parsers and cataloged exploitable inconsistencies. Here are three attack patterns:

#### 3a. Key Collision Attacks (Duplicate Key Precedence)

Scenario: Cart service validates, Payment service processes.

```json
{"qty": 1, "qty": -1}
```

- Cart service (Python, last-key precedence): sees `qty: -1`, fails validation? No — JSON Schema validates the *parsed* object, which only has one key.
- Payment service (Go, first-key precedence): sees `qty: 1`

Result: attacker gets items, payment processes negative amount (refund).

#### 3b. Large Number Overflow

```json
{"qty": 999999999999999999999999999999999999999999999999999999999999}
```

- Cart service (Python): faithfully decodes to Python's arbitrary-precision int
- Payment service (Go with `buger/jsonparser`): overflows, returns `0`

Result: qty validates as huge number, processes as zero cost.

#### 3c. Character Truncation

Inject control characters to create "shadow keys":

```json
{"qty": 1, "qty\u0000": -1}
```

Some parsers truncate at NUL byte, seeing two different keys. Others see one key with a NUL in its name. The mismatch creates exploitable gaps.

---

### 4. The Microservices Amplifier

In a monolith, parser quirks are annoying. In microservices, they're a vulnerability class.

> "Parsers provided by standard libraries tended to be the most compliant, but they often lacked speed, which is of increasing importance in microservice architectures."
> — BishopFox

Performance pressure drives teams to third-party parsers. Each service picks its own. Your validation layer uses Python's `json`, your business logic uses Go's `encoding/json`, your downstream uses Node's `JSON.parse` — three different interpretations of the same payload.

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Gateway   │───▶│   Service   │───▶│  Database   │
│  (Python)   │    │    (Go)     │    │   (Node)    │
│ last-key    │    │ first-key   │    │ last-key    │
└─────────────┘    └─────────────┘    └─────────────┘
       │                 │                   │
       └── {"a":1,"a":2} sees a=2           │
                         └── sees a=1       │
                                            └── sees a=2 again
```

Validation passed at the gateway. Business logic saw different data. The vulnerability exists nowhere and everywhere.

---

### 5. Practical Mitigations

1. **Pick one parser, use it everywhere**
   - Reserialize at service boundaries
   - Don't pass raw JSON strings through validation layers

2. **Reject duplicates explicitly**
   - Python: use `object_pairs_hook` to detect duplicates
   - Most parsers can be configured to error on duplicate keys

3. **Validate the parsed object, not just the schema**
   - JSON Schema validates structure, not parsing semantics
   - Add explicit checks for edge cases

4. **Use strict mode**
   - Python: `json.dumps(..., allow_nan=False)`
   - Disable lenient parsing features

5. **Test with JSONTestSuite**
   - Seriot's test corpus: https://github.com/nst/JSONTestSuite
   - Run it against your stack's parsers
   - Document where they diverge

---

### 6. Closing Thought

JSON's simplicity is a mirage. The spec punts on hard decisions, and every library author made different choices. In a single-service world, this is an annoyance. In microservices, it's a vulnerability class.

The fix isn't to abandon JSON — it's to stop assuming all parsers agree. They don't. They never did.

---

## References

- [BishopFox: An Exploration of JSON Interoperability Vulnerabilities](https://bishopfox.com/blog/json-interoperability-vulnerabilities)
- [Seriot: Parsing JSON is a Minefield](https://seriot.ch/projects/parsing_json.html)
- [RFC 8259: The JSON Data Interchange Format](https://tools.ietf.org/html/rfc8259)
- [JSONTestSuite on GitHub](https://github.com/nst/JSONTestSuite)
- [BishopFox Labs: json-interop-vuln-labs](https://github.com/BishopFox/json-interop-vuln-labs)
