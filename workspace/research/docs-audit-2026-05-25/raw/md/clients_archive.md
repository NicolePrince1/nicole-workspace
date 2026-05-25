> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Archive Client

> Soft-delete a client with full recovery within the retention window.

Archiving a client removes it from your active dashboard without permanently destroying anything. The client's projects, pages, widgets, and data connections are preserved and can be restored at any time before the retention window expires.

## Archive a client

<Steps>
  <Step title="Open the client's menu">
    From the client card or inside the client's workspace, click the three-dot menu.
  </Step>

  <Step title="Choose Archive">
    Click **Archive client**.
  </Step>

  <Step title="Confirm">
    The client disappears from the active list and moves to the [Archive](/archive/view).
  </Step>
</Steps>

## Restore an archived client

From the [Archive](/archive/view) view, find the client, click **Restore**, and the client reappears in your active list with all its projects intact.

## Retention

Archived clients older than the retention window (90 days by default) are **permanently deleted** by a background job. If you need to keep a client indefinitely without it cluttering the active dashboard, keep it in a dedicated [folder](/clients/folders) instead.
