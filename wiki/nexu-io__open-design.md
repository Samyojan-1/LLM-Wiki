# Open Design

> A local-first, open-source desktop app that turns coding-agent CLIs into a design engine for prototypes, decks, images, and video.

- **Repository:** https://github.com/nexu-io/open-design
- **Stars:** 74889

## What it is

Open Design bills itself as the open-source alternative to Anthropic's closed, cloud-only "Claude Design" product. Rather than shipping its own AI model, it wraps whatever coding-agent CLI is already on the user's machine (Claude Code, Codex, Cursor, Gemini CLI, and about 20 others) and turns that agent into a design engine driven by skills, plugins, and a brand-contract file called `DESIGN.md`. It runs as a native desktop app (macOS/Windows, with a Linux AppImage) plus a local daemon, and outputs real files — HTML, PDF, PPTX, and MP4 — rather than a proprietary canvas format.

## What it's good for

- Generating web/desktop/mobile prototypes, dashboards, and live artifacts from a text brief
- Producing pitch decks, slides, and marketing image sets aligned to a brand's design system
- Creating motion graphics/video (via the bundled HyperFrames framework) from HTML+CSS+GSAP
- Migrating an existing Figma or code-based design workflow into React/Next.js/Vue source
- Using a design workspace from inside an existing coding agent via its MCP server, instead of a separate GUI

## Key features

- Ships 100+ "skills" (SKILL.md-based workflows) and 150 brand-grade `DESIGN.md` design systems (Linear, Stripe, Airbnb, etc.)
- 261 official plugins for scenarios like Figma migration, code migration, and media generation
- Works as a stdio MCP server so any MCP-compatible coding agent can call it directly (`od mcp install <agent>`)
- BYOK model router / proxy supporting Anthropic, OpenAI, Azure, Google, and Ollama-compatible endpoints, with SSRF protection
- Exports artifacts as real HTML/CSS, PDF, PPTX, MP4, or ZIP rather than a locked-in file format
- Self-hostable via Docker or Sealos, in addition to the native desktop app

## Category

tooling — it is a design-workflow tool that orchestrates existing coding agents (via skills, plugins, and MCP) rather than being itself an agent framework or a memory/orchestration layer.
