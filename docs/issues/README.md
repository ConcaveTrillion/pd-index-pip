---
Status: active
Owner: CT
Created: 2026-07-15
Last verified: 2026-07-15
Kind: process
Level: I1
---

# Issues

## Agent Index

- **Kind:** process
- **Status:** active
- **Level:** I1
- **Last verified:** 2026-07-15
- **Read when:** filing an issue or checking active and migrated issue records.
- **Search terms:** issues folder, issue report, migration, issue lifecycle.

## Purpose

`docs/issues/` holds governed issue reports that need a durable, citable record.
Each report is a docgraph node, so repository intent does not depend on an
external issue tracker.

## Convention

- Store reports in `docs/issues/`.
- Name migrated GitHub records `YYYY-MM-DD-gh-NNN-short-slug.md`.
- Keep frontmatter and Agent Index lifecycle fields consistent.
- Use `Status: active` for unresolved work.
- On resolution, route through `doc-retirer`: promote anything durable into the
  doc that owns it, delete the report, and write a tombstone to
  `docs/context/decisions.md`. Git history keeps the report.
- Link each record from governed context.
- Stage each record before reindexing and running the strict docgraph check.
- Copy `docs/issues/TEMPLATE.md` when creating a report. The template is
  excluded from the index and must not be linked as a governed node.

## Open issues

- [Resolve the gh executable before subprocess invocation](2026-07-19-gh-021-resolve-gh-executable.md)
  — active.
- [Rename sweep tracking cluster](2026-07-19-gh-001-015-rename-sweep.md) —
  needs owner decision.
- Migration records are listed in the [intent map](../context/intent-map.md).

## Where resolved work is recorded

- Completed GitHub issues are recorded in the
  [migration ledger](../context/github-issue-migration-ledger.md).
