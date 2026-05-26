"""Regenerate the PEP 503 simple index from GitHub Releases of pd-* repos.

Reads release-asset metadata via the `gh` CLI (which uses GITHUB_TOKEN in CI or
the user's local auth in dev) and emits static HTML under --out.

PEP 503 only requires `<a href>` links to wheel/sdist filenames. We point each
link directly at the GitHub Release asset's browser_download_url so consumers
fetch from github.com release storage, not from this index host.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
from pathlib import Path

ORG = "ConcaveTrillion"

# Every pd-* repo that may publish wheel assets to GitHub Releases.
# Keep alphabetized. Append a new repo here when it starts cutting releases —
# safe to list a repo with zero releases (renders an empty page).
REPOS: list[str] = [
    "pdomain-book-tools",
    "pdomain-ocr-cli",
    "pd-ocr-labeler",
    "pdomain-ocr-labeler-spa",
    "pdomain-ocr-ops",
    "pdomain-ocr-synth",
    "pdomain-ocr-training",
    "pd-ocr-trainer",
    "pd-png-optimizer",
    "pdomain-prep-for-pgdp",
]


def normalize(name: str) -> str:
    """PEP 503 normalization: lowercase, runs of [-_.] collapse to a single -."""
    return re.sub(r"[-_.]+", "-", name).lower()


def gh_json(args: list[str]) -> object:
    """Run `gh` with --json output and parse. Raise on non-zero."""
    proc = subprocess.run(
        ["gh", *args], capture_output=True, text=True, check=True
    )
    return json.loads(proc.stdout)


def fetch_releases(repo: str) -> list[dict]:
    """Return non-draft releases for ConcaveTrillion/<repo>, with assets.

    Returns [] if the repo doesn't exist or has no releases. Errors other than
    not-found are re-raised — we want the workflow to fail loudly on auth or
    rate-limit problems rather than silently emit a stale empty page.
    """
    try:
        rels = gh_json(
            [
                "release",
                "list",
                "--repo",
                f"{ORG}/{repo}",
                "--limit",
                "1000",
                "--json",
                "tagName,name,isDraft,isPrerelease,publishedAt",
            ]
        )
    except subprocess.CalledProcessError as e:
        if "Could not resolve to a Repository" in (e.stderr or "") or "404" in (e.stderr or ""):
            print(f"  {repo}: repo not found, skipping", file=sys.stderr)
            return []
        raise

    out: list[dict] = []
    for rel in rels:
        if rel.get("isDraft"):
            continue
        tag = rel["tagName"]
        try:
            view = gh_json(
                [
                    "release",
                    "view",
                    tag,
                    "--repo",
                    f"{ORG}/{repo}",
                    "--json",
                    "assets",
                ]
            )
        except subprocess.CalledProcessError:
            print(f"  {repo}@{tag}: failed to fetch assets, skipping tag", file=sys.stderr)
            continue
        out.append(
            {
                "tag": tag,
                "is_prerelease": rel.get("isPrerelease", False),
                "published_at": rel.get("publishedAt", ""),
                "assets": view.get("assets", []),
            }
        )
    return out


_DIST_SUFFIXES = (".whl", ".tar.gz", ".zip")


def render_project_page(project_normalized: str, releases: list[dict]) -> str:
    lines = [
        "<!DOCTYPE html>",
        '<html><head>',
        '<meta name="pypi:repository-version" content="1.0">',
        f"<title>Links for {html.escape(project_normalized)}</title>",
        "</head><body>",
        f"<h1>Links for {html.escape(project_normalized)}</h1>",
    ]
    seen: set[str] = set()
    sorted_rels = sorted(releases, key=lambda r: r.get("published_at", ""))
    for rel in sorted_rels:
        for a in rel["assets"]:
            fname = a.get("name", "")
            if not fname.endswith(_DIST_SUFFIXES):
                continue
            if fname in seen:
                continue
            seen.add(fname)
            url = a.get("url", "")
            if not url:
                continue
            lines.append(
                f'<a href="{html.escape(url)}">{html.escape(fname)}</a><br>'
            )
    lines.append("</body></html>")
    return "\n".join(lines) + "\n"


def render_root_page(repos: list[str]) -> str:
    lines = [
        "<!DOCTYPE html>",
        "<html><head>",
        '<meta name="pypi:repository-version" content="1.0">',
        "<title>Simple Index</title>",
        "</head><body>",
        "<h1>Simple Index</h1>",
    ]
    for repo in sorted(repos):
        n = normalize(repo)
        lines.append(f'<a href="{n}/">{html.escape(n)}</a><br>')
    lines.append("</body></html>")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--out",
        type=Path,
        default=Path("_site/simple"),
        help="Output dir for simple-index HTML (default: _site/simple)",
    )
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    total_assets = 0
    for repo in REPOS:
        n = normalize(repo)
        proj_dir = args.out / n
        proj_dir.mkdir(parents=True, exist_ok=True)
        releases = fetch_releases(repo)
        page = render_project_page(n, releases)
        (proj_dir / "index.html").write_text(page, encoding="utf-8")
        n_assets = sum(
            1
            for r in releases
            for a in r["assets"]
            if a.get("name", "").endswith(_DIST_SUFFIXES)
        )
        total_assets += n_assets
        print(f"  {n}: {len(releases)} releases, {n_assets} dist assets")

    (args.out / "index.html").write_text(
        render_root_page(REPOS), encoding="utf-8"
    )
    print(f"wrote root index → {args.out / 'index.html'}")
    print(f"total assets indexed: {total_assets}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
