> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Restore

> Bring a soft-deleted item back to your active workspace.

Restoring moves an item out of the Archive and back to its original location. Clients, projects, and media items can all be restored — and their dependent children (a client's projects, a project's widgets) come back intact.

<Steps>
  <Step title="Open Archive">
    From **Account → Archive**.
  </Step>

  <Step title="Filter by type">
    Narrow to **Clients**, **Projects**, or **Media** if you know what you're looking for.
  </Step>

  <Step title="Select items">
    Check the items you want to restore. Multi-select works.
  </Step>

  <Step title="Click Restore">
    Items reappear in their original location — clients back to the Clients list, projects back under their client, media back to the Media library.
  </Step>
</Steps>

## What if the parent was deleted too?

* Restoring a **project** whose parent **client** is also archived — the client is restored first automatically. You end up with both the client and its project active again.
* Restoring a **project** whose parent client was **permanently deleted** — the project returns to the Archive with a new error state. You'll need to reassign it to a different active client.

## Retention

You can only restore items within the retention window (90 days by default). Past that, the item is permanently purged.
