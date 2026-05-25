> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Onboarding

> The 4-step account setup shown after your first sign-in.

After your first sign-in, Oviond opens an **Account Setup** modal that asks for four things. The modal is blocking — you can't click outside or press Escape to dismiss — but each step is one field, and the whole flow takes under a minute.

Once you complete it, the `account.onboarding` flag flips off and the modal never appears again. You can always update the values later under [Account](/account/overview) and [Company](/company/overview).

## The 4 steps

<Steps>
  <Step title="Full Name">
    *"What should we call you?"* — your name as it should appear throughout the app and in activity-log entries. Also shown on team member listings.
  </Step>

  <Step title="Company Name">
    *"What is the name of your company?"* — the agency name used on report headers, email footers, and shared links (unless overridden by [white-label branding](/company/branding)).
  </Step>

  <Step title="Website">
    *"What is your company's website?"* — your agency's URL. If you don't include `http://` or `https://`, Oviond adds `https://` automatically. Shown on the accounts row and used for the default screenshot on your own company card.
  </Step>

  <Step title="Client Count">
    *"How many clients do you report for?"* — pick one: **1–5**, **6–20**, **21–100**, or **100+**. This isn't a hard limit — it's used for plan recommendations and to tailor onboarding emails.
  </Step>
</Steps>

## What happens next

When you click **Get Started** on step 4, Oviond:

* Saves your name to [Profile Settings](/users/profile).
* Saves company name and website to [Company](/company/overview).
* Records the client-count bucket on your account.
* Sets `account.onboarding = false` so the modal doesn't show again.
* Drops you on your Clients dashboard, ready to [add your first client](/clients/add).

## Troubleshooting

* **The modal won't dismiss** — each step validates the field before you can advance. Fix any red inline error, then **Continue** becomes active.
* **Website rejected** — it expects a simple domain (e.g. `yourcompany.com`). Leave off paths and trailing slashes.
* **The modal reappears on a different device** — it follows the account, not the device. If you only partially completed it elsewhere, finish it on this device and it syncs.
