from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import tempfile
import unittest
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Any, Iterable

import yaml


SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
NOTEBOOK_STATUSES = {
    "researching",
    "drafting",
    "reviewing",
    "ready",
    "published",
    "parked",
}
STREAM_STATUSES = {"open", "running", "landed", "dropped"}
ACTIVE_STATUSES = {"researching", "drafting", "reviewing", "ready"}
ARCHIVE_STATUSES = {"published", "parked"}
KINDS = {"technical", "undertones"}
STATUS_ORDER = {
    "ready": 0,
    "reviewing": 1,
    "drafting": 2,
    "researching": 3,
    "parked": 4,
    "published": 5,
}
OWNERSHIP_MARKER = "THIS FILE IS JUNAID'S"
UNFINISHED_RE = re.compile(
    r"(?im)^\s*>.*\bwork in progress\b|(?:\(|`)\s*todo:|\bTODO:\s+(?:verify|write|fix|add|replace|check|come up)"
)


class NotebookError(RuntimeError):
    pass


@dataclass
class NotebookRow:
    notebook: str
    kind: str
    status: str
    thesis: str
    open_streams: int
    target: str
    last_touched: str
    archived: bool
    path: str


def repo_root() -> Path:
    configured = os.environ.get("NOTEBOOK_REPO_ROOT")
    if configured:
        return Path(configured).resolve()

    current = Path.cwd().resolve()
    for candidate in (current, *current.parents):
        if (candidate / "hugo.toml").is_file() and (candidate / "writing").is_dir():
            return candidate
    raise NotebookError("run this command inside the website repository")


def validate_slug(slug: str) -> None:
    if not SLUG_RE.fullmatch(slug):
        raise NotebookError(
            f"invalid slug {slug!r}; use lowercase letters, digits, and single hyphens"
        )


def normalize_kind(kind: str) -> str:
    if kind == "essay":
        return "undertones"
    if kind not in KINDS:
        raise NotebookError("kind must be 'technical' or 'undertones'")
    return kind


def split_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise NotebookError(f"{path}: missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise NotebookError(f"{path}: unterminated YAML frontmatter")
    raw = text[4:end]
    try:
        data = yaml.safe_load(raw) or {}
    except yaml.YAMLError as exc:
        raise NotebookError(f"{path}: invalid YAML frontmatter: {exc}") from exc
    if not isinstance(data, dict):
        raise NotebookError(f"{path}: frontmatter must be a mapping")
    return data, text[end + 5 :]


def render_frontmatter(data: dict[str, Any], body: str) -> str:
    raw = yaml.safe_dump(data, sort_keys=False, allow_unicode=True).rstrip()
    return f"---\n{raw}\n---\n{body.lstrip()}"


def render_template(path: Path, replacements: dict[str, str]) -> str:
    text = path.read_text(encoding="utf-8")
    for key, value in replacements.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def notebook_dir(root: Path, kind: str, slug: str, *, archived: bool = False) -> Path:
    lane = root / "writing" / "notebooks" / normalize_kind(kind)
    return lane / "archive" / slug if archived else lane / slug


def create_notebook(
    root: Path, slug: str, title: str, kind: str, status: str = "researching"
) -> Path:
    validate_slug(slug)
    kind = normalize_kind(kind)
    if status not in ACTIVE_STATUSES:
        raise NotebookError(
            f"new notebook status must be one of {sorted(ACTIVE_STATUSES)}"
        )
    destination = notebook_dir(root, kind, slug)
    if destination.exists():
        raise NotebookError(f"refusing to overwrite existing notebook: {destination}")

    templates = root / ".agents" / "skills" / "notebooks" / "templates"
    today = date.today().isoformat()
    replacements = {
        "TITLE": title,
        "DATE": today,
        "KIND": kind,
        "SLUG": slug,
        "STATUS": status,
    }
    destination.mkdir(parents=True)
    (destination / "research").mkdir()
    (destination / "artifacts").mkdir()
    (destination / "research" / ".gitkeep").touch()
    (destination / "artifacts" / ".gitkeep").touch()
    for name in ("notebook.md", "draft.md", "sources.md"):
        (destination / name).write_text(
            render_template(templates / name, replacements), encoding="utf-8"
        )
    return destination


def marked_outline(seed: str) -> str | None:
    match = re.search(
        r"<!--\s*draft-outline:start\s*-->(.*?)<!--\s*draft-outline:end\s*-->",
        seed,
        flags=re.DOTALL | re.IGNORECASE,
    )
    return match.group(1).strip() if match else None


def promote_idea(root: Path, slug: str, kind: str) -> Path:
    validate_slug(slug)
    idea = root / "writing" / "ideas" / f"{slug}.md"
    if not idea.is_file():
        raise NotebookError(f"idea not found: {idea}")
    data, body = split_frontmatter(idea)
    title_match = re.search(r"(?m)^#\s+(.+)$", body)
    if not title_match:
        raise NotebookError(f"{idea}: missing H1 title")
    destination = create_notebook(root, slug, title_match.group(1).strip(), kind)
    shutil.copy2(idea, destination / "artifacts" / "seed.md")

    outline = marked_outline(idea.read_text(encoding="utf-8"))
    if outline:
        draft = destination / "draft.md"
        text = draft.read_text(encoding="utf-8")
        text = text.replace("<!-- Junaid may place an outline below. -->", outline)
        draft.write_text(text, encoding="utf-8")

    notebook = destination / "notebook.md"
    notebook_data, notebook_body = split_frontmatter(notebook)
    notebook_data["promoted_from"] = f"writing/ideas/{slug}.md"
    notebook.write_text(
        render_frontmatter(notebook_data, notebook_body), encoding="utf-8"
    )
    return destination


def iter_notebook_files(
    root: Path, include_archive: bool = False
) -> Iterable[tuple[Path, bool]]:
    base = root / "writing" / "notebooks"
    for kind in sorted(KINDS):
        lane = base / kind
        if not lane.is_dir():
            continue
        for path in sorted(lane.glob("*/notebook.md")):
            if path.parent.name != "archive":
                yield path, False
        if include_archive:
            for path in sorted((lane / "archive").glob("*/notebook.md")):
                yield path, True


def plain_thesis(body: str) -> str:
    for line in body.splitlines():
        if line.startswith(">"):
            value = line.lstrip("> ").replace("**", "").replace("_", "").strip()
            value = re.sub(
                r"^Thesis\s*/?\s*question\.\s*", "", value, flags=re.IGNORECASE
            )
            return value
    return ""


def count_open_streams(notebook_body: str, notebook_dir_path: Path) -> int:
    statuses: dict[str, str] = {}
    research = notebook_dir_path / "research"
    if research.is_dir():
        for stream in research.glob("*.md"):
            try:
                data, _ = split_frontmatter(stream)
            except NotebookError:
                continue
            statuses[stream.name] = str(data.get("status", ""))

    count = sum(1 for value in statuses.values() if value in {"open", "running"})
    referenced = set(re.findall(r"`research/([a-z0-9][a-z0-9-]*\.md)`", notebook_body))
    missing_from_disk = [name for name in referenced if name not in statuses]
    return count + len(missing_from_disk)


def read_rows(root: Path, include_archive: bool = False) -> list[NotebookRow]:
    rows: list[NotebookRow] = []
    for path, archived in iter_notebook_files(root, include_archive):
        data, body = split_frontmatter(path)
        rows.append(
            NotebookRow(
                notebook=path.parent.name,
                kind=str(data.get("kind", path.parents[1].name)),
                status=str(data.get("status", "")),
                thesis=plain_thesis(body),
                open_streams=count_open_streams(body, path.parent),
                target=str(data.get("target") or ""),
                last_touched=str(data.get("updated") or ""),
                archived=archived,
                path=str(path.parent.relative_to(root)),
            )
        )
    rows.sort(
        key=lambda row: (
            row.archived,
            STATUS_ORDER.get(row.status, 99),
            row.last_touched,
            row.notebook,
        )
    )
    return rows


def clipped(value: str, width: int) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    return value if len(value) <= width else value[: width - 1] + "…"


def print_status(rows: list[NotebookRow], as_json: bool) -> None:
    if as_json:
        print(json.dumps([asdict(row) for row in rows], indent=2, ensure_ascii=False))
        return
    headers = ["Notebook", "Kind", "Status", "Thesis", "Open", "Target", "Last touched"]
    values = [
        [
            row.notebook,
            row.kind,
            row.status,
            clipped(row.thesis, 54),
            str(row.open_streams),
            clipped(row.target, 30),
            row.last_touched,
        ]
        for row in rows
    ]
    widths = [len(header) for header in headers]
    for value_row in values:
        widths = [max(current, len(value)) for current, value in zip(widths, value_row)]
    print("  ".join(header.ljust(width) for header, width in zip(headers, widths)))
    print("  ".join("-" * width for width in widths))
    for value_row in values:
        print("  ".join(value.ljust(width) for value, width in zip(value_row, widths)))


def append_log(body: str, message: str) -> str:
    line = f"- **{date.today().isoformat()}** — {message}\n"
    if re.search(r"(?m)^## Log\s*$", body):
        return body.rstrip() + "\n" + line
    return body.rstrip() + "\n\n---\n\n## Log\n" + line


def find_slug(root: Path, slug: str, *, archived: bool) -> tuple[Path, str]:
    validate_slug(slug)
    for kind in sorted(KINDS):
        candidate = notebook_dir(root, kind, slug, archived=archived)
        if candidate.is_dir():
            return candidate, kind
    location = "archived" if archived else "active"
    raise NotebookError(f"{location} notebook not found: {slug}")


def archive_notebook(root: Path, slug: str, status: str, reason: str) -> Path:
    if status not in ARCHIVE_STATUSES:
        raise NotebookError("archive status must be 'parked' or 'published'")
    source, kind = find_slug(root, slug, archived=False)
    destination = notebook_dir(root, kind, slug, archived=True)
    if destination.exists():
        raise NotebookError(f"refusing to overwrite archived notebook: {destination}")
    data, body = split_frontmatter(source / "notebook.md")
    data["status"] = status
    data["updated"] = date.today().isoformat()
    data["archive_reason"] = reason
    body = append_log(body, f"{status}: {reason}")
    (source / "notebook.md").write_text(
        render_frontmatter(data, body), encoding="utf-8"
    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(source), str(destination))
    return destination


def revive_notebook(root: Path, slug: str, status: str, reason: str) -> Path:
    if status not in ACTIVE_STATUSES:
        raise NotebookError(f"revived status must be one of {sorted(ACTIVE_STATUSES)}")
    source, kind = find_slug(root, slug, archived=True)
    destination = notebook_dir(root, kind, slug)
    if destination.exists():
        raise NotebookError(f"refusing to overwrite active notebook: {destination}")
    data, body = split_frontmatter(source / "notebook.md")
    if data.get("status") != "parked":
        raise NotebookError("only parked notebooks can be revived")
    data["status"] = status
    data["updated"] = date.today().isoformat()
    data["revived_reason"] = reason
    body = append_log(body, f"revived as {status}: {reason}")
    (source / "notebook.md").write_text(
        render_frontmatter(data, body), encoding="utf-8"
    )
    shutil.move(str(source), str(destination))
    return destination


def source_ids(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    return set(re.findall(r"(?m)^## \[S(\d+)\]", text))


def draft_citations(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    if text.startswith("<!--") and "-->" in text:
        text = text.split("-->", 1)[1]
    return set(re.findall(r"(?<!\^)\[S(\d+)\]", text))


def doctor(root: Path) -> list[str]:
    errors: list[str] = []
    targets: dict[str, Path] = {}
    notebooks = list(iter_notebook_files(root, include_archive=True))

    for notebook_file, archived in notebooks:
        directory = notebook_file.parent
        slug = directory.name
        relative = directory.relative_to(root)
        try:
            validate_slug(slug)
        except NotebookError as exc:
            errors.append(f"{relative}: {exc}")

        for required in (
            "notebook.md",
            "draft.md",
            "sources.md",
            "research",
            "artifacts",
        ):
            if not (directory / required).exists():
                errors.append(f"{relative}: missing {required}")

        try:
            data, body = split_frontmatter(notebook_file)
        except NotebookError as exc:
            errors.append(str(exc))
            continue

        status = str(data.get("status", ""))
        kind = str(data.get("kind", ""))
        for field in ("kind", "status", "target", "created", "updated"):
            if field not in data:
                errors.append(f"{relative}: missing frontmatter field {field!r}")
        if status not in NOTEBOOK_STATUSES:
            errors.append(f"{relative}: invalid notebook status {status!r}")
        if kind not in KINDS:
            errors.append(f"{relative}: invalid kind {kind!r}")
        if archived and status not in ARCHIVE_STATUSES:
            errors.append(f"{relative}: archived notebook has active status {status!r}")
        if not archived and status not in ACTIVE_STATUSES:
            errors.append(f"{relative}: active notebook has archived status {status!r}")

        draft = directory / "draft.md"
        if draft.is_file() and OWNERSHIP_MARKER not in draft.read_text(
            encoding="utf-8"
        ):
            errors.append(f"{relative}: draft.md is missing the ownership banner")

        sources = directory / "sources.md"
        if draft.is_file() and sources.is_file():
            missing = draft_citations(draft) - source_ids(sources)
            if missing:
                errors.append(
                    f"{relative}: citation IDs missing from sources.md: {', '.join('S' + i for i in sorted(missing, key=int))}"
                )

        referenced_streams = set(
            re.findall(r"`research/([a-z0-9][a-z0-9-]*\.md)`", body)
        )
        for stream_name in sorted(referenced_streams):
            stream_path = directory / "research" / stream_name
            if not stream_path.is_file():
                errors.append(
                    f"{relative}: referenced research stream is missing: research/{stream_name}"
                )
                continue
            try:
                stream_data, _ = split_frontmatter(stream_path)
            except NotebookError as exc:
                errors.append(str(exc))
                continue
            if stream_data.get("status") not in STREAM_STATUSES:
                errors.append(
                    f"{stream_path.relative_to(root)}: invalid stream status {stream_data.get('status')!r}"
                )

        research_dir = directory / "research"
        if research_dir.is_dir():
            for stream_path in sorted(research_dir.glob("*.md")):
                try:
                    stream_data, _ = split_frontmatter(stream_path)
                except NotebookError as exc:
                    errors.append(str(exc))
                    continue
                if stream_data.get("status") not in STREAM_STATUSES:
                    errors.append(
                        f"{stream_path.relative_to(root)}: invalid stream status {stream_data.get('status')!r}"
                    )
                if stream_data.get("stream") != stream_path.stem:
                    errors.append(
                        f"{stream_path.relative_to(root)}: stream field must match filename {stream_path.stem!r}"
                    )

        target = str(data.get("target") or "")
        if target:
            if target in targets:
                errors.append(
                    f"target collision: {target} used by {targets[target].parent} and {directory}"
                )
            else:
                targets[target] = notebook_file
            target_path = root / target
            if not archived and status != "published" and target_path.is_file():
                try:
                    target_data, _ = split_frontmatter(target_path)
                except NotebookError as exc:
                    errors.append(str(exc))
                else:
                    if target_data.get("draft") is False:
                        errors.append(
                            f"{relative}: unfinished notebook target is public: {target}"
                        )

    for post in sorted((root / "content" / "posts").rglob("*.md")):
        try:
            data, body = split_frontmatter(post)
        except NotebookError as exc:
            errors.append(str(exc))
            continue
        body_without_fences = re.sub(r"(?ms)^```.*?^```\s*", "", body)
        if data.get("draft") is False and UNFINISHED_RE.search(body_without_fences):
            errors.append(
                f"{post.relative_to(root)}: public page contains an unfinished marker"
            )
        if "/Users/junaidrahim/Obsidian/Everything" in post.read_text(encoding="utf-8"):
            errors.append(
                f"{post.relative_to(root)}: public page leaks an absolute source-vault path"
            )

    for path in (root / "content").rglob("*"):
        if path.is_file() and "research" in path.parts:
            errors.append(
                f"{path.relative_to(root)}: notebook research must not live under public content"
            )

    for path in (root / "writing").rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if "[[" in text or "]]" in text:
            errors.append(f"{path.relative_to(root)}: unresolved Obsidian wiki-link")

    for path in sorted((root / "writing" / "ideas").glob("*.md")):
        try:
            data, _ = split_frontmatter(path)
            validate_slug(path.stem)
        except NotebookError as exc:
            errors.append(str(exc))
            continue
        if data.get("status") != "idea":
            errors.append(f"{path.relative_to(root)}: idea status must be 'idea'")
        if data.get("kind") not in KINDS:
            errors.append(
                f"{path.relative_to(root)}: invalid idea kind {data.get('kind')!r}"
            )

    for archive_status in ("archived", "cancelled"):
        archive_dir = root / "writing" / "archive" / "blog-notes" / archive_status
        for path in sorted(archive_dir.glob("*.md")):
            try:
                data, _ = split_frontmatter(path)
            except NotebookError as exc:
                errors.append(str(exc))
                continue
            if data.get("status") != archive_status:
                errors.append(
                    f"{path.relative_to(root)}: status must be {archive_status!r}"
                )

    return errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="notebook", description="Manage repository-local writing notebooks"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    new = sub.add_parser("new", help="create a notebook")
    new.add_argument("slug")
    new.add_argument("title")
    new.add_argument("--kind", default="technical", choices=sorted(KINDS))
    new.add_argument("--status", default="researching", choices=sorted(ACTIVE_STATUSES))

    promote = sub.add_parser("promote", help="promote a committed idea into a notebook")
    promote.add_argument("slug")
    promote.add_argument("--kind", default="technical", choices=sorted(KINDS))

    status = sub.add_parser("status", help="show the notebook dashboard")
    status.add_argument("--all", action="store_true", help="include archived notebooks")
    status.add_argument(
        "--json", action="store_true", help="emit machine-readable JSON"
    )

    check = sub.add_parser("doctor", help="validate the writing system")
    check.add_argument("--json", action="store_true", help="emit machine-readable JSON")

    archive = sub.add_parser("archive", help="park or archive an active notebook")
    archive.add_argument("slug")
    archive.add_argument("--status", default="parked", choices=sorted(ARCHIVE_STATUSES))
    archive.add_argument("--reason", default="Archived by explicit notebook command.")

    revive = sub.add_parser("revive", help="revive a parked notebook")
    revive.add_argument("slug")
    revive.add_argument(
        "--status", default="researching", choices=sorted(ACTIVE_STATUSES)
    )
    revive.add_argument("--reason", default="Revived by explicit notebook command.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        root = repo_root()
        if args.command == "new":
            path = create_notebook(root, args.slug, args.title, args.kind, args.status)
            print(f"created {path.relative_to(root)}")
        elif args.command == "promote":
            path = promote_idea(root, args.slug, args.kind)
            print(f"promoted writing/ideas/{args.slug}.md -> {path.relative_to(root)}")
        elif args.command == "status":
            print_status(read_rows(root, include_archive=args.all), args.json)
        elif args.command == "doctor":
            errors = doctor(root)
            if args.json:
                print(json.dumps({"ok": not errors, "errors": errors}, indent=2))
            elif errors:
                print("notebook doctor found problems:", file=sys.stderr)
                for error in errors:
                    print(f"- {error}", file=sys.stderr)
            else:
                print("notebook doctor: ok")
            return 1 if errors else 0
        elif args.command == "archive":
            path = archive_notebook(root, args.slug, args.status, args.reason)
            print(f"archived {path.relative_to(root)}")
        elif args.command == "revive":
            path = revive_notebook(root, args.slug, args.status, args.reason)
            print(f"revived {path.relative_to(root)}")
        return 0
    except (NotebookError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


NOTEBOOK_TEST_TEMPLATE = """---
kind: {{KIND}}
status: {{STATUS}}
target: ""
week:
created: {{DATE}}
updated: {{DATE}}
---

# {{TITLE}}

> **Thesis / question.**

## Research streams

---

## Log
- **{{DATE}}** — created the notebook.
"""

DRAFT_TEST_TEMPLATE = """<!--
  THIS FILE IS JUNAID'S.
  Agents do not write prose here.
-->

# {{TITLE}}

<!-- Junaid may place an outline below. -->
"""

SOURCES_TEST_TEMPLATE = "# Sources\n"


class NotebookCliTest(unittest.TestCase):
    """Focused checks kept here so the root project remains a single Python file."""

    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        templates = self.root / ".agents" / "skills" / "notebooks" / "templates"
        templates.mkdir(parents=True)
        (templates / "notebook.md").write_text(NOTEBOOK_TEST_TEMPLATE, encoding="utf-8")
        (templates / "draft.md").write_text(DRAFT_TEST_TEMPLATE, encoding="utf-8")
        (templates / "sources.md").write_text(SOURCES_TEST_TEMPLATE, encoding="utf-8")
        for kind in ("technical", "undertones"):
            (self.root / "writing" / "notebooks" / kind / "archive").mkdir(parents=True)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_slug_validation(self) -> None:
        validate_slug("valid-slug-2")
        for invalid in ("Bad-Slug", "bad_slug", "-bad", "bad-", "bad--slug", ""):
            with self.subTest(invalid=invalid), self.assertRaises(NotebookError):
                validate_slug(invalid)

    def test_path_handling(self) -> None:
        self.assertEqual(
            notebook_dir(self.root, "technical", "one"),
            self.root / "writing" / "notebooks" / "technical" / "one",
        )
        self.assertEqual(
            notebook_dir(self.root, "undertones", "one", archived=True),
            self.root / "writing" / "notebooks" / "undertones" / "archive" / "one",
        )

    def test_create_refuses_overwrite(self) -> None:
        create_notebook(self.root, "one-piece", "One piece", "technical")
        with self.assertRaises(NotebookError):
            create_notebook(self.root, "one-piece", "Replacement", "technical")

    def test_status_parsing_skips_archive_by_default(self) -> None:
        create_notebook(
            self.root, "active-piece", "Active piece", "technical", "drafting"
        )
        create_notebook(self.root, "park-me", "Park me", "technical")
        archive_notebook(self.root, "park-me", "parked", "Scope cut.")
        self.assertEqual(
            [row.notebook for row in read_rows(self.root)], ["active-piece"]
        )
        self.assertEqual(
            {row.notebook for row in read_rows(self.root, include_archive=True)},
            {"active-piece", "park-me"},
        )

    def test_archive_moves_notebook_and_updates_status(self) -> None:
        create_notebook(self.root, "archivable", "Archivable", "undertones")
        destination = archive_notebook(
            self.root, "archivable", "parked", "Not this month."
        )
        self.assertTrue((destination / "notebook.md").is_file())
        self.assertFalse(notebook_dir(self.root, "undertones", "archivable").exists())
        text = (destination / "notebook.md").read_text(encoding="utf-8")
        self.assertIn("status: parked", text)
        self.assertIn("Not this month.", text)

    def test_doctor_ignores_todo_identifiers_in_code(self) -> None:
        posts = self.root / "content" / "posts"
        posts.mkdir(parents=True)
        (posts / "example.md").write_text(
            "---\ndraft: false\n---\n\n```python\ndef add_todo(self, todo: Item):\n    pass\n```\n",
            encoding="utf-8",
        )
        self.assertEqual(doctor(self.root), [])

    def test_promote_preserves_seed_and_copies_only_marked_outline(self) -> None:
        ideas = self.root / "writing" / "ideas"
        ideas.mkdir(parents=True)
        idea = ideas / "selected-piece.md"
        original = """---
kind: technical
status: idea
created: 2026-08-23
updated: 2026-08-23
---

# Selected piece

Agent notes that must not become draft prose.

<!-- draft-outline:start -->
- Junaid's first section
- Junaid's second section
<!-- draft-outline:end -->
"""
        idea.write_text(original, encoding="utf-8")
        destination = promote_idea(self.root, "selected-piece", "technical")
        self.assertEqual(idea.read_text(encoding="utf-8"), original)
        self.assertEqual(
            (destination / "artifacts" / "seed.md").read_text(encoding="utf-8"),
            original,
        )
        draft = (destination / "draft.md").read_text(encoding="utf-8")
        self.assertIn("Junaid's first section", draft)
        self.assertNotIn("Agent notes", draft)
        with self.assertRaises(NotebookError):
            promote_idea(self.root, "selected-piece", "technical")


if __name__ == "__main__":
    raise SystemExit(main())
