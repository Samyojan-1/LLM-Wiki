# LLM-Wiki Pipeline

Pipeline that discovers top AI-agent repositories on GitHub and turns their READMEs into a Markdown knowledge vault ("LLM wiki").

## Pipeline shape

find.py -> manifest.json -> download.py (new entries only) -> raw/ -> wiki skill (create | update) -> wiki/

## Layout

- `find.py` — queries the GitHub API, writes `manifest.json` (top ~20 repos).
- `download.py` — reads the manifest, downloads each repo's README into `raw/<owner__repo>/` (README.md + meta.json). Incremental: existing folders are skipped.
- `raw/` — downloaded source data. One folder per repo.
- `wiki/` — the generated Markdown vault. Built ONLY by the wiki-builder skill.
- `.claude/skills/wiki-builder/` — the skill that creates/updates the wiki.

## Rules

- The Python scripts are purely mechanical: GitHub REST API + filesystem only. Never add LLM SDKs, clients, or API calls to them.
- All intelligence (summarizing READMEs into wiki pages) lives in the wiki-builder skill.
- Never hand-edit files in `wiki/` outside the skill workflow.
- The GitHub token comes from the `GITHUB_TOKEN` env var (via `.env`, which is gitignored). Never hardcode secrets.

## Running

- `python find.py` — refresh the manifest.
- `python download.py` — fetch READMEs for new manifest entries.
- Wiki: invoke the `wiki-builder` skill in create or update mode.