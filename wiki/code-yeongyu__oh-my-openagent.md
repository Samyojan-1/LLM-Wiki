# Oh My OpenAgent (OmO)

> A plugin for the OpenCode (and Codex CLI) agent harness that adds a set of specialized subagents, orchestration modes, and developer tooling on top of the base coding agent.

- **Repository:** https://github.com/code-yeongyu/oh-my-openagent
- **Stars:** 64791

## What it is

oh-my-openagent (OmO) is a plugin distributed in two editions: an "Ultimate" edition for OpenCode with the full feature set, and a "Light" edition (also called LazyCodex) that ports a portable subset of components into OpenAI's Codex CLI plugin system. It layers named subagents (Sisyphus as orchestrator, Hephaestus as autonomous worker, Prometheus as planner, plus Oracle, Librarian, Explore), a multi-agent "Team Mode," LSP and AST-grep tooling, and a hash-anchored file-edit mechanism ("Hashline") on top of the underlying harness, aiming to reduce edit errors and let one command (`ultrawork`) drive a task to completion.

## What it's good for

- Users already running OpenCode or Codex CLI who want a pre-configured set of specialist agents (planning, review, debugging, frontend/backend work) instead of building that setup themselves.
- Teams that want multiple agents working in parallel on one task (Team Mode) with a visualized tmux layout.
- Reducing "stale line" edit failures in agentic coding via the Hashline content-hash edit tool.
- Projects wanting auto-generated hierarchical `AGENTS.md` context files (`/init-deep`).
- Users who want to reuse existing Claude Code hooks, commands, skills, and MCP configurations inside OpenCode, since the plugin claims compatibility with that surface.

## Key features

- Named "discipline agents" (Sisyphus, Hephaestus, Prometheus, Oracle, Librarian, Explore) each mapped to specific models and roles.
- Team Mode (opt-in, v4.0): a lead agent coordinates up to 8 parallel team members via dedicated `team_*` tools, with a tmux-based live view; powers bundled skills like `hyperplan` and `security-research`.
- Hash-anchored edit tool ("Hashline"): every read line is tagged with a content hash so edits are rejected if the underlying line changed, avoiding stale-line corruption.
- Built-in LSP tools (goto-definition, references, diagnostics, rename) and AST-grep for pattern-aware code search/rewriting across languages.
- Skill system with skill-embedded MCP servers that load on demand, plus built-in MCPs for web search (Exa), docs (Context7), and GitHub code search (Grep.app).
- Category-based agent-to-model routing (`visual-engineering`, `deep`, `quick`, `ultrabrain`) so subagents automatically get an appropriate model.

## Category

**skills/plugins** — it is installed as a plugin into an existing agent harness (OpenCode or Codex CLI) to add agents, commands, hooks, and MCP-backed skills, rather than being a standalone framework.
