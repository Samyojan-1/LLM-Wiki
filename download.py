"""Download READMEs for repositories listed in the manifest.

Incremental: a repository whose folder already exists under raw/ is skipped, so re-running only fetches 
entries added since the last run.
"""

import base64
import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

GITHUB_API = "https://api.github.com"
MANIFEST_PATH = Path("manifest.json")
RAW_DIR = Path("raw")


def load_manifest(path: Path) -> list[dict]:
    """Read the manifest file and return its entries."""
    return json.loads(path.read_text())


def repo_dir_name(full_name: str) -> str:
    """Convert 'owner/repo' into a safe folder name like 'owner__repo'."""
    return full_name.replace("/", "__")


def fetch_readme(full_name: str, token: str) -> str:
    """Fetch and decode the README text for one repository."""
    response = requests.get(
        f"{GITHUB_API}/repos/{full_name}/readme",
        headers={"Authorization": f"Bearer {token}"},
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    return base64.b64decode(payload["content"]).decode("utf-8")


def download_entry(entry: dict, token: str) -> None:
    """Download one repository's README and metadata into raw/."""
    target = RAW_DIR / repo_dir_name(entry["full_name"])
    readme_text = fetch_readme(entry["full_name"], token)

    target.mkdir(parents=True)
    (target / "README.md").write_text(readme_text)
    (target / "meta.json").write_text(json.dumps(entry, indent=2) + "\n")


def main() -> None:
    """Download READMEs for all manifest entries not yet in raw/."""
    load_dotenv()
    token = os.environ["GITHUB_TOKEN"]

    entries = load_manifest(MANIFEST_PATH)
    RAW_DIR.mkdir(exist_ok=True)

    downloaded, skipped, failed = 0, 0, 0
    for entry in entries:
        full_name = entry["full_name"]
        target = RAW_DIR / repo_dir_name(full_name)

        if target.exists():
            skipped += 1
            continue

        try:
            download_entry(entry, token)
            print(f"Downloaded: {full_name}")
            downloaded += 1
        except requests.RequestException as error:
            print(f"FAILED: {full_name} ({error})")
            failed += 1

    print(f"\nDone. {downloaded} downloaded, {skipped} skipped, {failed} failed.")


if __name__ == "__main__":
    main()
