# browser-use

> A Python library that lets an LLM-driven agent control a real web browser to complete tasks online.

- **Repository:** https://github.com/browser-use/browser-use
- **Stars:** 102670

## What it is

browser-use makes websites accessible to AI agents by giving an `Agent` object a browser it can drive: navigating pages, reading page content, and taking actions to accomplish a natural-language task. It ships as an open-source Python package (`pip install browser-use` / `uv add browser-use`) that pairs with any LLM (OpenAI, Anthropic, Google, or the project's own `ChatBrowserUse` models), plus an optional CLI and hosted cloud service for scaled, stealth-enabled browser automation. The core idea, per the README, is to give agents a direct, dependable surface for acting in the browser rather than heavily abstracting the browser away.

## What it's good for

- Automating browser-based tasks from a plain-language description, e.g. "fill in this job application" or "put this shopping list into my instacart."
- Building custom agents that need deep code-level browser integration and custom tools.
- Prototyping browser agents locally before moving to production, where the hosted Cloud API handles scaling, proxy rotation, and stealth/anti-bot handling.
- Adding a browser capability to coding agents like Claude Code or Codex via the packaged "skill" and CLI.
- Extending agent behavior with custom tools/actions via the `Tools` API.

## Key features

- `Agent` class that takes a task string and an LLM, then autonomously drives a `BrowserProfile`-configured browser to complete it.
- CLI (`browser-use`) for scripting direct Python-driven browser control, plus an installable "skill" for coding agents.
- `ChatBrowserUse` model wrapper that reaches multiple LLM providers (OpenAI, Anthropic, Google) through one API key, alongside the project's own optimized `bu-*` models.
- Template generator (`uvx browser-use init --template ...`) for minimal, advanced, or tools-focused starter scripts.
- Custom tool/action support via the `Tools` API for extending agent capabilities.
- Optional integration with Browser Use Cloud for remote/stealth browsers, proxy rotation, CAPTCHA handling, and 1000+ third-party integrations.

## Category

**tooling** — it is a library/CLI that equips an LLM agent with a specific capability (browser control) rather than an end-to-end agent framework or orchestration system.
