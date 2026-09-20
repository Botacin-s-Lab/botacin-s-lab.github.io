# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

The Botacin's Lab website (Texas A&M University), served at https://botacin-s-lab.github.io/. It is a MkDocs Material site, deliberately matching the AutoPYara docs site (`Botacin-s-Lab/AutoPYaraPyPI`, served under the same domain at `/AutoPYaraPyPI/`): same indigo/teal palette, Inter font, hero and `feature-grid` styles.

## Commands

```bash
python3 -m venv .venv && .venv/bin/pip install -r docs/requirements.txt
.venv/bin/mkdocs serve                             # live preview at http://127.0.0.1:8000
.venv/bin/mkdocs build --strict --site-dir _site   # what CI runs; warnings fail the build
```

CI (`.github/workflows/docs.yml`) builds and deploys on pushes to `main` that touch `docs/**`, `cards/**`, `mkdocs.yml` or the workflow. Repo Settings, Pages, Source must be "GitHub Actions".

## Structure

- `mkdocs.yml`: nav, theme and extensions. Adding a page means adding it to `nav` here.
- `docs/`: the pages. `docs/stylesheets/extra.css` holds all custom styling.
- `cards/`: **content that individual students own, outside `docs/`**. `cards/phd/<slug>.md` is one PhD or visiting-PhD member card; `cards/projects/<slug>.md` is that student's slot on the Current projects page. They are pulled into `docs/members/index.md` and `docs/projects/current.md` with `--8<-- "cards/..."` lines (`pymdownx.snippets`, `base_path: ["."]`, `check_paths: true`). A card that is not included by such a line does not appear, and an include of a missing file fails the build. See `cards/README.md` for the student-facing instructions.
- Placeholders: links still set to `#` in a card are dimmed and inert by CSS (`a[href="#"]`). Photos default to `docs/assets/people/placeholder.svg`.

## Content conventions

- Pages: Home, Members (one page: PI, PhD cards, visiting PhD, Master's and undergraduate tables, alumni), Publications, Projects (Current: HPC Security plus per-PhD slots; Published: a card and nav entry per finished project that link straight to the project's own site, AutoPYara first (https://botacin-s-lab.github.io/AutoPYaraPyPI/)), Funding, News, Join us.
- The layout follows https://t3slab.github.io/ (mono labels, key-facts row, stats row, PI block, ruled rows for publications and news); colours and fonts are the Material indigo/teal theme, not theirs.
- `docs/index.md` reuses the newest rows of `docs/publications/index.md` and `docs/news/index.md` through snippet markers (`<!-- --8<-- [start:latest] -->` ... `[end:latest]`). Keep the newest entries inside those markers, and use absolute URLs for internal links inside marked rows, because MkDocs rewrites relative links against the including page.
- `docs/javascripts/members.js` adds the per-section entry counts on the Members page; it runs via `document$` because of instant navigation.
- Publications are lab papers only, meaning papers with a current or former lab member as an author. Not the PI's full record.
- Member names and terms come from the PI's site (https://marcusbotacin.github.io/); `lab-index.md` is the raw snapshot from 2026-09-20 and is not built into the site.
- Links between pages use the `.md` path (MkDocs validates them). Publications rows carry ids `#2026`, `#2025`, `#2021`, `#2020`, `#2019` on the first row of each year.
