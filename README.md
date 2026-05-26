# pd-index

Self-hosted [PEP 503](https://peps.python.org/pep-0503/) simple Python package index for the `pd-*` family of repos under [github.com/ConcaveTrillion](https://github.com/ConcaveTrillion).

Wheels themselves live as **GitHub Release assets** in each individual `pd-*` repo. This repo just publishes a static HTML index that hyperlinks to those release assets, so [`uv`](https://docs.astral.sh/uv/) / `pip` can resolve cross-repo `pd-*` dependencies without needing the names to exist on PyPI.

## URL

Once GitHub Pages is enabled on this repo, the index will be live at:

```
https://concavetrillion.github.io/pd-index/simple/
```

## How consumers use it

Add `--extra-index-url https://concavetrillion.github.io/pd-index/simple/` to whatever invocation installs a `pd-*` wheel. For example, the `pdomain-ocr-cli/install.sh` script can:

```sh
uv tool install --reinstall ./pdomain_ocr_cli-X.Y.Z-py3-none-any.whl \
    --extra-index-url https://concavetrillion.github.io/pd-index/simple/
```

For a project's `pyproject.toml` (declarative form):

```toml
[[tool.uv.index]]
name = "pd-index"
url = "https://concavetrillion.github.io/pd-index/simple/"
explicit = false
```

## How it stays up to date

`.github/workflows/regen.yml` runs every 15 minutes (cron) and on `workflow_dispatch` / `repository_dispatch`. It:

1. Calls `scripts/regen_index.py`, which uses the GitHub API (read-only, public, no PAT required) to enumerate every release asset across the configured `pd-*` repos.
2. Renders PEP 503 simple-index HTML into `_site/simple/`.
3. Deploys `_site/` via [`actions/deploy-pages`](https://github.com/actions/deploy-pages) — no commits are made to `main` from CI.

To trigger an immediate rebuild without waiting for cron, individual `pd-*` release workflows can dispatch a `pd-release-published` event to this repo (one HTTP call with a fine-grained PAT). The cron is the safety net.

## Repos covered

The list lives in `scripts/regen_index.py` (`REPOS`). Adding a new `pd-*` repo: append it there, push, the next cron / workflow_dispatch picks it up.

## Why not just publish to PyPI?

Eventually we may. This index is a stepping stone: it speaks the same protocol PyPI does, so migrating later is a matter of `uv publish` + dropping the `--extra-index-url` flag. No wheel changes, no metadata changes.

The `pd-*` repos already follow a few habits to keep that door open:
- Plain version-pinned dep specifiers in `pyproject.toml` (no PEP 508 direct-URL deps that PyPI would reject).
- Release versions are immutable (no asset overwrites — PyPI rejects re-uploads of the same version).
- PEP 440-clean version strings.

## Local dry-run

```sh
gh auth status              # any GitHub auth is fine; only public reads
python scripts/regen_index.py --out /tmp/pd-index-out/simple
ls /tmp/pd-index-out/simple/
```
