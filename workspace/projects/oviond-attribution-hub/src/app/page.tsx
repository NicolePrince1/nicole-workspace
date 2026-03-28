import { hasAdminSession } from "@/lib/auth";
import { getDashboardData } from "@/lib/dashboard";

export const dynamic = "force-dynamic";

function formatLabel(value: string) {
  return value.replace(/_/g, " ");
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
                Reliable conversion truth for Meta, GA4, Google Ads, and Stripe.
              </h1>
              <p className="max-w-2xl text-base leading-7 text-slate-300 sm:text-lg">
                This app records canonical backend events first, then fans them out to ad and analytics platforms. That means page views and form submits stop pretending to be business truth.
              </p>
            </div>
            <div className="grid gap-3 sm:grid-cols-2">
              {[
                "Canonical event ledger",
                "Meta StartTrial + dedupe ready",
                "GA4 Measurement Protocol delivery",
                "Google Ads adapter scaffold with replay support",
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

  const { dbOk, env, keyCounts, recentEvents, recentDeliveries } = await getDashboardData();

  return (
    <main className="min-h-screen bg-[radial-gradient(circle_at_top,_#0f172a,_#020617_55%)] text-slate-100">
      <div className="mx-auto max-w-7xl px-6 py-8">
        <div className="rounded-[28px] border border-white/10 bg-white/5 p-6 shadow-2xl shadow-slate-950/40 backdrop-blur">
          <div className="flex flex-col gap-6 xl:flex-row xl:items-end xl:justify-between">
            <div className="space-y-4">
              <div className="inline-flex items-center rounded-full border border-cyan-400/30 bg-cyan-400/10 px-3 py-1 text-xs font-medium text-cyan-200">
                Railway-ready internal app
              </div>
              <div>
                <h1 className="text-3xl font-semibold tracking-tight sm:text-4xl">
                  Oviond Attribution Hub
                </h1>
                <p className="mt-3 max-w-3xl text-sm leading-7 text-slate-300 sm:text-base">
                  Backend-first event truth for trials, subscriptions, invoices, and lifecycle events. This dashboard shows what the app believes happened, then how that truth was dispatched to Meta, GA4, and Google Ads.
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

        <section className="mt-8 grid gap-4 md:grid-cols-2 xl:grid-cols-4">
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

        <section className="mt-8 grid gap-6 xl:grid-cols-[1.1fr_0.9fr]">
          <article className="rounded-3xl border border-white/10 bg-white/5 p-6 shadow-lg shadow-slate-950/20">
            <div className="flex items-center justify-between gap-4">
              <div>
                <h2 className="text-xl font-semibold">Environment readiness</h2>
                <p className="mt-1 text-sm text-slate-400">
                  These flags show which delivery surfaces are ready right now.
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
              Useful endpoints for wiring the app into Oviond and replaying events when credentials come online.
            </p>
            <div className="mt-6 space-y-4 text-sm text-slate-200">
              <div className="rounded-2xl border border-white/10 bg-slate-950/40 p-4">
                <p className="font-medium text-white">POST /api/ingest</p>
                <p className="mt-1 text-slate-400">Canonical app event ingest with bearer auth.</p>
              </div>
              <div className="rounded-2xl border border-white/10 bg-slate-950/40 p-4">
                <p className="font-medium text-white">POST /api/stripe/webhook</p>
                <p className="mt-1 text-slate-400">Verified Stripe webhooks mapped into canonical revenue events.</p>
              </div>
              <div className="rounded-2xl border border-white/10 bg-slate-950/40 p-4">
                <p className="font-medium text-white">POST /api/internal/replay</p>
                <p className="mt-1 text-slate-400">Re-dispatch a stored event to platform adapters after config changes.</p>
              </div>
              <div className="rounded-2xl border border-white/10 bg-slate-950/40 p-4">
                <p className="font-medium text-white">GET /api/health</p>
                <p className="mt-1 text-slate-400">Runtime and database health probe for Railway.</p>
              </div>
            </div>
          </article>
        </section>

        <section className="mt-8 rounded-3xl border border-white/10 bg-white/5 p-6 shadow-lg shadow-slate-950/20">
          <div className="flex items-end justify-between gap-4">
            <div>
              <h2 className="text-xl font-semibold">Recent canonical events</h2>
              <p className="mt-1 text-sm text-slate-400">
                The event ledger is the source of truth. Platforms are downstream.
              </p>
            </div>
          </div>

          <div className="mt-6 overflow-x-auto">
            <table className="min-w-full text-left text-sm">
              <thead className="text-xs uppercase tracking-[0.16em] text-slate-400">
                <tr>
                  <th className="pb-3 pr-4">Type</th>
                  <th className="pb-3 pr-4">Event ID</th>
                  <th className="pb-3 pr-4">Source</th>
                  <th className="pb-3 pr-4">User</th>
                  <th className="pb-3 pr-4">Session</th>
                  <th className="pb-3">Occurred</th>
                </tr>
              </thead>
              <tbody>
                {recentEvents.length === 0 ? (
                  <tr>
                    <td className="py-6 text-sm text-slate-400" colSpan={6}>
                      No events yet. Wire Oviond to POST canonical events into <code>/api/ingest</code>.
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
                      <td className="py-4 pr-4 text-slate-300">{event.source}</td>
                      <td className="py-4 pr-4 text-slate-400">{event.user_email ?? "—"}</td>
                      <td className="py-4 pr-4 text-slate-400">
                        {[event.session_source, event.session_medium, event.session_campaign]
                          .filter(Boolean)
                          .join(" / ") || "—"}
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
              Each canonical event records what was attempted downstream and what happened.
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
