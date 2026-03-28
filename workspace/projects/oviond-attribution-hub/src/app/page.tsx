import { hasAdminSession } from "@/lib/auth";
import { getDashboardData } from "@/lib/dashboard";

export const dynamic = "force-dynamic";

function formatLabel(value: string) {
  return value.replace(/_/g, " ");
}

function percent(value: number) {
  return `${(value * 100).toFixed(0)}%`;
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
                Stripe decides when a trial, payment, or cancellation is real. This app captures attribution identifiers, stitches them back onto Stripe lifecycle events, and then pushes clean downstream signals to Meta, GA4, and Google Ads.
              </p>
            </div>
            <div className="grid gap-3 sm:grid-cols-2">
              {[
                "Stripe lifecycle events as source of truth",
                "Lightweight attribution capture endpoint",
                "Stitching layer for Meta / GA4 / Google Ads",
                "Railway-ready dashboard and replay tooling",
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

  const {
    dbOk,
    env,
    keyCounts,
    attributionCaptures7d,
    attributedTrialStarts7d,
    unattributedTrialStarts7d,
    trialAttributionMatchRate,
    recentEvents,
    recentDeliveries,
  } = await getDashboardData();

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
                  Stripe lifecycle events are the truth layer. Attribution captures are stitched onto those events before downstream delivery, so paid media platforms observe real business events instead of fragile pageview or form-submit proxies.
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

        <section className="mt-8 grid gap-4 md:grid-cols-2 xl:grid-cols-5">
          {keyCounts.map((item) => (
            <article
              key={item.eventType}
              className="rounded-3xl border border-white/10 bg-white/5 p-5 shadow-lg shadow-slate-950/20"
            >
              <p className="text-xs uppercase tracking-[0.18em] text-slate-400">
                {formatLabel(item.eventType)}
              </p>
              <p className="mt-4 text-4xl font-semibold text-white">{item.count}</p>
              <p className="mt-2 text-sm text-slate-400">Last 7 days</p>
            </article>
          ))}
        </section>

        <section className="mt-8 grid gap-4 md:grid-cols-2 xl:grid-cols-4">
          <article className="rounded-3xl border border-white/10 bg-white/5 p-5 shadow-lg shadow-slate-950/20">
            <p className="text-xs uppercase tracking-[0.18em] text-slate-400">
              Attribution captures
            </p>
            <p className="mt-4 text-4xl font-semibold text-white">{attributionCaptures7d}</p>
            <p className="mt-2 text-sm text-slate-400">Last 7 days</p>
          </article>
          <article className="rounded-3xl border border-white/10 bg-white/5 p-5 shadow-lg shadow-slate-950/20">
            <p className="text-xs uppercase tracking-[0.18em] text-slate-400">
              Attributed trial starts
            </p>
            <p className="mt-4 text-4xl font-semibold text-white">{attributedTrialStarts7d}</p>
            <p className="mt-2 text-sm text-slate-400">Last 7 days</p>
          </article>
          <article className="rounded-3xl border border-white/10 bg-white/5 p-5 shadow-lg shadow-slate-950/20">
            <p className="text-xs uppercase tracking-[0.18em] text-slate-400">
              Unattributed trial starts
            </p>
            <p className="mt-4 text-4xl font-semibold text-white">{unattributedTrialStarts7d}</p>
            <p className="mt-2 text-sm text-slate-400">Last 7 days</p>
          </article>
          <article className="rounded-3xl border border-white/10 bg-white/5 p-5 shadow-lg shadow-slate-950/20">
            <p className="text-xs uppercase tracking-[0.18em] text-slate-400">
              Trial match rate
            </p>
            <p className="mt-4 text-4xl font-semibold text-white">{percent(trialAttributionMatchRate)}</p>
            <p className="mt-2 text-sm text-slate-400">Attributed trials / total trials</p>
          </article>
        </section>

        <section className="mt-8 grid gap-6 xl:grid-cols-[1.1fr_0.9fr]">
          <article className="rounded-3xl border border-white/10 bg-white/5 p-6 shadow-lg shadow-slate-950/20">
            <div className="flex items-center justify-between gap-4">
              <div>
                <h2 className="text-xl font-semibold">Environment readiness</h2>
                <p className="mt-1 text-sm text-slate-400">
                  These flags show which stitching and delivery surfaces are ready right now.
                </p>
              </div>
            </div>
            <div className="mt-6 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
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
            <h2 className="text-xl font-semibold">Quick ops</h2>
            <p className="mt-1 text-sm text-slate-400">
              Wire captures in first, let Stripe send lifecycle truth second, and replay if credentials change.
            </p>
            <div className="mt-6 space-y-4 text-sm text-slate-200">
              <div className="rounded-2xl border border-white/10 bg-slate-950/40 p-4">
                <p className="font-medium text-white">POST /api/attribution/capture</p>
                <p className="mt-1 text-slate-400">Capture UTMs, click IDs, landing-page context, and identity keys before Stripe events arrive.</p>
              </div>
              <div className="rounded-2xl border border-white/10 bg-slate-950/40 p-4">
                <p className="font-medium text-white">POST /api/stripe/webhook</p>
                <p className="mt-1 text-slate-400">Verified Stripe webhooks mapped into trial, payment, expiry, and cancellation lifecycle events.</p>
              </div>
              <div className="rounded-2xl border border-white/10 bg-slate-950/40 p-4">
                <p className="font-medium text-white">POST /api/ingest</p>
                <p className="mt-1 text-slate-400">Manual lifecycle ingest for backfills and testing only.</p>
              </div>
              <div className="rounded-2xl border border-white/10 bg-slate-950/40 p-4">
                <p className="font-medium text-white">POST /api/internal/replay</p>
                <p className="mt-1 text-slate-400">Re-stitch and re-dispatch a stored Stripe lifecycle event after config changes.</p>
              </div>
            </div>
          </article>
        </section>

        <section className="mt-8 rounded-3xl border border-white/10 bg-white/5 p-6 shadow-lg shadow-slate-950/20">
          <div className="flex items-end justify-between gap-4">
            <div>
              <h2 className="text-xl font-semibold">Recent Stripe lifecycle events</h2>
              <p className="mt-1 text-sm text-slate-400">
                This is the operational truth layer. Attribution is a stitched attribute, not the event source itself.
              </p>
            </div>
          </div>

          <div className="mt-6 overflow-x-auto">
            <table className="min-w-full text-left text-sm">
              <thead className="text-xs uppercase tracking-[0.16em] text-slate-400">
                <tr>
                  <th className="pb-3 pr-4">Type</th>
                  <th className="pb-3 pr-4">Event ID</th>
                  <th className="pb-3 pr-4">Stripe IDs</th>
                  <th className="pb-3 pr-4">User</th>
                  <th className="pb-3 pr-4">Attribution</th>
                  <th className="pb-3">Occurred</th>
                </tr>
              </thead>
              <tbody>
                {recentEvents.length === 0 ? (
                  <tr>
                    <td className="py-6 text-sm text-slate-400" colSpan={6}>
                      No lifecycle events yet. Start by capturing attribution and pointing Stripe webhooks at <code>/api/stripe/webhook</code>.
                    </td>
                  </tr>
                ) : (
                  recentEvents.map((event) => (
                    <tr key={event.id} className="border-t border-white/5 align-top">
                      <td className="py-4 pr-4">
                        <span className="rounded-full bg-cyan-400/10 px-2.5 py-1 text-xs font-medium text-cyan-200">
                          {formatLabel(event.event_type)}
                        </span>
                      </td>
                      <td className="py-4 pr-4 font-mono text-xs text-slate-300">{event.event_id}</td>
                      <td className="py-4 pr-4 text-slate-400">
                        <div>{event.stripe_customer_id ?? "—"}</div>
                        <div className="mt-1 text-xs">{event.stripe_subscription_id ?? "—"}</div>
                      </td>
                      <td className="py-4 pr-4 text-slate-400">{event.user_email ?? "—"}</td>
                      <td className="py-4 pr-4">
                        <span
                          className={`rounded-full px-2.5 py-1 text-xs font-medium ${
                            event.attributed
                              ? "bg-emerald-400/15 text-emerald-200"
                              : "bg-amber-400/15 text-amber-200"
                          }`}
                        >
                          {event.attributed ? "stitched" : "missing"}
                        </span>
                      </td>
                      <td className="py-4 text-slate-400">{event.occurred_at}</td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </section>

        <section className="mt-8 rounded-3xl border border-white/10 bg-white/5 p-6 shadow-lg shadow-slate-950/20">
          <div>
            <h2 className="text-xl font-semibold">Recent platform delivery attempts</h2>
            <p className="mt-1 text-sm text-slate-400">
              These are downstream observers of stitched Stripe truth.
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
                  <th className="pb-3 pr-4">Error</th>
                  <th className="pb-3">Time</th>
                </tr>
              </thead>
              <tbody>
                {recentDeliveries.length === 0 ? (
                  <tr>
                    <td className="py-6 text-sm text-slate-400" colSpan={7}>
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
                      <td className="py-4 pr-4 text-slate-400">{delivery.error ?? "—"}</td>
                      <td className="py-4 text-slate-400">{delivery.created_at}</td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </section>
      </div>
    </main>
  );
}
