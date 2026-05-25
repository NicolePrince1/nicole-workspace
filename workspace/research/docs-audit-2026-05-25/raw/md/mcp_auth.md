> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Authentication

> How the Oviond MCP server authenticates AI agents — OAuth 2.1 under the hood.

The Oviond MCP server uses **OAuth 2.1 authorization-code flow with PKCE** — the same pattern Anthropic's MCP spec mandates for remote servers. This section walks through what the agent and Oviond do during the handshake.

## Flow at a glance

1. **Discovery** — the agent fetches `https://api.oviond.com/.well-known/oauth-authorization-server` to learn the auth endpoints.
2. **Client registration** — the agent dynamically registers with Oviond (no manual client-secret setup required).
3. **Authorization request** — the agent opens a browser to Oviond's `/oauth/authorize` with a PKCE challenge.
4. **User consent** — you sign in to Oviond and approve the connection scope.
5. **Token exchange** — the agent exchanges the authorization code for an access token via `/oauth/token`.
6. **Tool calls** — every subsequent MCP request carries `Authorization: Bearer <access_token>`.

## Token scope

Access tokens are scoped to **the signed-in user's role and allowed projects**. The MCP server:

* Sees only clients, projects, and data the authenticated user can see in the web app.
* Inherits role restrictions (read-only users can only read via MCP).
* Can't delete or modify data the user isn't authorized for.

## Token lifetime

* **Access tokens** last 1 hour.
* **Refresh tokens** are issued alongside the access token and last 30 days.
* The MCP client auto-refreshes — you won't be prompted to sign in again during normal usage.

## Revoking access

Revoke an MCP client's access at any time from **Account → Connected Apps** in Oviond. Revoked tokens stop working immediately — the agent will need to re-authorize on its next tool call.

<Note>
  The MCP server does **not** use the Bearer API keys you create under **API Keys**. Those are for direct REST API calls. MCP has its own OAuth flow with per-client tokens.
</Note>
