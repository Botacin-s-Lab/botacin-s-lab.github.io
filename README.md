# Botacin's Lab website

Source of https://botacin-s-lab.github.io/, the website of Botacin's Lab at Texas A&M University.

Everything you would want to change (members, papers, talks, news, projects) lives in small text files in [`data/`](data/). You edit a file, open a pull request, and the site rebuilds itself when it is merged. **You do not need to install anything.**

## What do you want to change?

| I want to... | Edit this file | Section below |
|---|---|---|
| Add or update **my card** (photo, bio, links) | [`data/people/members/<your-name>.yml`](data/people/members/) | [Members](#members-phd-visiting-pi) |
| Add a **Master's, undergraduate or alumni** entry | [`data/people/students.yml`](data/people/students.yml) | [Students](#masters-undergraduate-and-alumni-lists) |
| Add a **paper** | [`data/publications.yml`](data/publications.yml) | [Papers](#papers) |
| Add a **talk or presentation** | [`data/talks.yml`](data/talks.yml) | [Talks](#talks) |
| Post **news** | [`data/news.yml`](data/news.yml) | [News](#news) |
| Describe what **I am working on** now | [`data/projects/current/<your-name>.yml`](data/projects/current/) | [Current projects](#current-projects) |
| List a **finished project** (code, data, paper) | [`data/projects/published.yml`](data/projects/published.yml) | [Published projects](#published-projects) |
| Edit **funding** or **join us** text | [`docs/funding/index.md`](docs/funding/index.md), [`docs/join.md`](docs/join.md) | [Text pages](#text-pages) |

Every data file starts with a commented example. Copy an existing entry, change the values, save.

## The 60-second workflow (all in the browser)

1. Open the file you want in GitHub (links above) and click the **pencil icon** (Edit). To make a new file, use **Add file → Create new file** in the right folder.
2. Make your change. Follow the pattern of the entries around it.
3. Click **Commit changes**, choose **Create a new branch and start a pull request**, and open the pull request.
4. Wait for the **Check Site** check on the pull request. Green means the site builds. Red means something is off: click **Details**, and the error names the file and the entry to fix.
5. A lab maintainer merges the pull request. The site updates about a minute later.

Photos: on the GitHub page for the folder `docs/assets/people/`, use **Add file → Upload files**.

## Recipes

Text rules that apply to every file:

- Every entry starts with `- ` (a dash and a space), and its fields are indented two spaces below.
- Put text in double quotes `"like this"`, especially anything with a colon `:`, a `#`, or that starts with `*`, `[` or `&`.
- Use **full URLs** starting with `https://`.
- Text fields accept Markdown: `**bold**`, `*italic*`, `[link text](https://...)`.
- Newest entries go at the top of `publications.yml` and `news.yml`. `talks.yml` sorts itself by date.

### Members (PhD, visiting, PI)

One file per person in `data/people/members/`. To add yourself, create `data/people/members/jane-doe.yml`:

```yaml
name: Jane Doe
group: phd                    # phd, visiting or pi
role: PhD student
since: since Fall 2025
order: 6                      # optional; cards sort by this number, then by name
photo: jane-doe.jpg           # a file you upload to docs/assets/people/
bio: "One or two sentences about your research."
links:                        # keep only the ones you have
  website: https://janedoe.com
  github: https://github.com/janedoe
  scholar: https://scholar.google.com/citations?user=XXXX
  linkedin: https://www.linkedin.com/in/janedoe
  email: jane@tamu.edu
```

Available link names: `website`, `github`, `scholar`, `linkedin`, `twitter`, `orcid`, `youtube`, `email`, `cv`. Any other name is shown as a plain link with that label.

**Photo:** a square-ish JPG or PNG, about 600 pixels wide, uploaded to `docs/assets/people/`. The `photo:` value is just the file name. If you leave `photo:` out, a grey placeholder is shown. If the file name does not match an uploaded file, the build fails and says so.

To update yourself later, edit your own file. When someone leaves, delete their file and add a line for them under `alumni` in `students.yml`.

### Master's, undergraduate and alumni lists

One line per person in [`data/people/students.yml`](data/people/students.yml), inside the right section (`masters`, `undergraduates` or `alumni`, then `current`, `previous`, and so on):

```yaml
  - {name: "Jane Doe", role: "MSc thesis", term: "Fall 2026", notes: "Topic, or [a paper](https://...)"}
```

`name` and `role` are required; `term` and `notes` are optional. When someone finishes, move their line from `current` to `previous` (or `graduated`).

### Papers

Add an entry at the **top** of [`data/publications.yml`](data/publications.yml):

```yaml
- year: 2026
  venue: "ACSAC"
  title: "Full paper title"
  authors: "**Jane Doe**, Other Author, Marcus Botacin."   # **bold** = lab members
  note: "To appear."                                        # optional
  tags: ["malware", "YARA"]                                 # optional
  links:                                                    # optional; any labels
    publisher: https://doi.org/...
    pdf: https://...
    code: https://github.com/...
    data: https://zenodo.org/...
    slides: https://...
    video: https://youtu.be/...
```

The home page shows the 4 newest papers; the Publications page shows all. If a Master's or undergraduate coauthored it, also add the paper to their `notes` in `students.yml`.

### Talks

Add an entry anywhere in [`data/talks.yml`](data/talks.yml). The page sorts by date, newest first:

```yaml
- date: 2026-11-05            # YYYY-MM-DD (the day is optional: 2026-11)
  title: "Talk title"
  venue: "Conference or seminar name, city"
  speaker: "Jane Doe"
  type: "talk"                # optional: talk, invited talk, poster, tutorial, defense
  links:                      # optional
    slides: https://...
    video: https://youtu.be/...
```

### News

Add an item at the **top** of [`data/news.yml`](data/news.yml):

```yaml
- date: "2026-11-05"          # any text works: "2026-11-05", "2026-11", "2026 Fall"
  text: "Jane Doe's paper is accepted at *ACSAC 2026*. [Read it](https://...)"
```

The home page shows the 5 newest items; the News page shows all.

### Current projects

Each PhD student has a file in `data/projects/current/`. Fill in yours:

```yaml
owner: "Jane Doe"
title: "Short project title"
summary: "Two or three sentences: the problem, the approach, where it stands."
links:
  code: https://github.com/...
  paper: https://...
```

Leave `title` and `summary` empty and the page shows a "to be filled in" placeholder. New PhD student: copy an existing file in that folder and change `owner`. When the project is public and has a paper, move it to Published projects and delete the file.

### Published projects

Add an entry to [`data/projects/published.yml`](data/projects/published.yml). It becomes a line in the Published projects list that links straight to the project's own site or repository:

```yaml
- name: ProjectName
  url: https://github.com/Botacin-s-Lab/ProjectName     # or the project's docs site
  summary: "One or two sentences about what it does."
```

### Text pages

Funding, Join us and the HPC Security project are ordinary Markdown pages in `docs/`. Edit them like any text file. To add a new page, create `docs/your-page.md` and list it under `nav:` in [`mkdocs.yml`](mkdocs.yml).

## Preview on your computer (optional)

```bash
python3 -m venv .venv
.venv/bin/pip install -r docs/requirements.txt
.venv/bin/mkdocs serve           # http://127.0.0.1:8000, rebuilds when you save
.venv/bin/mkdocs build --strict  # the same check the pull request runs
```

## How it works

- **`data/`**: all content, as YAML. Edit this.
- **`main.py`**: turns the data into rows and cards, and checks it. Missing required fields and unknown photo names fail the build with a clear message. Edit only to change how something looks.
- **`docs/`**: the pages (mostly a few lines that call `{{ pub_rows(publications) }}` and similar), the stylesheet `docs/stylesheets/extra.css`, and photos in `docs/assets/people/`.
- **`mkdocs.yml`**: navigation, theme and plugins.
- **`.github/workflows/`**: `pr-checks.yml` builds every pull request; `docs.yml` deploys `main` to GitHub Pages.

The site is [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and works on phones, tablets and desktops, in light and dark mode.

## One-time setup (maintainers)

In the repository on GitHub: **Settings → Pages → Build and deployment → Source: GitHub Actions**. Then every merge to `main` that touches `docs/`, `data/`, `main.py` or `mkdocs.yml` redeploys the site.

## Related sites

- [AutoPYara documentation](https://botacin-s-lab.github.io/AutoPYaraPyPI/)
