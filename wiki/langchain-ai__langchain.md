# LangChain

> A Python framework for building agents and LLM-powered applications from interoperable components.

- **Repository:** https://github.com/langchain-ai/langchain
- **Stars:** 140902

## What it is

LangChain is a framework for building agents and LLM-powered applications. It provides a standard interface for chat models, embeddings, and vector stores, so developers can chain together interoperable components and third-party integrations instead of writing bespoke glue code, while keeping the option to swap models as the underlying technology evolves. The README positions it as the base layer of a larger ecosystem: LangGraph for lower-level agent orchestration and Deep Agents for higher-level, batteries-included agent patterns such as planning, subagents, and filesystem use.

## What it's good for

- Building LLM applications that need to swap or compare model providers without rewriting integration code
- Rapidly prototyping chains and workflows using modular, component-based building blocks
- Connecting LLMs to external data sources and tools via LangChain's library of integrations
- Production LLM apps that need monitoring, evaluation, and debugging (via LangSmith)
- Starting point before moving to LangGraph for fine-grained orchestration or Deep Agents for higher-level agent patterns

## Key features

- Standard interface for chat models, embeddings, and vector stores (e.g. `init_chat_model`)
- Modular, component-based architecture for chaining interoperable pieces and integrations
- Part of a broader ecosystem: LangGraph (orchestration), Deep Agents (agent patterns), LangSmith (evals/observability and deployment)
- Available for both Python and JS/TS (LangChain.js)

## Category

**framework** — the README explicitly describes it as "a framework for building agents and LLM-powered applications."
