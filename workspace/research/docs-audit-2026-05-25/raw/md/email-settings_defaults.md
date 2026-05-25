> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Defaults

> Set the default subject, sender, and message for every automation email.

Defaults live at **Account → Email Settings → Defaults**. Anything you set here becomes the starting value every time you create a new [automation](/automations/add) — automations can override per-delivery.

## Fields

| Field                    | Default                   | Notes                                                                         |
| ------------------------ | ------------------------- | ----------------------------------------------------------------------------- |
| **Default subject**      | `{project_name} — {date}` | Supports template variables like `{project_name}`, `{client_name}`, `{date}`. |
| **Default from name**    | Your agency company name  | Shown as the sender name in the recipient's inbox.                            |
| **Default from email**   | `hello@oviond.com`        | Override by adding a [sender](/email-settings/senders) on a verified domain.  |
| **Default message body** | Short Oviond-branded copy | Use the rich text editor to set your own intro copy.                          |

<Tip>
  Keeping the defaults client-agnostic (no hardcoded client names) means every automation inherits sensible defaults and you only customize the bits that differ per client.
</Tip>
