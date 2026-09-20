# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

The Botacin's Lab website (Texas A&M University), served at https://botacin-s-lab.github.io/. It is a MkDocs Material site with the `mkdocs-macros-plugin`, deliberately matching the AutoPYara docs site (`Botacin-s-Lab/AutoPYaraPyPI`, served under the same domain at `/AutoPYaraPyPI/`): same indigo/teal palette and Inter font. The layout follows https://t3slab.github.io/ (mono labels, key-facts row, PI block, ruled rows), with our own colours.

The goal is that lab members update the site by editing small YAML files in the browser and opening a pull request. Keep that workflow simple; `README.md` is the contributor guide and must stay in sync with the data schemas below.

## Commands

```bash
python3 -m venv .venv && .venv/bin/pip install -r docs/requirements.txt
.venv/bin/mkdocs serve                             # live preview at http://127.0.0.1:8000, rebuilds when data/ changes
.venv/bin/mkdocs build --strict --site-dir _site   # what CI runs; warnings and data errors fail the build
```

CI: `.github/workflows/pr-checks.yml` builds every pull request; `.github/workflows/docs.yml` deploys `main` to GitHub Pages (Settings, Pages, Source must be "GitHub Actions").

## Architecture

- **`data/` holds all content, `main.py` renders it, `docs/` pages call the renderers.** Pages contain lines like `{{ pub_rows(publications) }}`; `main.py` (`define_env`) loads and validates the YAML and defines the macros (`pub_rows`, `talk_rows`, `news_rows`, `member_cards`, `people_table`, `project_slots`, `published_list`). Validation raises `DataError` naming the file and entry, so contributors get a clear failure instead of a silently missing row.
- Data files: `publications.yml` and `news.yml` (newest first, file order), `talks.yml` (sorted by date), `people/members/*.yml` (one card per PI/PhD/visiting person, sorted by `order`), `people/students.yml` (Master's, undergraduate, alumni rows in sections), `projects/current/*.yml` (one slot per PhD student), `projects/published.yml` (a plain list of links out, e.g. AutoPYara to its docs site). Each file starts with a commented example; keep those in sync with `main.py`.
- Macro output is Markdown plus `md_in_html` HTML (`<div ... markdown>`), so data strings may contain Markdown. Internal image paths are made page-relative by `rel()` in `main.py`; links inside data should be full `https://` URLs.
- The home page reuses the same data: `publications[:4]` and `news[:5]`.
- `docs/stylesheets/extra.css` holds all custom styling, including the mobile rules (`@media (max-width: 40em)`); the site was checked at 375px with no horizontal overflow on any page. `docs/javascripts/members.js` adds the per-section entry counts on the Members page.
- `overrides/partials/source.html` replaces Material's GitHub repo widget in the header with a "Join the lab" button (`repo_url` stays set so "edit this page" links work).
- Photos live in `docs/assets/people/`; a member's `photo:` must name a file there (checked at build time), otherwise `placeholder.svg` is used.

## Content conventions

- Publications list only papers with a current or former lab member as an author, not the PI's full record. Lab members are `**bold**` in the authors string.
- Member names and terms originally came from the PI's site (https://marcusbotacin.github.io/); `lab-index.md` is the raw snapshot from 2026-09-20 and is not built into the site.
- Do not put a logo in the landing hero and do not add a stats strip; the owner rejected both.
