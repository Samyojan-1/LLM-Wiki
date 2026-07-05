# AnythingLLM

> An all-in-one, self-hostable application for chatting with your documents and running AI agents, configurable with a wide range of LLM, embedding, and vector-database providers.

- **Repository:** https://github.com/Mintplex-Labs/anything-llm
- **Stars:** 62563

## What it is

AnythingLLM is a private, "ChatGPT-like" application that lets a user connect an LLM provider (local or cloud), ingest documents, and chat with them, with multi-user support and built-in AI agents. It is a monorepo made of a Vite/React frontend, a Node.js/Express server that handles vector-database and LLM interactions, a document-collector service, and Docker deployment tooling, plus submodules for a browser extension and an embeddable chat widget.

## What it's good for

- Running a private, local-first chat-with-your-documents assistant without depending on a third-party hosted service.
- Standing up a multi-user AI chat instance with per-user access control (Docker version).
- Building no-code AI agent flows or giving agents web-browsing and tool capabilities inside a workspace.
- Embedding an AI chat widget on a website, or using the desktop app or browser extension.
- Integrating with a specific combination of LLM provider, embedding model, and vector database already used elsewhere.

## Key features

- Broad provider support: dozens of LLM providers (OpenAI, Anthropic, Azure, Bedrock, Gemini, Ollama, and more), embedding models, TTS/STT options, and vector databases (LanceDB default, plus Pinecone, Chroma, Weaviate, Qdrant, Milvus, and others).
- Built-in AI agents with web browsing, a no-code agent-flow builder, and MCP compatibility.
- Dynamic model routing, scheduled/cron tasks with full agent capabilities, and "intelligent tool selection" to cut token usage.
- Multi-user support with permissioning (Docker version), and a full developer API for custom integrations.
- Multiple document type ingestion (PDF, TXT, DOCX, etc.) with source citations in the chat UI.
- Optional anonymous telemetry (can be disabled), plus companion mobile app, browser extension, and embeddable widget products.

## Category

tooling — it is a ready-to-deploy application/tool for document chat and agent workflows, rather than a library for building custom agents.
