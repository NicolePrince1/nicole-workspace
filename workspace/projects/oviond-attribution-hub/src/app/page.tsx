import { hasAdminSession } from "@/lib/auth";
import { getDashboardData } from "@/lib/dashboard";

export const dynamic = "force-dynamic";

function pct(value: number) {
  return `${(value * 100).toFixed(0)}%`;
}

function money(value: number) {
  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    maximumFractionDigits: 0,
  }).format(value);
}

function formatDateTime(value: string | null) {
  if (!value) {
    return "—";
  }

  return new Intl.DateTimeFormat("en-ZA", {
    dateStyle: "medium",
    timeStyle: "short",
    timeZone: "UTC",
  }).format(new Date(value));
}

function statePillClasses(state: "trialing" | "paid" | "expired" | "cancelled") {
  switch (state) {
    case "paid":
      return "bg-emerald-400/15 text-emerald-200";
    case "trialing":
      return "bg-cyan-400/15 text-cyan-200";
    case "expired":
      return "bg-amber-400/15 text-amber-200";
    case "cancelled":
      return "bg-rose-400/15 text-rose-200";
    default:
      return "bg-slate-400/15 text-slate-200";
  }
}

function LoginScreen() {
  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto flex min-h-screen max-w-5xl items-center px-6 py-16">
        <div className="grid w-full gap-10 lg:grid-cols-[1.2fr_0.8fr]">
          <section className="space-y-6">
            <div className="inline-flex items-center rounded-full border border-cyan-400/30 bg-cyan-400/10 px-3 py-1 text-xs font-medium text-cyan-200">
              Oviond Attribution Hub
            </div>
            <div className="space-y-4">
              <h1 className="text-4xl font-semibold tracking-tight sm:text-5xl">
                Stripe-first attribution truth for Oviond.
              </h1>
              <p className="max-w-2xl text-base leading-7 text-slate-300 sm:text-lg">
                Stripe tells us when a trial really starts, when it becomes paid, and when it dies. The hub’s job is to stitch campaign data onto that journey and make the commercial story obvious.
              </p>
            </div>
            <div className="grid gap-3 sm:grid-cols-2">
              {[
                "Commercial view first, ops lower down",
                "Paid outcomes, not noisy webhook counts",
                "Attribution coverage separated from revenue truth",
                "Customer-level outcomes table for fast diagnosis",
              ].map((item) => (
                <div
                  key={item}
                  className="rounded-2xl border border-white/10 bg-white/5 px-4 py-3 text-sm text-slate-200"
                >
                  {item}
                </div>
              ))}
            </div>
          </section>

          <section className="rounded-3xl border border-white/10 bg-white/5 p-6 shadow-2xl shadow-cyan-950/30 backdrop-blur">
            <div className="space-y-2">
              <p className="text-sm font-medium text-cyan-200">Admin login</p>
              <h2 className="text-2xl font-semibold">Unlock the dashboard</h2>
              <p className="text-sm leading-6 text-slate-300">
                Set <code className="rounded bg-black/30 px-1.5 py-0.5 text-xs">ADMIN_TOKEN</code> on Railway, then use it here to open the internal dashboard.
              </p>
            </div>

            <form action="/api/admin/login" method="post" className="mt-8 space-y-4">
              <label className="block space-y-2">
                <span className="text-sm text-slate-300">Admin token</span>
                <input
                  name="token"
                  type="password"
                  required
                  className="w-full rounded-2xl border border-white/10 bg-slate-950 px-4 py-3 text-sm outline-none ring-0 transition focus:border-cyan-400/50"
                  placeholder="Paste the internal token"
                />
              </label>
              <button
                type="submit"
                className="inline-flex w-full items-center justify-center rounded-2xl bg-cyan-400 px-4 py-3 text-sm font-semibold text-slate-950 transition hover:bg-cyan-300"
              >
                Enter dashboard
              </button>
            </form>
          </section>
        </div>
      </div>
    </main>
  );
}

export default async function DashboardPage() {
  const authed = await hasAdminSession();
  if (!authed) {
    return <LoginScreen />;
  }

  const { dbOk, env, hero, attribution, funnel, recentOutcomes, recentDeliveries } =
    await getDashboardData();

  const commercialCards = [
    {
      label: "Trials started",
      value: String(hero.trialsStarted30d),
      caption: "Last 30 days",
    },
    {
      label: "Paid conversions",
      value: String(hero.paidConversions30d),
      caption: "Trials that became paid in the last 30 days",
    },
    {
      label: "Cohort conversion rate",
      value: pct(hero.cohortConversionRate),
      caption: `${hero.maturePaidCount} of ${hero.matureTrialsCount} mature trials`,
    },
    {
      label: "First-payment revenue",
      value: money(hero.firstPaymentRevenue30d),
      caption: "Recognised from first positive invoices in the last 30 days",
    },
    {
      label: "Trials in flight",
      value: String(hero.trialsInFlight),
      caption: "Started, but not yet paid or lost",
    },
  ];

  const attributionCards = [
    {
      label: "Attribution captures",
      value: String(attribution.captures30d),
      caption: "Last 30 days",
    },
    {
      label: "Attributed trials",
      value: String(attribution.attributedTrials30d),
      caption: "Trial starts with a stitched source/campaign",
    },
    {
      label: "Attributed paid customers",
      value: String(attribution.attributedPaid30d),
      caption: "Paid conversions with stitched attribution",
    },
    {
      label: "Paid attribution coverage",
      value: pct(attribution.paidAttributionCoverage30d),
      caption: `${attribution.unattributedPaid30d} paid conversions still unattributed`,
    },
  ];

  const funnelStages = [
    {
      label: "Tracked trials",
      count: funnel.totalTrackedTrials,
      tone: "text-white",
      bar: "bg-slate-200",
    },
    {
      label: "Still in trial",
      count: funnel.inTrial,
      tone: "text-cyan-200",
      bar: "bg-cyan-400",
    },
    {
      label: "Converted to paid",
      count: funnel.paid,
      tone: "text-emerald-200",
      bar: "bg-emerald-400",
    },
    {
      label: "Lost before pay",
      count: funnel.lostPrePay,
      tone: "text-amber-200",
      bar: "bg-amber-400",
    },
  ];

  return (
    <main className="min-h-screen bg-[radial-gradient(circle_at_top,_#0f172a,_#020617_55%)] text-slate-100">
      <div className="mx-auto max-w-7xl px-6 py-8">
        <div className="rounded-[28px] border border-white/10 bg-white/5 p-6 shadow-2xl shadow-slate-950/40 backdrop-blur">
          <div className="flex flex-col gap-6 xl:flex-row xl:items-end xl:justify-between">
            <div className="space-y-4">
              <div className="inline-flex items-center rounded-full border border-cyan-400/30 bg-cyan-400/10 px-3 py-1 text-xs font-medium text-cyan-200">
                Stripe-first lifecycle attribution
              </div>
              <div>
                <h1 className="text-3xl font-semibold tracking-tight sm:text-4xl">
                  Oviond Attribution Hub
                </h1>
                <p className="mt-3 max-w-3xl text-sm leading-7 text-slate-300 sm:text-base">
                  This dashboard now follows the actual customer journey: trials started, trials that became paid, revenue from first payments, and how much of that story is attributable to real campaigns.
                </p>
              </div>
            </div>

            <div className="flex flex-wrap items-center gap-3">
              <div
                className={`rounded-full px-3 py-1 text-xs font-medium ${
                  dbOk ? "bg-emerald-400/15 text-emerald-200" : "bg-amber-400/15 text-amber-200"
                }`}
              >
                {dbOk ? "Database connected" : "Database missing or unavailable"}
              </div>
              <div
                className={`rounded-full px-3 py-1 text-xs font-medium ${
                  env.STRIPE_WEBHOOK_SECRET && env.STRIPE_SECRET_KEY
                    ? "bg-emerald-400/15 text-emerald-200"
                    : "bg-amber-400/15 text-amber-200"
                }`}
              >
                {env.STRIPE_WEBHOOK_SECRET && env.STRIPE_SECRET_KEY
                  ? "Stripe webhooks live"
                  : "Stripe not fully configured"}
              </div>
              <div
                className={`rounded-full px-3 py-1 text-xs font-medium ${
                  attribution.captures30d > 0
                    ? "bg-cyan-400/15 text-cyan-200"
                    : "bg-slate-400/15 text-slate-300"
                }`}
              >
                {attribution.captures30d > 0
                  ? "Attribution capture active"
                  : "Attribution capture still empty"}
              </div>
              <form action="/api/admin/logout" method="post">
                <button
                  type="submit"
                  className="rounded-full border border-white/10 px-3 py-1 text-xs text-slate-300 transition hover:border-white/20 hover:text-white"
                >
                  Log out
                </button>
              </form>
            </div>
          </div>
        </div>

        <section className="mt-8">
          <div className="mb-4 flex items-end justify-between gap-4">
            <div>
              <h2 className="text-xl font-semibold">Commercial view</h2>
              <p className="mt-1 text-sm text-slate-400">
                Read this row left-to-right: how many trials arrived, how many converted, what that means for cohort performance, and how much cash was recognised from first payments.
              </p>
            </div>
          </div>

          <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-5">
            {commercialCards.map((card) => (
              <article
                key={card.label}
                className="rounded-3xl border border-white/10 bg-white/5 p-5 shadow-lg shadow-slate-950/20"
              >
                <p className="text-xs uppercase tracking-[0.18em] text-slate-400">
                  {card.label}
                </p>
                <p className="mt-4 text-4xl font-semibold text-white">{card.value}</p>
                <p className="mt-2 text-sm leading-6 text-slate-400">{card.caption}</p>
              </article>
            ))}
          </div>
        </section>

        <section className="mt-8">
          <div className="mb-4 flex items-end justify-between gap-4">
            <div>
              <h2 className="text-xl font-semibold">Attribution quality</h2>
              <p className="mt-1 text-sm text-slate-400">
                Keep this separate from revenue truth: this row tells us how much of the paid story we can explain back to channels and campaigns.
              </p>
            </div>
          </div>

          <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
            {attributionCards.map((card) => (
              <article
                key={card.label}
                className="rounded-3xl border border-white/10 bg-white/5 p-5 shadow-lg shadow-slate-950/20"
              >
                <p className="text-xs uppercase tracking-[0.18em] text-slate-400">
                  {card.label}
                </p>
                <p className="mt-4 text-4xl font-semibold text-white">{card.value}</p>
                <p className="mt-2 text-sm leading-6 text-slate-400">{card.caption}</p>
              </article>
            ))}
          </div>
        </section>

        <section className="mt-8 grid gap-6 xl:grid-cols-[1.1fr_0.9fr]">
          <article className="rounded-3xl border border-white/10 bg-white/5 p-6 shadow-lg shadow-slate-950/20">
            <div>
              <h2 className="text-xl font-semibold">Trial pipeline since launch</h2>
              <p className="mt-1 text-sm text-slate-400">
                This is the clearest answer to “what happens to our trials?” It shows the total tracked cohort and where each trial currently sits.
              </p>
            </div>

            <div className="mt-6 space-y-4">
              {funnelStages.map((stage) => {
                const share = funnel.totalTrackedTrials === 0 ? 0 : stage.count / funnel.totalTrackedTrials;
                return (
                  <div key={stage.label} className="space-y-2">
                    <div className="flex items-center justify-between gap-3">
                      <div className="flex items-center gap-2">
                        <span className={`text-sm font-medium ${stage.tone}`}>{stage.label}</span>
                      </div>
                      <div className="text-sm text-slate-300">
                        <span className="font-semibold text-white">{stage.count}</span>
                        <span className="ml-2 text-slate-400">{pct(share)}</span>
                      </div>
                    </div>
                    <div className="h-2 overflow-hidden rounded-full bg-slate-900/70">
                      <div
                        className={`h-full rounded-full ${stage.bar}`}
                        style={{ width: `${Math.max(share * 100, stage.count > 0 ? 6 : 0)}%` }}
                      />
                    </div>
                  </div>
                );
              })}
            </div>
          </article>

          <article className="rounded-3xl border border-white/10 bg-white/5 p-6 shadow-lg shadow-slate-950/20">
            <div>
              <h2 className="text-xl font-semibold">Pipeline notes</h2>
              <p className="mt-1 text-sm text-slate-400">
                A few plain-English readings from the live data so you don’t have to mentally translate the numbers.
              </p>
            </div>
            <div className="mt-6 space-y-4 text-sm leading-7 text-slate-300">
              <div className="rounded-2xl border border-white/10 bg-slate-950/40 p-4">
                <p className="font-medium text-white">What counts as “paid” here</p>
                <p className="mt-1 text-slate-400">
                  We treat a trial as paid when Stripe shows the trial becoming active/paid and, where available, the first positive invoice is recorded. Revenue cards use the positive invoice amount only.
                </p>
              </div>
              <div className="rounded-2xl border border-white/10 bg-slate-950/40 p-4">
                <p className="font-medium text-white">Where attribution still breaks down</p>
                <p className="mt-1 text-slate-400">
                  If a paid customer has no matching capture, the commercial numbers are still right — we just can’t yet tell you which campaign drove them.
                </p>
              </div>
              <div className="rounded-2xl border border-white/10 bg-slate-950/40 p-4">
                <p className="font-medium text-white">Paid then cancelled later</p>
                <p className="mt-1 text-slate-400">
                  {funnel.paidThenCancelled} customers in the tracked cohort converted first and then later cancelled. They still count as successful trial-to-paid conversions historically.
                </p>
              </div>
            </div>
          </article>
        </section>

        <section className="mt-8 rounded-3xl border border-white/10 bg-white/5 p-6 shadow-lg shadow-slate-950/20">
          <div className="flex items-end justify-between gap-4">
            <div>
              <h2 className="text-xl font-semibold">Recent customer outcomes</h2>
              <p className="mt-1 text-sm text-slate-400">
                This replaces raw webhook-event reading. Each row is a real customer/subscription outcome so you can see which trials became paid and which ones did not.
              </p>
            </div>
          </div>

          <div className="mt-6 overflow-x-auto">
            <table className="min-w-full text-left text-sm">
              <thead className="text-xs uppercase tracking-[0.16em] text-slate-400">
                <tr>
                  <th className="pb-3 pr-4">Customer</th>
                  <th className="pb-3 pr-4">Plan</th>
                  <th className="pb-3 pr-4">Trial start</th>
                  <th className="pb-3 pr-4">Current state</th>
                  <th className="pb-3 pr-4">First payment</th>
                  <th className="pb-3 pr-4">Days to pay</th>
                  <th className="pb-3 pr-4">Source / campaign</th>
                  <th className="pb-3">Attribution</th>
                </tr>
              </thead>
              <tbody>
                {recentOutcomes.length === 0 ? (
                  <tr>
                    <td className="py-6 text-sm text-slate-400" colSpan={8}>
                      No customer outcomes yet. Once Stripe webhooks and attribution captures both flow, the journey view will populate here.
                    </td>
                  </tr>
                ) : (
                  recentOutcomes.map((outcome) => (
                    <tr key={outcome.key} className="border-t border-white/5 align-top">
                      <td className="py-4 pr-4 text-slate-200">{outcome.userEmail ?? "—"}</td>
                      <td className="py-4 pr-4 text-slate-400">{outcome.planName ?? "—"}</td>
                      <td className="py-4 pr-4 text-slate-400">{formatDateTime(outcome.trialStartedAt)}</td>
                      <td className="py-4 pr-4">
                        <span
                          className={`rounded-full px-2.5 py-1 text-xs font-medium ${statePillClasses(
                            outcome.currentState,
                          )}`}
                        >
                          {outcome.currentStateLabel}
                        </span>
                      </td>
                      <td className="py-4 pr-4 text-slate-400">
                        {outcome.firstPaidAmountCents != null
                          ? money(outcome.firstPaidAmountCents / 100)
                          : outcome.convertedAt
                            ? formatDateTime(outcome.convertedAt)
                            : "—"}
                      </td>
                      <td className="py-4 pr-4 text-slate-400">
                        {outcome.daysToConvert != null ? `${outcome.daysToConvert} days` : "—"}
                      </td>
                      <td className="py-4 pr-4 text-slate-400">
                        {outcome.source || outcome.campaign ? (
                          <div>
                            <div>{outcome.source ?? "Unknown source"}</div>
                            <div className="mt-1 text-xs text-slate-500">{outcome.campaign ?? outcome.landingPage ?? "—"}</div>
                          </div>
                        ) : (
                          "—"
                        )}
                      </td>
                      <td className="py-4">
                        <span
                          className={`rounded-full px-2.5 py-1 text-xs font-medium ${
                            outcome.attributed
                              ? "bg-emerald-400/15 text-emerald-200"
                              : "bg-amber-400/15 text-amber-200"
                          }`}
                        >
                          {outcome.attributed ? "stitched" : "missing"}
                        </span>
                      </td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </section>

        <section className="mt-8 grid gap-6 xl:grid-cols-[0.9fr_1.1fr]">
          <article className="rounded-3xl border border-white/10 bg-white/5 p-6 shadow-lg shadow-slate-950/20">
            <div className="flex items-center justify-between gap-4">
              <div>
                <h2 className="text-xl font-semibold">System readiness</h2>
                <p className="mt-1 text-sm text-slate-400">
                  Useful, but intentionally lower down now so it doesn’t compete with the commercial read.
                </p>
              </div>
            </div>
            <div className="mt-6 grid gap-3 sm:grid-cols-2">
              {Object.entries(env).map(([key, ready]) => (
                <div
                  key={key}
                  className={`rounded-2xl border px-4 py-3 text-sm ${
                    ready
                      ? "border-emerald-400/20 bg-emerald-400/10 text-emerald-100"
                      : "border-white/10 bg-slate-950/40 text-slate-400"
                  }`}
                >
                  <div className="font-mono text-xs uppercase tracking-wide">{key}</div>
                  <div className="mt-2 text-sm font-medium">{ready ? "Ready" : "Missing"}</div>
                </div>
              ))}
            </div>
          </article>

          <article className="rounded-3xl border border-white/10 bg-white/5 p-6 shadow-lg shadow-slate-950/20">
            <div>
              <h2 className="text-xl font-semibold">Recent downstream delivery attempts</h2>
              <p className="mt-1 text-sm text-slate-400">
                These are the operational logs for Meta, GA4, and Google Ads. Useful for debugging, not for interpreting performance.
              </p>
            </div>

            <div className="mt-6 overflow-x-auto">
              <table className="min-w-full text-left text-sm">
                <thead className="text-xs uppercase tracking-[0.16em] text-slate-400">
                  <tr>
                    <th className="pb-3 pr-4">Platform</th>
                    <th className="pb-3 pr-4">Destination</th>
                    <th className="pb-3 pr-4">Event ID</th>
                    <th className="pb-3 pr-4">Status</th>
                    <th className="pb-3 pr-4">Code</th>
                    <th className="pb-3">Time</th>
                  </tr>
                </thead>
                <tbody>
                  {recentDeliveries.length === 0 ? (
                    <tr>
                      <td className="py-6 text-sm text-slate-400" colSpan={6}>
                        No downstream delivery attempts yet.
                      </td>
                    </tr>
                  ) : (
                    recentDeliveries.map((delivery) => (
                      <tr key={delivery.id} className="border-t border-white/5 align-top">
                        <td className="py-4 pr-4 uppercase text-slate-200">{delivery.platform}</td>
                        <td className="py-4 pr-4 text-slate-400">{delivery.destination_event_name ?? "—"}</td>
                        <td className="py-4 pr-4 font-mono text-xs text-slate-300">{delivery.event_id}</td>
                        <td className="py-4 pr-4">
                          <span
                            className={`rounded-full px-2.5 py-1 text-xs font-medium ${
                              delivery.status === "sent"
                                ? "bg-emerald-400/15 text-emerald-200"
                                : delivery.status === "error"
                                  ? "bg-rose-400/15 text-rose-200"
                                  : delivery.status === "disabled"
                                    ? "bg-amber-400/15 text-amber-200"
                                    : "bg-slate-400/15 text-slate-200"
                            }`}
                          >
                            {delivery.status}
                          </span>
                        </td>
                        <td className="py-4 pr-4 font-mono text-xs text-slate-400">{delivery.response_code ?? "—"}</td>
                        <td className="py-4 text-slate-400">{formatDateTime(delivery.created_at)}</td>
                      </tr>
                    ))
                  )}
                </tbody>
              </table>
            </div>
          </article>
        </section>
      </div>
    </main>
  );
}
