# Letta (formerly MemGPT)

> A platform for building stateful AI agents with advanced memory that persists and improves over time.

- **Repository:** https://github.com/letta-ai/letta
- **Stars:** 23658

## What it is

Letta addresses the problem of agents losing context between interactions by giving them persistent, advanced memory that can learn and self-improve over time. It offers two entry points: the Letta Agent CLI/desktop app for running agents locally or via channels like Slack, and the Letta Agent SDK (TypeScript) for embedding stateful agents into other applications. Agents can run on Letta's cloud (Constellation), fully locally, or against a self-hosted App Server, and are model-agnostic across providers like Anthropic, OpenAI, and zAI. Note this specific repository is the legacy Letta V1 API server; active agent development has moved to a separate Letta Agent repo.

## What it's good for

- Running a memory-equipped coding/task agent locally in a terminal, desktop app, or Slack
- Embedding a stateful agent with persistent memory into a custom application via the SDK
- Building agents that need to remember information across sessions rather than starting fresh each time
- Using pre-built skills and subagents for continual learning without building memory infrastructure from scratch

## Key features

- Persistent, advanced agent memory that carries over between sessions and improves over time
- Letta Agent CLI supporting installable skills and subagents
- TypeScript Agent SDK for building stateful agents into applications, with streaming conversation support
- Model-agnostic: works with Anthropic, OpenAI, zAI, and other providers
- Multiple deployment options: Letta's cloud (Constellation), fully local, or self-hosted App Server
- Legacy V1 SDKs (TypeScript and Python) still available for direct API access

## Category

memory — its core purpose is giving agents advanced, persistent memory that carries across sessions and self-improves over time.
