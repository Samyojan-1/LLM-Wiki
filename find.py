"""Discover top AI-agent repositories on GitHub and write them to a manifest.

Runs several targeted searches (frameworks, memory, orchestration, ...),
merges the results, deduplicates them, and keeps the top N by stars.
"""

import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

GITHUB_API = "https://api.github.com/search/repositories"
MANIFEST_PATH = Path("manifest.json")
TOP_N = 20

# Multiple queries so we cover the sub-areas the task mentions,
# not just whatever happens to carry one topic tag.
QUERIES = [
    "topic:ai-agents",
    "topic:llm-agents",
    "ai agent framework in:name,description",
    "llm orchestration in:name,description",
    "agent memory llm in:name,description",
]


def fetch_top_repos(query: str, token: str, per_page: int = 20) -> list[dict]:
    """Return the most-starred repositories matching one search query."""
    response = requests.get(
        GITHUB_API,
        params={"q": query, "sort": "stars", "order": "desc", "per_page": per_page},
        headers={"Authorization": f"Bearer {token}"},
        timeout=30,
    )
    response.raise_for_status()  # crash loudly if GitHub returned an error
    return response.json()["items"]


def build_manifest_entries(repos: list[dict]) -> list[dict]:
    """Deduplicate raw API results and reduce them to the fields we keep."""
    seen: dict[str, dict] = {}
    for repo in repos:
        seen[repo["full_name"]] = {
            "full_name": repo["full_name"],
            "html_url": repo["html_url"],
            "description": repo["description"],
            "stars": repo["stargazers_count"],
            "default_branch": repo["default_branch"],
        }
    entries = sorted(seen.values(), key=lambda e: e["stars"], reverse=True)
    return entries[:TOP_N]


def write_manifest(entries: list[dict], path: Path) -> None:
    """Write manifest entries to disk as readable, human-editable JSON."""
    path.write_text(json.dumps(entries, indent=2) + "\n")


def main() -> None:
    """Run all searches and write the manifest."""
    load_dotenv()
    token = os.environ["GITHUB_TOKEN"]

    all_repos: list[dict] = []
    for query in QUERIES:
        print(f"Searching: {query}")
        all_repos.extend(fetch_top_repos(query, token))

    entries = build_manifest_entries(all_repos)
    write_manifest(entries, MANIFEST_PATH)
    print(f"Wrote {len(entries)} repositories to {MANIFEST_PATH}")


if __name__ == "__main__":
    main()