> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect

> Wire Claude, Cursor, or another MCP client to your Oviond account.

Every MCP client supports remote HTTP servers with OAuth. The specifics differ, but the server URL is always the same:

```
https://api.oviond.com/mcp
```

## Claude Desktop

<Steps>
  <Step title="Open Claude Desktop settings">
    From the menu bar, open **Settings → Connectors**.
  </Step>

  <Step title="Add Oviond">
    Click **+ Add custom connector** and enter the URL `https://api.oviond.com/mcp`.
  </Step>

  <Step title="Sign in">
    Claude Desktop opens a browser window to Oviond's sign-in page. Sign in and authorize the connection.
  </Step>

  <Step title="Verify">
    Back in Claude Desktop, you should see Oviond in your connector list. Start a chat and ask Claude to *"list my Oviond clients"* to confirm.
  </Step>
</Steps>

## Cursor

<Steps>
  <Step title="Open Cursor settings">
    **Settings → MCP** (or edit `~/.cursor/mcp.json` directly).
  </Step>

  <Step title="Add the server">
    ```json theme={null}
    {
      "mcpServers": {
        "oviond": {
          "url": "https://api.oviond.com/mcp"
        }
      }
    }
    ```
  </Step>

  <Step title="Authorize">
    Restart Cursor. On first tool call, Cursor opens a browser to complete OAuth.
  </Step>
</Steps>

## Other MCP clients

Any client that speaks the MCP HTTP transport with OAuth 2.1 support works. Point it at `https://api.oviond.com/mcp` and complete the OAuth flow.

<Note>
  Only **streamable HTTP** transport is supported. Stdio servers don't apply here — Oviond's MCP server is hosted by us, not run locally.
</Note>

## First prompts to try

* *"List all my Oviond clients."*
* *"Create a new client called 'Acme Corp' with website acme.example."*
* *"Build a dashboard called 'Paid Social Overview' for Acme."*
* *"Schedule the Acme monthly report to send on the 1st of every month."*
