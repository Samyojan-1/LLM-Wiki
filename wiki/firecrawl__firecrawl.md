# Firecrawl

> An API that searches, scrapes, and interacts with the web at scale, turning pages into clean data for AI agents.

- **Repository:** https://github.com/firecrawl/firecrawl
- **Stars:** 144018

## What it is

Firecrawl is an open-source API for searching, scraping, and interacting with the web at scale. It converts pages into clean markdown or structured JSON, handles JS-rendered content, rotating proxies, and rate limiting internally, and exposes endpoints for search, scrape, crawl, map, and interactive page actions. It's built to feed AI agents and LLM applications with reliable, token-efficient web content, and is available self-hosted (open source) or as a hosted cloud service.

## What it's good for

- Feeding LLM agents clean, structured web content instead of raw HTML
- Scraping single pages or crawling entire sites into markdown/JSON
- Searching the web and retrieving full page content from the results
- Automated data-gathering where an agent describes what it needs rather than supplying exact URLs (Agent endpoint)
- Interacting with pages (click, scroll, type, wait) before extraction, or batch-scraping thousands of URLs asynchronously

## Key features

- Core endpoints: Search, Scrape, Interact, Agent, Crawl, Map, Batch Scrape
- Output formats include markdown, structured JSON (via schema), and screenshots
- Media parsing for web-hosted PDFs, DOCX, and other document types
- MCP server and CLI/skill integration for connecting to AI agents (e.g. Claude Code, OpenCode)
- SDKs for Python, Node.js, Java, Elixir, Rust, and a community-maintained Go SDK
- Open source (AGPL-3.0 core, MIT for SDKs/UI components) with a hosted cloud version offering added features

## Category

**tooling** — it is a web data-acquisition API/service that agents and applications call as a tool, rather than a framework for orchestrating agent logic.
