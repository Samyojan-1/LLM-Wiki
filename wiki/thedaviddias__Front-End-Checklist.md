# Front-End Checklist

> An open-source, structured checklist of front-end quality rules, usable via a website, an MCP server, or this README.

- **Repository:** https://github.com/thedaviddias/Front-End-Checklist
- **Stars:** 73121

## What it is

Front-End Checklist turns front-end best practices into a practical review workflow. It is organized as 385 individual rules spread across 11 categories (HTML, CSS, JavaScript, Performance, Accessibility, SEO, Security, Images, Testing, Privacy, Internationalization), each with a priority level (Critical/High/Medium/Low), an explanation, remediation guidance, and verification steps. The same rule corpus can be browsed on a website, queried by AI agents through a hosted MCP server, or worked through directly as checkboxes in the README.

## What it's good for

- Auditing a website or component against accessibility, performance, SEO, and security best practices
- Running a structured code review of pasted HTML/CSS/JavaScript/React/Next.js code
- Having an MCP-compatible AI agent look up a specific rule and get remediation guidance with code examples
- Auditing a live public URL for accessibility, performance, and SEO issues
- Reviewing a pull request against a fixed, prioritized checklist before shipping

## Key features

- 385 rules across 11 categories, each tagged with a Critical/High/Medium/Low priority
- A public MCP server (`mcp.frontendchecklist.io`) exposing 11 tools, including `review_code`, `search_rules`, `audit_url`, and `get_workflow`
- Installable "skills" (e.g., a global audit skill and focused rule-specific skills like `https`) for tools that support the Agent Skills convention
- A companion project, UX Patterns for Devs, for choosing the right UI pattern before verifying implementation quality
- A generated, always-in-sync README checklist plus a browsable rules website

## Category

skills/plugins — its primary interface for AI agents is a set of installable skills and an MCP server exposing rule-lookup/audit tools, rather than a framework, memory system, or orchestrator.
