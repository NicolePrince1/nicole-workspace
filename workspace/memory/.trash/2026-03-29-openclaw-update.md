# Session: 2026-03-29 06:06:27 UTC

- **Session Key**: agent:main:telegram:direct:5810523015
- **Session ID**: 9f71fb51-5a60-4f74-87dd-e5d11ffdf385
- **Source**: telegram

## Conversation Summary

assistant: ✅ New session started · model: openai-codex/gpt-5.4
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "1166",
  "sender_id": "5810523015",
  "sender": "Chris Irwin",
  "timestamp": "Sun 2026-03-29 05:42 UTC"
}
```

Sender (untrusted metadata):
```json
{
  "label": "Chris Irwin (5810523015)",
  "id": "5810523015",
  "name": "Chris Irwin"
}
```

What’s new in latest version of openclaw
assistant: <final>The latest version of OpenClaw (v2026.3.28) is out. Here are the highlights:

### **Major Changes**
*   **Approval Workflow:** Plugins can now require explicit approval before tool execution. This uses a new `requireApproval` hook and works natively via Telegram buttons, Discord interactions, or the `/approve` command.
*   **xAI Integration:** The xAI provider moved to the Responses API, adding first-class support for `x_search`. It now auto-enables for web-search/tool configurations.
*   **MiniMax Image Gen:** Added support for the `image-01` model, including generation and image-to-image editing.
*   **Unified File Uploads:** A new `upload-file` action now handles Slack, MS Teams, and Google Chat, with support for BlueBubbles as well.
*   **Container Simplified:** The setup for Podman/Docker containers is now much leaner (launches under `~/.local/bin` instead of requiring a service user).

### **Key Fixes**
*   **Telegram:** Long messages now split at word boundaries instead of mid-word.
*   **Discord/WhatsApp:** Fixed several infinite-loop/echo issues in self-chat/group modes and improved reconnection stability for Discord.
*   **UI/Experience:**
    *   **Skill Management:** The Control UI now features a better filterable skill list with one-click installation recipes.
    *   **Agent Workspace:** File previewing is more interactive, with lazy-loaded markdown rendering and a better tree-style sidebar navigation.

**Breaking Notice:** If you use Qwen, the old OAuth integration is removed; you'll need to migrate to Model Studio (`openclaw onboard --auth-choice modelstudio-api-key`). Also, the configuration system no longer automatically migrates very old legacy keys (older than two months)—these will now fail validation if not updated.

Let me know if you want me to look into anything specific or update your local setup!</final>
