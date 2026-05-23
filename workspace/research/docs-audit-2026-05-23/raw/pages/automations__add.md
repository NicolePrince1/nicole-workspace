> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add Automation

> Schedule a report or dashboard for recurring email delivery.

An **automation** sends a report to a list of recipients on a recurring schedule — daily, weekly, or monthly. Once configured, Oviond renders the report, attaches it (if you chose PDF), and emails it from the sender you specify.

<Steps>
  <Step title="Open Automations">
    From the left sidebar.
  </Step>

  <Step title="Click + New Automation">
    Opens the create dialog.
  </Step>

  <Step title="Pick a project">
    Choose the report or dashboard to deliver.
  </Step>

  <Step title="Set the schedule">
    Frequency (daily / weekly / monthly), day, time, and timezone. See [Scheduled Delivery](/automations/scheduled).
  </Step>

  <Step title="Configure the email">
    Recipients, subject, sender, and message body. See [Email Delivery](/automations/email).
  </Step>

  <Step title="Choose attachment">
    Inline HTML only, or attach a [PDF export](/automations/pdf).
  </Step>

  <Step title="Create">
    The automation is saved and starts firing on the next scheduled run.
  </Step>
</Steps>

<Tip>
  Always [Test](/automations/test) a new automation before going live — the test send bypasses the schedule and emails you immediately, so you can verify the content looks right.
</Tip>
