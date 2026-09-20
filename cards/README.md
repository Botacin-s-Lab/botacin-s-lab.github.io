# Cards

Everything a person edits on the site lives in this folder, one small file each, so nobody has to touch anyone else's text.

| Folder | Shown on | Edit if you are... |
|---|---|---|
| `phd/<name>.md` | Members page (PhD and visiting PhD cards) | a PhD or visiting PhD student |
| `projects/<name>.md` | Current projects page | a PhD student describing what you are working on |

## Updating your card

1. Put a square photo (about 400 x 400 px, JPG or PNG) in `docs/assets/people/`, e.g. `docs/assets/people/jane-doe.jpg`.
2. Open your file in `cards/phd/` and change the image path from `placeholder.svg` to your photo.
3. Write a two or three line "about" text and replace each `#` link with your real URL. Delete links you do not want. Links left as `#` show dimmed and do nothing.
4. Open a pull request. The site rebuilds when it is merged to `main`.

## Adding a new PhD student

Copy an existing file in `cards/phd/`, edit it, then add one line to `docs/members/index.md` inside the matching grid:

```
--8<-- "cards/phd/your-name.md"
```

Do the same in `cards/projects/` and `docs/projects/current.md` for a project slot.
