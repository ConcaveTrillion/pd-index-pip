<!--
Status: active
Owner: CT
Created: 2026-07-14
Last verified: 2026-07-14
Kind: context
-->

# Durable decisions

## Agent Index

- **Status:** active
- **Owner:** CT
- **Created:** 2026-07-14
- **Last verified:** 2026-07-14
- **Kind:** context
- **Read when:** checking durable repository decisions and their evidence.
- **Search terms:** decisions, docgraph migration, spec lifecycle, lint suppression.

### 2026-07-14 — Govern repository documentation with docgraph

- **Context:** Repository documentation lacked explicit lifecycle metadata,
  authored context, and graph-integrity enforcement.
- **Decision:** Track the repository root as the docgraph scope, use `master` as
  the workflow base, enforce touched-document metadata, and detect
  legacy-unverified live documents.
- **Rationale:** Explicit status and graph checks keep current truth
  distinguishable from stale or historical material.
- **Evidence:** `docgraph.toml`, `DOCGRAPH.md`, and the three files in
  `docs/context/`.
- **Remaining work:** none.

### 2026-07-14 — Promote shipped truth before retiring implementation documents

- **Context:** The earlier convention described moving a completed design spec
  into architecture as a whole file.
- **Decision:** Promote current behavior and durable rationale into architecture
  and context first. Then remove completed checklist scaffolding after neighbor
  analysis, tombstone recording, reindexing, and strict checks.
- **Rationale:** Current retrieval should contain shipped truth and residual
  intent without obsolete execution projections.
- **Evidence:** `CONVENTIONS.md`, `DOCGRAPH.md`, and the active doc-retirer policy
  used for this migration.
- **Remaining work:** none.

### 2026-07-14 — Keep only live lint suppressions

- **Context:** The Ruff configuration suppressed `ANN401`, but an unsuppressed
  audit produced no `ANN401` finding. The shared script rules covered more
  call sites than the catalogue described.
- **Decision:** Remove the unused `ANN401` ignore and document the full safety
  basis for `T201`, `S603`, `S607`, `S101`, and `SC2086`.
- **Rationale:** A suppression catalogue is trustworthy only when it matches
  source and configuration.
- **Evidence:** `pyproject.toml`, `scripts/regen_index.py`,
  `scripts/update_github_actions.py`, `scripts/release-common.sh`, and
  `docs/conventions/lint-deviations.md`.
- **Remaining work:** Automated catalogue drift detection remains deferred in
  `docs/context/intent-map.md`.

### 2026-07-14 — Verify legacy guidance as active

- **Context:** Six inferred live documents were stale or legacy-unverified and
  lacked explicit lifecycle evidence.
- **Decision:** Keep `AGENTS.md`, `CLAUDE.md`, `CONVENTIONS.md`,
  `docs/conventions/ignored-surfaces.md`,
  `docs/conventions/lint-deviations.md`, and
  `docs/process/writing-style.md` active.
- **Rationale:** Each document still governs or accurately describes current
  repository behavior; none is implementation scaffolding or superseded
  history.
- **Evidence:** Commit `4a3d73f` created the assistant guidance and conventions;
  commits `799968c` and `2e4235a` refreshed or established the writing rules;
  commit `e4f3a79` added ignore and lint governance. `Makefile`,
  `.github/workflows/ci.yml`, `.github/workflows/regen.yml`, `.gitignore`,
  `pyproject.toml`, and `scripts/release-common.sh` implement the current
  commands, surfaces, and suppressions.
- **Remaining work:** none.
