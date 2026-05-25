> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Monthly Client Report

> Automate a recurring monthly report email for a client.

This guide sets up a monthly automated report that delivers to your client's inbox on the 1st of every month. You'll end with an automation that runs without any manual work month to month.

## Before you start

* You have a [project](/projects/add) — report or dashboard — ready to send.
* You've [configured email sending](/email-settings/defaults) from your agency's domain (optional but recommended).
* You've tested the project's widgets with live data.

## 1. Verify the report is ready to send

<Steps>
  <Step title="Open the project">
    Make sure every widget is configured against the right data source and date range.
  </Step>

  <Step title="Use a relative date range">
    Configure the project's default date range to something like **Last Month** or **Previous Calendar Month**. See [Update Project](/projects/update). Relative dates are essential for automations — each monthly fire should pull its own month's data.
  </Step>

  <Step title="Export a test PDF">
    See [PDF Export](/automations/pdf). Check that the rendered PDF looks clean before automating.
  </Step>
</Steps>

## 2. Create the automation

<Steps>
  <Step title="Open Automations">
    From the left sidebar.
  </Step>

  <Step title="Click + New Automation">
    See [Add Automation](/automations/add).
  </Step>

  <Step title="Pick the project">
    The report you just validated.
  </Step>

  <Step title="Set the schedule">
    Frequency: **Monthly**. Day: **1st**. Time: a morning hour in the client's timezone.
  </Step>

  <Step title="Set recipients">
    Add the client contact's email. You can include multiple recipients — they all receive the same message.
  </Step>

  <Step title="Configure the email">
    Subject: *{client_name} — {date}*. Use the default sender from [Email Settings](/email-settings/defaults) or pick a specific one. Write a short intro paragraph for the body.
  </Step>

  <Step title="Choose PDF attachment">
    Attach the report as a PDF so the client has a durable copy.
  </Step>

  <Step title="Create">
    The automation is saved — it fires on the next scheduled run.
  </Step>
</Steps>

## 3. Test before going live

Always test:

<Steps>
  <Step title="Open the automation">
    From the Automations list.
  </Step>

  <Step title="Click Test Send">
    See [Test Automation](/automations/test). Override the recipient to send to yourself.
  </Step>

  <Step title="Check the email">
    Subject, sender, body copy, and PDF attachment — all should look exactly how the client will see it.
  </Step>
</Steps>

## 4. Monitor the first real run

After the first scheduled delivery (on the 1st of next month):

<Steps>
  <Step title="Open the automation's Run History">
    See [Run History](/automations/history).
  </Step>

  <Step title="Check the status">
    **Delivered** — you're good. **Partial** — some recipients bounced; check their email addresses. **Failed** — the render errored; read the message.
  </Step>

  <Step title="Check Email Logs">
    See [Email Logs](/email-settings/logs) for per-recipient delivery events (opened, clicked, bounced).
  </Step>
</Steps>

## If the client changes their address

Edit the automation, update the recipients list, and save. No need to re-test unless you also changed the sender or subject.

## If you need to pause

Toggle **Pause** on the automation row. The schedule stops firing until you unpause — no need to delete the automation. See [List Automations](/automations/list).
