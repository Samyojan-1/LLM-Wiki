# ECC

> A large collection of agents, skills, hooks, and rules that installs into Claude Code (and other AI coding harnesses) to make coding agents more effective and consistent.

- **Repository:** https://github.com/affaan-m/ECC
- **Stars:** 225912

## What it is

ECC ("the agent harness operating system") is a Claude Code plugin — plus manual-install components — that packages specialized subagents, workflow skills, always-on rules, and lifecycle hooks for agentic coding work. Rather than a single tool, it's a configuration and workflow layer: agents for planning, code review, build-error resolution, and security auditing; skills covering language-specific patterns, TDD, deployment, and business/content workflows; hooks for memory persistence across sessions and continuous learning from past sessions. It targets Claude Code, Codex, Cursor, OpenCode, Gemini, Zed, and GitHub Copilot.

## What it's good for

- Bootstrapping a coding agent (Claude Code, Codex, Cursor, etc.) with a consistent set of review, planning, and testing workflows across a team or project.
- Adding language-specific rules and skills (TypeScript, Python, Go, Java, Kotlin, Rust, PHP, Swift, and more) so an agent follows established idioms per stack.
- Running automated security scans on agent-generated code via the bundled AgentShield tool.
- Persisting context/memory across agent sessions instead of starting from scratch each time.
- Auto-extracting reusable "instincts"/skills from past agent sessions (continuous learning).

## Key features

- 60+ specialized subagents (planner, architect, tdd-guide, code-reviewer, security-reviewer, build-error-resolvers per language, etc.) for delegation.
- Large skills library covering coding standards, TDD, security review, deployment patterns, database migrations, and niche framework patterns (Django, Laravel, Spring Boot, Quarkus).
- Hook system (`hooks/hooks.json`) for session-start/session-end memory persistence, pre-compaction state saving, and strategic-compaction suggestions.
- AgentShield — a bundled security auditor that scans agent-authored code and can auto-fix safe issues.
- Continuous Learning v2 — extracts confidence-scored "instincts" from sessions and can evolve them into new skills.
- Cross-harness install paths (plugin install, manual `install.sh`/`install.ps1`, npx installer) with profiles (minimal, core, full) and runtime controls like `ECC_HOOK_PROFILE`.

## Category

**skills/plugins** — it is distributed and consumed as a Claude Code plugin (and equivalent packages for other harnesses) made up of agents, skills, hooks, and rules rather than a standalone framework or runtime.
