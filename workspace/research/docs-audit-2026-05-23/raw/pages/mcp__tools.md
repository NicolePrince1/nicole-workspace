> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Available Tools

> The full catalog of tools the Oviond MCP server exposes.

The Oviond MCP server exposes 100+ tools across 19 categories. Each tool maps to one or more REST API operations — the MCP server is a thin wrapper that lets your AI agent call the Oviond API with natural language.

## Categories

| Category         | What the agent can do                                                              |
| ---------------- | ---------------------------------------------------------------------------------- |
| **Account**      | Read account info and usage.                                                       |
| **Agency**       | List and manage account-level reports not tied to a client.                        |
| **Assets**       | Manage saved widget sections.                                                      |
| **Automations**  | Create, pause, test, and delete scheduled deliveries.                              |
| **Branding**     | Update logo, favicon, and brand colors.                                            |
| **Clients**      | Create, rename, move, delete, and bulk-delete clients.                             |
| **Company**      | Update agency-level company info.                                                  |
| **Domain**       | Manage custom white-label domains.                                                 |
| **Folders**      | Create, rename, and delete client folders.                                         |
| **Integrations** | List connected data sources and their profiles.                                    |
| **Media**        | Upload, rename, and delete media files.                                            |
| **Pages**        | Add, reorder, rename, and delete pages inside projects.                            |
| **Projects**     | Create, duplicate, bulk-delete, and share reports/dashboards.                      |
| **Search**       | Search clients, projects, and assets by name.                                      |
| **Templates**    | Browse and apply templates.                                                        |
| **Themes**       | Create, update, and apply themes.                                                  |
| **Users**        | List, invite, update, and remove team members.                                     |
| **Widgets**      | Add every widget type (KPI, chart, table, text, image, embed, goal, button, data). |

## Conventions

* **Identifiers** — tool calls return resource IDs that the agent uses to chain subsequent calls. You never see the IDs in chat; the agent handles them behind the scenes.
* **Multi-tenancy** — every call is automatically scoped to the authenticated account. You don't pass an `account_id` or similar.
* **Rate limits** — the same per-account rate limits that apply to the REST API apply to MCP calls.

## Reference

Each MCP tool is a thin wrapper around a single REST operation. For the exact parameters and response shape, see the [API Reference](/api/introduction).
