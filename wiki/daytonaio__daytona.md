# Daytona

> Secure, elastic cloud infrastructure for spinning up isolated sandboxes to run AI-generated code.

- **Repository:** https://github.com/daytonaio/daytona
- **Stars:** 72303

## What it is

Daytona is a runtime for executing AI-generated code inside secure, isolated "sandboxes" — full composable computers with their own kernel, filesystem, network stack, and allocated vCPU/RAM/disk. Sandboxes start in under 90ms, run Python, TypeScript, and JavaScript, and are built on OCI/Docker compatibility with massive parallelization and persistence via stateful snapshots. Agents and developers interact with sandboxes through SDKs, a REST API, and a CLI. Note: per the README, this repository is no longer actively maintained as of June 2026 — development moved to a private codebase, though the code remains public to use and fork.

## What it's good for

- Running AI-agent-generated code in an isolated, secure environment instead of on a local or shared machine
- Building agent architectures that need persistent, stateful execution across sessions (via snapshots)
- Programmatic sandbox management from application code using SDKs in Python, TypeScript, Ruby, Go, or Java
- Giving agents filesystem operations, process/code execution, git operations, and computer-use capabilities
- Organizations standardizing sandbox access and governance (dashboard, SSH/VNC, audit logs)

## Key features

- Sandboxes: isolated full computers with dedicated kernel/filesystem/network, spinning up in under 90ms
- Agent tools: process & code execution, filesystem operations, LSP, computer use, MCP server, git operations
- Human tools: dashboard, web terminal, SSH/VNC/VPN access, preview proxy
- Platform controls: organizations, API keys, usage limits, billing, audit logs
- Client SDKs for Python, TypeScript, Ruby, Go, and Java, plus a CLI and REST API
- Declarative builder and stateful snapshots for persistent environments

## Category

**tooling** — it provides infrastructure/runtime tooling (sandboxed compute environments and their SDK/API/CLI surface) for executing and managing agent-generated code, rather than a framework for building agent logic itself.
