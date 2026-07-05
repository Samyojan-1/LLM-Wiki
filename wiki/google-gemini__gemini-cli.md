# Gemini CLI

> An open-source terminal agent that gives direct command-line access to Google's Gemini models.

- **Repository:** https://github.com/google-gemini/gemini-cli
- **Stars:** 105734

## What it is

Gemini CLI is an open-source AI agent that runs in the terminal, providing direct access to Gemini models for code understanding, generation, and task automation. It ships with built-in tools (file operations, shell commands, web fetch, Google Search grounding) and can be extended with MCP servers for custom integrations. It supports several authentication paths — a free tier via personal Google account sign-in, a Gemini API key, or Vertex AI for enterprise use.

## What it's good for

- Querying and editing large codebases from the terminal using natural-language prompts
- Generating new applications from PDFs, images, or sketches via multimodal input
- Automating operational GitHub tasks — PR reviews, issue triage, on-demand help — via the Gemini CLI GitHub Action
- Running non-interactively in scripts or CI pipelines for workflow automation (headless mode, JSON/streaming output)
- Extending capabilities with custom MCP servers, e.g. connecting to databases, Slack, or media-generation tools

## Key features

- Built-in tools: Google Search grounding, file operations, shell commands, web fetching
- MCP (Model Context Protocol) support for custom tool integrations
- Custom context files (GEMINI.md) to tailor behavior per project
- Conversation checkpointing to save/resume sessions, plus token caching
- Multiple output modes: interactive, plain-text non-interactive, JSON, and streaming JSON events
- GitHub Action integration for automated PR reviews, issue triage, and @gemini-cli mentions

## Category

**tooling** — it is a terminal-based agent/CLI application built around a model plus built-in and MCP-extensible tools, rather than a library for constructing custom agents.
