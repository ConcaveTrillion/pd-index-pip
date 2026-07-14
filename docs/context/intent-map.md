<!--
Status: active
Owner: CT
Created: 2026-07-14
Last verified: 2026-07-14
Kind: context
-->

# Intent map

## Agent Index

- **Status:** active
- **Owner:** CT
- **Created:** 2026-07-14
- **Last verified:** 2026-07-14
- **Kind:** context
- **Read when:** evaluating direction, deferred work, rejected approaches, or owner decisions.
- **Search terms:** active intent, deferred work, rejected direction, owner decision.

## Active bets

- **Active:** Keep the static release-asset index as the current distribution
  path. Evidence: [README](../../README.md) and the
  [current architecture](../architecture/python-release-asset-index.md).

## Deferred work

- **Deferred:** Move pdomain distributions to PyPI. Each changed distribution
  needs a new version, then consumers can remove their private-index source
  mappings. Evidence: [README](../../README.md#why-not-just-publish-to-pypi).
- **Deferred:** Automate the audit between live lint suppressions and the
  [suppression catalogue](../conventions/lint-deviations.md). The migration
  verified the catalogue manually; no automated drift gate exists.
- **Deferred:** Replace or validate the space-delimited `RELEASE_VERSION_FILES`
  contract in `scripts/release-common.sh`. The current helper trusts a
  maintainer-provided environment value and cannot represent paths with spaces.

## Rejected directions

- **Rejected:** Configure the pdomain index as an unrestricted one-off index.
  This can fall through to a same-named public package. Use explicit source
  mappings or a direct artifact requirement. Evidence:
  [private-index decision](../decisions/private-index-resolution.md).

## Blocked (waiting on)

None.

## Needs owner decision

None.

## Legacy-unverified sweep

The 2026-07-14 migration classified `AGENTS.md`, `CLAUDE.md`, `CONVENTIONS.md`,
`docs/conventions/ignored-surfaces.md`, `docs/conventions/lint-deviations.md`,
and `docs/process/writing-style.md` as still active. The evidence is recorded in
the [2026-07-14 legacy-guidance decision](decisions.md#2026-07-14--verify-legacy-guidance-as-active).
