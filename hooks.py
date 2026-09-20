"""MkDocs hook: list every published project in the navigation.

Each entry in data/projects/published.yml becomes a menu item under
Projects -> Published projects that links straight to the project's own site.
This keeps the menu in sync with the data file, so adding a project needs no
change to mkdocs.yml.
"""

import os

import yaml


def on_config(config):
    path = os.path.join(os.path.dirname(config["config_file_path"]), "data", "projects", "published.yml")
    with open(path, encoding="utf-8") as f:
        projects = yaml.safe_load(f) or []

    for top in config["nav"]:
        if not (isinstance(top, dict) and "Projects" in top):
            continue
        children = top["Projects"]
        for i, child in enumerate(children):
            if isinstance(child, dict) and "Published projects" in child:
                index_page = child["Published projects"]
                children[i] = {
                    "Published projects": [index_page]
                    + [{p["name"]: p["url"]} for p in projects if p.get("name") and p.get("url")]
                }
    return config
