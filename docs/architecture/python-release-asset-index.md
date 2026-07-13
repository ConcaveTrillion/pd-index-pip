# Python release-asset index

## Agent Index

- **Status:** active
- **Owner:** CT
- **Created:** 2026-07-13
- **Last verified:** 2026-07-13
- **Kind:** architecture

The index is a generated PEP 503 view over Python distributions attached to
allowlisted pdomain GitHub Releases. GitHub Pages stores only HTML. Package
bytes remain in each publisher repository.

## Trust boundary

`scripts/regen_index.py` is the only writer. It enumerates a fixed repository
allowlist and accepts assets only when all of these conditions hold:

- the filename is a wheel, source archive, or zip distribution;
- the normalized distribution name matches the allowlisted repository page;
- the URL is HTTPS on `github.com` under that repository's release-download
  path; and
- the decoded path does not traverse above that boundary.

Wrong-project, duplicate, non-distribution, and unsafe assets are skipped. A
missing allowlisted repository, a disappearing release, or a GitHub API failure
stops regeneration. The previous Pages deployment therefore remains available
instead of being replaced by an incomplete index.

## Integrity metadata

When GitHub supplies a `sha256:` digest, the generated link includes a PEP 503
`#sha256=` fragment. Assets without a GitHub SHA-256 digest remain installable,
but the generator never invents a digest from metadata it did not verify.

## Consumer resolution boundary

The generated project page is both an index endpoint and a source of direct
artifact links. One-off installs use the selected wheel URL as a direct package
requirement, retaining its hash fragment and authenticating to the artifact host
when required. This pins the pdomain distribution without replacing PyPI for
public transitive dependencies.

Repeatable project configuration declares this index with `explicit = true` and
maps each pdomain distribution through `[tool.uv.sources]`. Passing the index as
an unrestricted one-off `--index` does not establish the same package-to-source
binding: a missing project can fall through to another index by package name.

## Publication flow

The daily schedule is the recovery path. Publisher release workflows can send
`pdomain-release-published` for a prompt rebuild, and maintainers can dispatch
the workflow manually. Regeneration writes a fresh `_site/simple/` tree and the
official Pages actions deploy it without committing generated HTML.

## Evidence

- Code: `scripts/regen_index.py`
- Tests: `tests/test_regen_index.py`, `tests/test_dispatch_event_name.py`
- Workflow: `.github/workflows/regen.yml`
- Verified: 2026-07-13 against the current source and tests
