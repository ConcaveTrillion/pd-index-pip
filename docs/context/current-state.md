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

No long-lived feature or migration work is recorded as in flight on the base
branch.

## Risks and test health

No red or flaky tests are documented. Asset enumeration depends on the GitHub
API, and regeneration fails closed when an allowlisted repository or release
cannot be read. See the architecture evidence for the implementation and tests.
