# Claude-Mem

> A plugin that gives Claude Code (and similar agents) persistent memory across sessions by compressing and re-injecting past context.

- **Repository:** https://github.com/thedotmack/claude-mem
- **Stars:** 85789

## What it is

Claude-Mem addresses the problem that coding-agent sessions normally lose all context once they end. It hooks into the agent's lifecycle (session start, prompt submit, tool use, stop, session end) to automatically capture what the agent did, compress those observations with AI into semantic summaries, and store them in a local SQLite database plus a Chroma vector database for hybrid semantic + keyword search. On future sessions, relevant past context is automatically injected back in, and a `mem-search` skill plus MCP tools let the agent (or the user) query project history directly. It installs as a Claude Code plugin (or via an OpenClaw/Antigravity/OpenCode integration) and runs a local worker service with a web viewer UI.

## What it's good for

- Keeping continuity of project knowledge across multiple, disconnected Claude Code sessions
- Searching past sessions in natural language for things like "the authentication bug we fixed last week"
- Reviewing a real-time stream of what an agent has done via the local web viewer (localhost:37777)
- Excluding sensitive information from stored memory using `<private>` tags
- Running the same persistent-memory layer across other agent tools (OpenClaw, Codex, Gemini, Copilot, OpenCode) via its multi-IDE install support

## Key features

- 5 lifecycle hooks (SessionStart, UserPromptSubmit, PostToolUse, Stop, SessionEnd) driving automatic capture, with no manual intervention required
- 3-layer MCP search workflow (`search` → `timeline` → `get_observations`) designed for roughly 10x token savings versus fetching full details upfront
- SQLite database for sessions/observations/summaries plus a Chroma vector database for hybrid semantic + keyword search
- Local worker service (managed by Bun) exposing an HTTP API and web viewer UI on port 37777
- Configurable modes (e.g., `code`, `code--zh`, `code--ja`) controlling both workflow behavior and the language of generated observations
- A beta channel with experimental features such as "Endless Mode," toggleable from the web viewer

## Category

memory — its entire purpose is capturing, compressing, storing, and re-injecting an agent's session context so that memory persists across sessions.
