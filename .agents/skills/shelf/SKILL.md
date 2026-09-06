---
name: shelf
description: Maintain Junaid's public Shelf page when he sends photos, links, or names of books or textbooks to add, or reports a purchase, reading progress, or completion. Use for shelf updates, not notebook research or book reports.
---

# Shelf

The public `/shelf/` page is a simple reading inventory with exactly two sections: Books and Textbooks.
All technical books belong in Textbooks, including programming, mathematics, computing/AI,
engineering references, and engineering management/career guides. General nonfiction and literature
belong in Books. Preserve Junaid’s explicit category choices for existing entries. Junaid does not need to write reviews to add an item.

## Files

- `data/shelf.yaml` is the canonical item list. Edit it for routine additions and updates.
- `content/shelf.md` owns the page introduction and the two section shortcodes.
- `layouts/shortcodes/shelf-list.html` renders each section alphabetically by title; data-file order does not affect display.
- `assets/css/shelf.css` and `assets/js/shelf.js` own the page styling and animated header.

This skill lives in the website repository. Run its commands from that repository root.

## Capture and update

1. Read the existing list before editing. Identify the work from the supplied photo, URL, title, or ISBN.
   Inspect supplied images. Verify unclear title/author/edition details using the publisher, author's site,
   or another authoritative catalogue. Ask one focused question only if ambiguity
   would risk adding the wrong work; handle the unambiguous items in the meantime.
2. Match an existing entry across both sections by ISBN, canonical URL, or normalized title plus author. Update it rather
   than duplicating it. A purchase followed by completion is one entry. Keep its stable ID and `added` date.
3. Add to `books` or `textbooks`, with a verified title and authors. Prefer a publisher/author book page. Use a clean public URL without tracking parameters. Offline works may
   have no URL; do not invent one. Do not upload cover photos, receipts, annotations, or PDFs unless asked.
4. Set `status: finished` only when Junaid explicitly says he finished/read the book. Otherwise omit
   `status`; purchases and reading progress do not get tags. Never infer completion from a mention,
   photo, or purchase. Preserve an existing finished status when a copy is bought later.
5. Use today's date for `added` on new entries. `purchased` and `finished` dates are optional and only
   recorded when stated; resolve “today” or “yesterday” in Junaid's timezone. Do not turn an unknown event
   date into today's date. Store only exact dates as `YYYY-MM-DD` strings.
6. Keep notes optional. Preserve Junaid's supplied note; do not generate a review, rating, summary, or
   first-person opinion. No automatic backfill from his writing, vault, or someone else's shelf.

## Record format

Both top-level keys are YAML lists (`[]` when empty). Each item has:

- `id`: stable lowercase hyphenated title/author slug, unique across both sections.
- `title`: full title as a string.
- `authors`: list of author names; use the work's credited group author where appropriate.
- `added`: quoted `YYYY-MM-DD` capture date, retained as metadata.
- Optional `url`, `status` (`finished` only), `purchased`, `finished`, `isbn`, `note`.

Example schema only; do not add this placeholder to the real shelf:

```yaml
books:
  - id: title-author
    title: "Verified title"
    authors: ["Author name"]
    added: "2026-09-06"
    status: finished
textbooks: []
```

The page displays title, authors, an optional finished tag, completion month, and optional note. ISBN and
purchase dates remain useful matching metadata. All fields in this file are committed public metadata;
never include private purchase/account details or access tokens.

## Verify and report

Run `hugo` and `git diff --check`. Check the rendered `public/shelf/index.html` for the new entry,
correct section, working internal anchors, and the intended status/date. Confirm no duplicate IDs or works
were introduced. For layout or animation edits, also check narrow widths, light/dark themes,
and reduced motion; a data-only addition does not require redesigning the page.

Report what was added or updated and any unresolved identification. An instruction to add to the shelf
authorizes the repository edit; committing, pushing, or deployment follows the user's session instructions.
