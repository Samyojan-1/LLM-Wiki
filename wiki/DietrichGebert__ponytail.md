# Ponytail

> A Claude Code / multi-agent-host plugin that pushes coding agents to write the minimal amount of code needed, rather than over-engineering solutions.

- **Repository:** https://github.com/DietrichGebert/ponytail
- **Stars:** 73656

## What it is

Ponytail addresses the tendency of AI coding agents to over-build simple requests (for example, installing a library and writing a wrapper component for what could be a single native HTML element). It injects a ruleset — a decision "ladder" — that the agent checks before writing code: does this need to exist, is it already in the codebase, does the standard library do it, does a native platform feature do it, is a dependency already installed, can it be one line, and only then write the minimum needed. It ships as a skill/plugin/hook set for many agent hosts (Claude Code, Codex, Gemini CLI, Hermes Agent, OpenCode, and others), plus static rule files for instruction-only tools like Cursor and Copilot.

## What it's good for

- Reducing lines of code, token usage, and cost on agentic coding sessions without disabling safety checks.
- Auditing an existing diff or repository for signs of over-engineering (`/ponytail-review`, `/ponytail-audit`).
- Tracking deferred shortcuts so they aren't silently forgotten (`/ponytail-debt`).
- Adding a "keep it minimal" always-on rule to coding agents that only support static instruction files (Cursor, Windsurf, Copilot, Kiro).

## Key features

- A 7-rung decision ladder (YAGNI check, reuse, stdlib, native platform feature, existing dependency, one-liner, minimal implementation) applied after the agent has read and understood the affected code.
- Adjustable intensity levels (`lite`/`full`/`ultra`/`off`) via the `/ponytail` command or a config file/env var.
- Companion commands: `/ponytail-review`, `/ponytail-audit`, `/ponytail-debt`, `/ponytail-gain`, `/ponytail-help`.
- Preserves validation, error handling, security, and accessibility — the ladder is only about avoiding unnecessary code.
- Benchmarked on real agentic Claude Code sessions, reporting reductions in lines of code, tokens, cost, and time versus a no-skill baseline.
- Ships adapters/install paths for over a dozen different agent hosts (Claude Code, Codex, Copilot CLI, Gemini CLI, Hermes Agent, OpenCode, Devin CLI, and more).

## Category

skills/plugins — it is distributed and installed as a skill/plugin (and static rule files) for AI coding agents, not a standalone application or framework.
