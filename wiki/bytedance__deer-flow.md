# DeerFlow

> An open-source "super agent harness" that runs long, multi-step agent tasks — research, coding, content creation — using sandboxes, memory, skills, and coordinated sub-agents.

- **Repository:** https://github.com/bytedance/deer-flow
- **Stars:** 76074

## What it is

DeerFlow (Deep Exploration and Efficient Research Flow) started as a Deep Research framework and was rewritten from scratch as version 2.0 into a general-purpose agent harness. It is built on LangGraph and LangChain and provides a lead agent that can plan, spawn parallel sub-agents, execute code and shell commands in a sandboxed filesystem, load "skills" (Markdown workflow modules) on demand, and retain long-term memory across sessions. It's designed to handle tasks that take minutes to hours, not just single-turn Q&A, and is deployed via Docker or local dev services with a web UI, TUI, and embedded Python client.

## What it's good for

- Long-horizon research tasks that fan out into many sub-agents (e.g., research a topic from a dozen angles and converge on a report).
- Generating multi-format deliverables: reports, slide decks, web pages, dashboards, images/video, from a single task description.
- Running agent workflows headlessly via its terminal workbench (TUI) or embedded `DeerFlowClient`, without needing the full web stack.
- Receiving and responding to tasks from messaging platforms (Telegram, Slack, Feishu/Lark, WeChat, WeCom, DingTalk).
- Scheduling recurring or one-off agent runs (cron/once) directly in the workspace.

## Key features

- Skills & Tools system: Markdown-defined workflow modules loaded progressively (only when needed) to keep context lean, plus custom tools via MCP servers or Python functions.
- Sub-agent orchestration: the lead agent spawns scoped, parallel sub-agents with isolated context that report back structured results.
- Sandbox & filesystem: each task gets its own execution environment (local, Docker, or Kubernetes-via-provisioner) with upload/workspace/output directories.
- Long-term memory: builds a persistent profile of user preferences and context across sessions, stored locally.
- Session Goals (`/goal`) that keep a thread working toward a stated completion condition across multiple turns.
- Observability integrations with LangSmith and Langfuse, plus a Claude Code integration skill (`claude-to-deerflow`) for driving DeerFlow from the terminal.

## Category

**orchestration** — its defining feature is coordinating a lead agent, parallel sub-agents, sandboxed execution, and memory/skills to complete complex multi-step tasks, rather than being a single-purpose tool or plugin pack.
