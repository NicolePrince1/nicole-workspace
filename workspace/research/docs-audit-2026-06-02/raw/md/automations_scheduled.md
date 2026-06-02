> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scheduled Delivery

> Set the cadence, day, and time an automation fires.

Oviond automations let you schedule reports to be delivered automatically to your clients — no manual sending required. You can send reports as live links or PDF attachments on any recurring schedule you define.

## Create an automation

<Steps>
  <Step title="Open Automations">
    In the left sidebar, click **Automations**, then click **New Automation**.
  </Step>

  <Step title="Select a report">
    Choose the project (report) you want to send. You can only select one project per automation.
  </Step>

  <Step title="Set the schedule">
    Choose a frequency: **Daily**, **Weekly**, or **Monthly**. Then set the specific day (for weekly/monthly), time, and timezone for delivery.
  </Step>

  <Step title="Configure delivery">
    Select the delivery method:

    * **Email link** — sends a live link to the report
    * **PDF attachment** — attaches a rendered PDF to the email

    Add recipient email addresses, customize the email subject line, and optionally write a message body.
  </Step>

  <Step title="Save the automation">
    Click **Save**. The automation is active immediately and will run on the next scheduled time.
  </Step>
</Steps>

## Manage automations

From the **Automations** list you can:

* **Pause / unpause** — Click the toggle next to any automation to suspend it without deleting it.
* **Edit** — Update the schedule, recipients, or delivery settings at any time.
* **Delete** — Remove automations individually or in bulk using the checkboxes.

## View execution history

Click on any automation to open its detail view and see a log of every past send — including the timestamp and delivery status (success or failure). This is useful for confirming reports were delivered or diagnosing missed sends.

## Test an automation

To send an immediate test delivery without waiting for the next scheduled time, open the automation detail and click **Send Now**. The report is sent to all configured recipients right away.

<Note>
  Test sends count toward your monthly email quota.
</Note>
