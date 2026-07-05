# RAGFlow

> An open-source Retrieval-Augmented Generation engine that combines document understanding with agent capabilities.

- **Repository:** https://github.com/infiniflow/ragflow
- **Stars:** 84257

## What it is

RAGFlow is an open-source RAG engine that fuses retrieval-augmented generation with agent capabilities to build a "context layer" for LLMs. It performs deep document understanding and template-based chunking over heterogeneous data sources (Word, slides, Excel, PDFs, scanned copies, web pages, and more), then serves retrieval with multi-recall and fused re-ranking, producing grounded answers with traceable citations. It targets enterprises building production RAG systems, offering pre-built agent templates and configurable LLM/embedding backends.

## What it's good for

- Building enterprise RAG pipelines over messy, mixed-format documents (scans, PDFs, spreadsheets, slides)
- Applications that need grounded answers with visible, traceable citations back to source chunks
- Combining RAG with agentic workflows, including a code executor component and MCP support
- Synchronizing and indexing content from external sources like Confluence, S3, Notion, Discord, and Google Drive
- Self-hosted or cloud deployment for teams needing configurable LLMs and embedding models

## Key features

- Deep document understanding-based knowledge extraction from unstructured, complex-format data
- Template-based, explainable chunking with multiple template options
- Grounded citations with chunk visualization to reduce hallucinations
- Multiple recall paired with fused re-ranking; configurable LLMs and embedding models
- Agentic workflow support, MCP integration, and a Python/JavaScript code executor for agents
- Switchable document engine backend (Elasticsearch or Infinity)

## Category

**framework** — described as an engine/context layer that developers build production RAG and agent-based systems on top of, rather than a single-purpose tool.
