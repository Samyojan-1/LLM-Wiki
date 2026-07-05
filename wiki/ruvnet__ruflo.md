# Ruflo

> An agent meta-harness that wraps Claude Code and Codex with multi-agent coordination, persistent memory, and self-learning.

- **Repository:** https://github.com/ruvnet/ruflo
- **Stars:** 62945

## What it is

Ruflo (formerly Claude Flow) is described as "the harness" around coding-agent CLIs — the execution layer that gives an underlying model tools, memory, loops, sandboxes, and coordination so it can work as more than a single-turn assistant. Running `npx ruflo init` adds 100+ specialized agents, swarm coordination, vector-backed memory, and hook-based automation to Claude Code, so tasks are automatically routed, learned from, and coordinated across agents in the background. It can be installed either as a lightweight set of Claude Code plugins (slash commands only) or as the full CLI install with an MCP server, hooks, and a daemon.

## What it's good for

- Coordinating many specialized agents (coder, tester, reviewer, architect, security, etc.) on a single task via swarms
- Giving agents memory that persists across sessions, backed by a vector database (AgentDB/HNSW)
- Letting agents on different machines or organizations securely exchange work via the federation layer
- Running autonomous background workers that trigger automatically (audit, optimize, test-gap detection, etc.)
- Auditing an existing agent setup for security/readiness via the built-in MetaHarness tool

## Key features

- 100+ specialized agents and 60+ commands, installable as Claude Code plugins or a full CLI/MCP setup
- Swarm coordination with hierarchical, mesh, and adaptive topologies plus consensus protocols
- Self-learning via SONA neural patterns, ReasoningBank, and trajectory learning
- Zero-trust agent federation with mTLS/ed25519 identity, PII-stripping, and behavioral trust scoring
- Multi-provider LLM routing (Claude, GPT, Gemini, Cohere, Ollama) with failover
- A self-hostable multi-model web UI (flo.ruv.io) and a goal-oriented action-planning UI (goal.ruv.io)

## Category

orchestration — its core purpose is coordinating multiple specialized agents (swarms, routing, federation) on top of existing coding-agent CLIs, rather than being a single-agent framework or a standalone memory tool.
