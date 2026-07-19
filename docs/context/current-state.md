<!--
Status: active
Owner: CT
Created: 2026-07-14
Last verified: 2026-07-14
Kind: context
-->

# Current state

## Agent Index

- **Status:** active
- **Owner:** CT
- **Created:** 2026-07-14
- **Last verified:** 2026-07-14
- **Kind:** context
- **Read when:** starting repository work or checking current operational truth.
- **Search terms:** current state, index generator, CI, release workflow, risks.

## What matters now

The repository generates a static PEP 503 index from allowlisted GitHub Release
assets. The current trust boundary, digest behavior, consumer configuration,
and publication flow are in the
[release-asset index architecture](../architecture/python-release-asset-index.md).

`make ci` is the local verification gate. It runs Ruff, basedpyright,
actionlint, ShellCheck, Markdown formatting checks, and pytest.

## In-flight work

The GitHub issue tracker migration is complete. All 21 issues were permanently
deleted on 2026-07-19 and GitHub Issues is disabled, so `docs/issues/` is now
the only issue tracker for this repository. The audit trail is the
[migration ledger](github-issue-migration-ledger.md) and the
[deletion journal](github-issue-deletion-journal.md).

Two items survive that migration:

- **Active work:** resolving the `gh` executable before subprocess invocation,
  in [the gh-021 record](../issues/2026-07-19-gh-021-resolve-gh-executable.md).
- **Needs owner decision:** what remains of the pd-index rename effort, in
  [the rename sweep record](../issues/2026-07-19-gh-001-015-rename-sweep.md).

## Risks and test health

No red or flaky tests are documented. Asset enumeration depends on the GitHub
API, and regeneration fails closed when an allowlisted repository or release
cannot be read. See the architecture evidence for the implementation and tests.
