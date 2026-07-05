# Hermes Agent

> A self-improving AI agent, built by Nous Research, that can be run from a terminal or messaging platforms and learns from experience over time.

- **Repository:** https://github.com/NousResearch/hermes-agent
- **Stars:** 209070

## What it is

Hermes Agent is an agent runtime with what the README calls a "closed learning loop": it creates and refines skills from experience, nudges itself to persist memory, searches its own past conversations, and builds a model of the user across sessions (via Honcho dialectic user modeling). It is provider-agnostic — it can be pointed at Nous Portal, OpenRouter, OpenAI, or a custom endpoint — and it runs from a full terminal UI or as a gateway reachable from Telegram, Discord, Slack, WhatsApp, Signal, or email.

## What it's good for

- Running a persistent personal AI agent that remembers context and improves its own skills over repeated use, rather than starting fresh each session.
- Interacting with an agent from chat platforms (Telegram, Discord, etc.) instead of only a local terminal.
- Automating recurring work with a built-in cron scheduler (daily reports, nightly backups, weekly audits) delivered to a chosen platform.
- Running the agent remotely on low-cost or serverless infrastructure (VPS, Daytona, Modal) that idles cheaply between sessions.
- Migrating an existing OpenClaw setup (memories, skills, config, API keys) into Hermes via `hermes claw migrate`.

## Key features

- Agent-curated memory with periodic nudges, autonomous skill creation and self-improvement, and FTS5 session search with LLM summarization for cross-session recall.
- Single gateway process serving a terminal UI plus Telegram, Discord, Slack, WhatsApp, Signal, and email, including voice-memo transcription.
- Model-agnostic: switch providers/models with `hermes model`, including Nous Portal, OpenRouter, OpenAI, or custom endpoints.
- Subagent delegation for parallel workstreams, and Python-scriptable tool calls via RPC.
- Six terminal/execution backends (local, Docker, SSH, Singularity, Modal, Daytona), with serverless hibernate-and-wake persistence on Daytona/Modal.
- Compatible with the agentskills.io open skills standard, and supports MCP servers for extended tool capability.

## Category

orchestration — it coordinates memory, skills, scheduled tasks, subagents, and multiple messaging front-ends through a single gateway process, rather than being a library for building one custom agent.
