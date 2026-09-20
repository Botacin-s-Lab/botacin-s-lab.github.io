"""Site macros for mkdocs-macros-plugin.

All editable content lives in ``data/`` as small YAML files. The functions
below turn that data into the HTML/Markdown blocks the pages embed, e.g.
``{{ pub_rows(publications) }}``. To change what a page looks like, edit this
file and ``docs/stylesheets/extra.css``; to change *content*, edit ``data/``
only (see the README).

Every loader validates its file and fails the build with a message that names
the file and the entry, so a typo in a YAML file never silently drops a row.
"""

import glob
import html
import os

import yaml

# Link label -> (icon shortcode, display text). Any label not listed here is
# shown with a generic link icon and the label itself.
LINK_STYLES = {
    "website": (":material-web:", "Website"),
    "github": (":fontawesome-brands-github:", "GitHub"),
    "scholar": (":material-school:", "Scholar"),
    "linkedin": (":fontawesome-brands-linkedin:", "LinkedIn"),
    "twitter": (":fontawesome-brands-x-twitter:", "X"),
    "orcid": (":fontawesome-brands-orcid:", "ORCID"),
    "youtube": (":fontawesome-brands-youtube:", "YouTube"),
    "email": (":material-email:", "Email"),
    "cv": (":material-file-account:", "CV"),
}

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


class DataError(Exception):
    """Raised for a malformed data file; the message says what to fix."""


def define_env(env):
    root = env.project_dir
    data_dir = os.path.join(root, "data")
    photo_dir = os.path.join(root, "docs", "assets", "people")

    # ---------------------------------------------------------------- loading

    def read(rel):
        path = os.path.join(data_dir, rel)
        try:
            with open(path, encoding="utf-8") as f:
                return yaml.safe_load(f)
        except yaml.YAMLError as exc:
            raise DataError(f"data/{rel} is not valid YAML: {exc}") from exc

    def require(item, keys, where):
        if not isinstance(item, dict):
            raise DataError(f"{where}: each entry must be a set of 'key: value' lines")
        missing = [k for k in keys if not item.get(k)]
        if missing:
            title = item.get("title") or item.get("name") or item.get("text") or "?"
            raise DataError(
                f"{where} ({str(title)[:50]!r}): missing required field(s): "
                + ", ".join(missing)
            )

    def load_list(rel, keys):
        items = read(rel) or []
        if not isinstance(items, list):
            raise DataError(f"data/{rel} must be a list (each entry starts with '- ')")
        for i, item in enumerate(items, 1):
            require(item, keys, f"data/{rel} entry #{i}")
        return items

    publications = load_list("publications.yml", ["year", "venue", "title", "authors"])
    news = load_list("news.yml", ["date", "text"])
    talks = load_list("talks.yml", ["date", "title", "venue", "speaker"])
    talks.sort(key=lambda t: str(t["date"]), reverse=True)
    published = load_list("projects/published.yml", ["name", "url", "summary"])

    students = read("people/students.yml") or {}
    for group, sections in students.items():
        for section, items in (sections or {}).items():
            for i, item in enumerate(items or [], 1):
                require(item, ["name", "role"],
                        f"data/people/students.yml {group}/{section} entry #{i}")

    def load_dir(rel, keys):
        out = []
        for path in sorted(glob.glob(os.path.join(data_dir, rel, "*.yml"))):
            name = os.path.relpath(path, data_dir)
            item = read(name)
            require(item, keys, f"data/{name}")
            out.append(item)
        return out

    members = load_dir("people/members", ["name", "role", "group"])
    for m in members:
        if m["group"] not in ("phd", "visiting", "pi"):
            raise DataError(f"member {m['name']!r}: group must be phd, visiting or pi")
        if m.get("photo") and not os.path.exists(os.path.join(photo_dir, m["photo"])):
            raise DataError(
                f"member {m['name']!r}: photo {m['photo']!r} not found in docs/assets/people/"
            )
    members.sort(key=lambda m: (m.get("order", 100), m["name"]))
    projects = load_dir("projects/current", ["owner"])

    env.variables["publications"] = publications
    env.variables["news"] = news
    env.variables["talks"] = talks
    env.variables["students"] = students

    # ---------------------------------------------------------------- helpers

    def rel(path):
        """Prefix that makes a docs/-relative path work from the current page."""
        url = env.page.url if getattr(env, "page", None) else ""
        return "../" * len([p for p in url.split("/") if p]) + path

    def esc(value):
        return html.escape(str(value), quote=True)

    def chips(links):
        return " ".join(
            f"[{label}]({url}){{ .chip }}" for label, url in (links or {}).items()
        )

    def link_row(links):
        parts = []
        for label, url in (links or {}).items():
            icon, text = LINK_STYLES.get(label, (":material-link:", str(label).title()))
            if label == "email" and "@" in str(url) and not str(url).startswith("mailto:"):
                url = "mailto:" + url
            parts.append(f"[{icon} {text}]({url})")
        return " · ".join(parts)

    def date_parts(value):
        """Return (year, 'Sep 16') for an ISO date like 2026-09-16."""
        text = str(value)
        bits = text.split("-")
        year = bits[0]
        if len(bits) >= 2 and bits[1].isdigit() and 1 <= int(bits[1]) <= 12:
            label = MONTHS[int(bits[1]) - 1]
            if len(bits) >= 3 and bits[2].isdigit():
                label += f" {int(bits[2])}"
            return year, label
        return year, ""

    # ----------------------------------------------------------------- macros

    @env.macro
    def pub_rows(items, ids=True):
        seen, out = set(), []
        for p in items:
            year = str(p["year"])
            row_id = ""
            if ids and year not in seen:
                row_id = f' id="{esc(year)}"'
                seen.add(year)
            tags = "".join(f'<span class="tag">{esc(t)}</span>' for t in p.get("tags", []))
            note = f" {p['note']}" if p.get("note") else ""
            out.append(
                f'<div class="pub-row"{row_id} markdown>\n'
                f'<div class="pub-meta" markdown>\n'
                f'<span class="pub-year">{esc(year)}</span>\n'
                f'<span class="mono-label">{esc(p["venue"])}</span>\n'
                f"</div>\n"
                f'<div class="pub-main" markdown>\n'
                f'**{p["title"]}**\n\n'
                f'{p["authors"]}{note}\n\n'
                f"{tags}\n"
                f"</div>\n"
                f'<div class="pub-links" markdown>\n'
                f'{chips(p.get("links"))}\n'
                f"</div>\n"
                f"</div>\n"
            )
        return "\n".join(out)

    @env.macro
    def talk_rows(items):
        out = []
        for t in items:
            year, day = date_parts(t["date"])
            kind = f'<span class="tag">{esc(t["type"])}</span>' if t.get("type") else ""
            out.append(
                f'<div class="pub-row" markdown>\n'
                f'<div class="pub-meta" markdown>\n'
                f'<span class="pub-year">{esc(year)}</span>\n'
                f'<span class="mono-label">{esc(day)}</span>\n'
                f"</div>\n"
                f'<div class="pub-main" markdown>\n'
                f'**{t["title"]}**\n\n'
                f'{t["speaker"]} · {t["venue"]}\n\n'
                f"{kind}\n"
                f"</div>\n"
                f'<div class="pub-links" markdown>\n'
                f'{chips(t.get("links"))}\n'
                f"</div>\n"
                f"</div>\n"
            )
        return "\n".join(out)

    @env.macro
    def news_rows(items):
        return "\n".join(
            f'<div class="news-row" markdown>\n'
            f'<span class="news-date">{esc(n["date"])}</span>\n'
            f'<div markdown>\n{n["text"]}\n</div>\n'
            f"</div>\n"
            for n in items
        )

    @env.macro
    def member_cards(group):
        cards = []
        for m in members:
            if m["group"] != group:
                continue
            photo = m.get("photo") or ""
            src = rel("assets/people/" + (photo or "placeholder.svg"))
            role = m["role"] + (f" · {m['since']}" if m.get("since") else "")
            links = link_row(m.get("links"))
            bio = m.get("bio") or "_About: to be added._"
            cards.append(
                f'<div class="member-card" markdown>\n'
                f'![Photo of {m["name"]}]({src}){{ .member-photo }}\n'
                f'### {m["name"]}\n'
                f'<span class="member-role">{esc(role)}</span>\n\n'
                f"{bio}\n\n"
                + (f'<div class="member-links" markdown>\n{links}\n</div>\n' if links else "")
                + "</div>\n"
            )
        return '<div class="member-grid" markdown>\n\n' + "\n".join(cards) + "\n</div>\n"

    @env.macro
    def people_table(items, columns=("Name", "Role", "Term", "Notes")):
        if not items:
            return "_No entries yet._\n"
        keys = ("name", "role", "term", "notes")
        lines = ["| " + " | ".join(columns) + " |", "|" + "---|" * len(columns)]
        for p in items:
            cells = [str(p.get(k, "") or "").replace("|", "\\|") for k in keys]
            lines.append("| " + " | ".join(cells) + " |")
        return "\n".join(lines) + "\n"

    @env.macro
    def project_slots():
        out = []
        for p in projects:
            title = p.get("title") or ""
            summary = p.get("summary") or ""
            links = p.get("links") or {}
            if not links and not title:
                # Blank template: dimmed placeholder links until the owner fills it in.
                link_line = ("[:material-github: Code](#) · "
                             "[:material-file-document-outline: Draft or paper](#) · "
                             "[:material-database: Data](#)")
            else:
                link_line = link_row(links)
            out.append(
                '<div class="project-slot" markdown>\n'
                f'### {p["owner"]}\n\n'
                + ('' if title else '<span class="pill">to be filled in</span>\n\n')
                + f'**Project:** {title or "_Title to be added._"}\n\n'
                + f'**Summary:** {summary or "_Two or three sentences on the problem, the approach and where it stands._"}\n\n'
                + (f"{link_line}\n" if link_line else "")
                + "</div>\n"
            )
        return "\n".join(out)

    @env.macro
    def published_cards():
        out = []
        for p in published:
            icon = p.get("icon", ":material-package-variant-closed:")
            out.append(
                f'<div markdown>\n'
                f'### {icon} {p["name"]}\n'
                f'{p["summary"]}\n\n'
                f'[{p["name"]} :material-arrow-right:]({p["url"]})\n'
                f"</div>\n"
            )
        return '<div class="feature-grid" markdown>\n\n' + "\n".join(out) + "\n</div>\n"
