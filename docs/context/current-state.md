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

The GitHub issue tracker is being migrated into governed documentation. All 21
issues are accounted for in the
[migration ledger](github-issue-migration-ledger.md); none has been deleted from
GitHub. The cutover is blocked on two gates: organization-level issue deletion
is unconfirmed, and the migration has not been pushed to the remote default
branch. The procedure is in the
[migration runbook](../runbooks/github-issues-to-docgraph-migration.md).

One piece of genuine open work came out of that migration: resolving the `gh`
executable before subprocess invocation, in
[the gh-021 record](../issues/2026-07-19-gh-021-resolve-gh-executable.md).

## Risks and test health

No red or flaky tests are documented. Asset enumeration depends on the GitHub
API, and regeneration fails closed when an allowlisted repository or release
cannot be read. See the architecture evidence for the implementation and tests.
