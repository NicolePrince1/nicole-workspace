> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> The Oviond MCP server lets Claude and other AI agents manage your Oviond account directly.

Oviond ships a **Model Context Protocol (MCP)** server so AI agents — Claude Desktop, Cursor, Claude Code, and any other MCP-compatible client — can manage your Oviond account programmatically. Ask your agent to *"create a new client and an agency report for them"* and it happens.

## What you can do

The MCP server exposes 19 tool categories that cover most of the Oviond surface area:

* **Clients & Folders** — create, rename, delete, and organize clients.
* **Projects & Pages** — create reports and dashboards, add pages, duplicate layouts.
* **Widgets** — add, update, and remove chart/KPI/table/text widgets.
* **Templates & Themes** — browse the template library, apply themes to projects.
* **Integrations** — list connected data sources, rename, and manage profiles.
* **Automations** — schedule and test automated report deliveries.
* **Branding & Company** — update logo, favicon, and company details.
* **Assets, Media, Domains, Search**, and more.

## How it works

* **Transport** — streamable HTTP at `https://api.oviond.com/mcp`.
* **Auth** — OAuth 2.1 authorization-code flow. Your AI agent launches a browser, you sign into Oviond, and the agent gets a scoped access token.
* **Isolation** — every tool call is scoped to the signed-in account. The agent can only touch data the authenticated user has permission for.

## Next steps

* [Connect](/mcp/connect) — wire up Claude, Cursor, or your MCP client to Oviond.
* [Authentication](/mcp/auth) — what the OAuth flow does under the hood.
* [Available Tools](/mcp/tools) — the full catalog of MCP tools.
