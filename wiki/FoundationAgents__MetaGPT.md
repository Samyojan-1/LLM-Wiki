# MetaGPT: The Multi-Agent Framework

> A multi-agent framework that assigns GPT-based agents distinct software-company roles to collaboratively turn a one-line requirement into a working software project.

- **Repository:** https://github.com/FoundationAgents/MetaGPT
- **Stars:** 69189

## What it is

MetaGPT takes a single-line natural-language requirement and produces outputs such as user stories, competitive analysis, requirements, data structures, APIs, and documents. Internally it models a software company with roles like product manager, architect, project manager, and engineer, and applies "carefully orchestrated SOPs" (standard operating procedures) to coordinate them — the core philosophy stated in the README is `Code = SOP(Team)`. It is installed as a Python package and can be used both from the command line and as a library.

## What it's good for

- Generating a full early-stage software project (docs, design artifacts, and code) from a short natural-language description.
- Building and experimenting with custom multi-agent teams (see the "MultiAgent 101" tutorial referenced in the README).
- Data analysis and coding tasks via the bundled "Data Interpreter" role, which can run code and produce plots from a natural-language instruction.
- Research-style use cases such as debate, researcher agents, and receipt-assistant workflows listed in the docs.

## Key features

- CLI usage (`metagpt "Create a 2048 game"`) and a library API (`generate_repo`, `ProjectRepo`).
- Configurable LLM backend (OpenAI, Azure, Ollama, Groq, and others) via `~/.metagpt/config2.yaml`.
- Predefined roles (product manager, architect, project manager, engineer) collaborating through SOPs.
- Data Interpreter role for running data analysis and generating plots from natural language.
- Associated research papers/methods referenced in the repo (e.g., AFlow for automating agentic workflow generation, SPO, AOT).

## Category

framework — it is a Python package/framework for composing role-based multi-agent teams to accomplish tasks, rather than a single end-user application.
