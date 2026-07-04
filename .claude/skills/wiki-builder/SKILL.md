---
name: wiki-builder
description: Build or update the Markdown wiki vault in wiki/ from the raw repository data in raw/. Use when asked to create the wiki from scratch (create mode) or to add pages for newly downloaded repositories (update mode).
---

# Wiki Builder

Turn raw GitHub repository data into an Obsidian-style Markdown vault: one page per repository plus an index page.

## Inputs

- `raw/` contains one folder per repository, named `owner__repo`, each with:
  - `README.md` — the repository's README.
  - `meta.json` — metadata: full_name, html_url, description, stars, default_branch.

## Outputs

- `wiki/<owner__repo>.md` — one page per repository (filename matches the raw/ folder name exactly).
- `wiki/index.md` — the vault's entry point, linking every page.

## Modes

Determine the mode from the user's request:

- **create** — build the vault from scratch. Process every folder in `raw/`. Overwrite anything already in `wiki/`.
- **update** — list folders in `raw/`, list pages in `wiki/`, and process ONLY repositories that have a raw/ folder but no wiki page. Do not modify or regenerate existing pages. Add the new pages to `index.md`, keeping its existing structure and sorting.

## Page template

Each repository page must follow exactly this structure:

    # <Repo display name>

    > One-sentence plain-language summary of what this project is.

    - **Repository:** <html_url>
    - **Stars:** <stars>

    ## What it is

    2–4 sentences explaining the project in plain language: the problem it addresses and the approach it takes.

    ## What it's good for

    3–5 bullet points of concrete use cases — when someone would reach for this tool.

    ## Key features

    3–6 bullet points of its main capabilities, drawn from the README.

    ## Category

    One of: framework | memory | skills/plugins | orchestration | tooling | other — with a short justification.

## Index template

`wiki/index.md` groups pages by Category, each entry as:

    - [[<owner__repo>]] — <one-line summary>

Use Obsidian-style [[wikilinks]] (the filename without .md).

## Writing rules

- Base every page ONLY on that repo's README.md and meta.json. Do not use outside knowledge about the project; if the README is thin, say what can be said and keep the page short rather than inventing details.
- Write for a technical reader who has never seen the project before.
- No marketing language; plain, factual tone.
- Keep each page under ~60 lines.

## Verification

After writing, confirm: every folder in raw/ has a matching page in wiki/ (create mode) or every previously-missing one now does (update mode), and index.md links every page. Report counts: pages created, pages skipped.