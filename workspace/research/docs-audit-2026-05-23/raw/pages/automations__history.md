> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run History

> See every past run of an automation and its status.

The **Run History** page lists every scheduled delivery an automation has made — successful or not — along with the exact time, recipient list, and any error if it failed.

## Status codes

| Status        | Meaning                                                                          |
| ------------- | -------------------------------------------------------------------------------- |
| **Delivered** | Email was successfully queued to every recipient's provider.                     |
| **Partial**   | Some recipients received it, others bounced or errored.                          |
| **Failed**    | The automation errored before sending — typically a rendering or template issue. |
| **Skipped**   | Automation was paused when the scheduled run fired.                              |

## When to check History

* **Debugging a missed delivery** — a client says they didn't receive the report; check History to confirm it fired and to see the recipient-level delivery status.
* **Auditing** — prove that an end-of-month report was delivered on time.
* **Error triage** — a row showing **Failed** includes the specific error (e.g. *Integration error — Google Ads token expired*).

## Retention

Run history is retained for 12 months. Older entries are purged automatically.
