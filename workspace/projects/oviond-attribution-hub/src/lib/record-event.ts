import type { CanonicalEvent } from "@/lib/canonical-events";
import { ensureTables, sql } from "@/lib/db";
import { dispatchEvent } from "@/lib/dispatch";

let tablesReady = false;

function normalizeForStorage(event: CanonicalEvent): CanonicalEvent {
  return {
    ...event,
    user_email: event.user_email?.toLowerCase(),
    currency: event.currency?.toUpperCase(),
  };
}

export async function recordEvent(eventInput: CanonicalEvent) {
  if (!tablesReady) {
    await ensureTables();
    tablesReady = true;
  }

  const event = normalizeForStorage(eventInput);
  const db = sql();

  const insertedRows = await db`
    INSERT INTO events (
      event_id,
      event_type,
      source,
      occurred_at,
      user_id,
      user_email,
      account_id,
      plan_name,
      trial_days,
      billing_model,
      amount_cents,
      currency,
      page_path,
      page_location,
      landing_page,
      session_source,
      session_medium,
      session_campaign,
      utm_source,
      utm_medium,
      utm_campaign,
      utm_content,
      utm_term,
      fbclid,
      fbp,
      fbc,
      gclid,
      gbraid,
      wbraid,
      client_ip,
      client_user_agent,
      raw_payload
    )
    VALUES (
      ${event.event_id},
      ${event.event_type},
      ${event.source},
      ${event.occurred_at},
      ${event.user_id ?? null},
      ${event.user_email ?? null},
      ${event.account_id ?? null},
      ${event.plan_name ?? null},
      ${event.trial_days ?? null},
      ${event.billing_model ?? null},
      ${event.amount_cents ?? null},
      ${event.currency ?? null},
      ${event.page_path ?? null},
      ${event.page_location ?? null},
      ${event.landing_page ?? null},
      ${event.session_source ?? null},
      ${event.session_medium ?? null},
      ${event.session_campaign ?? null},
      ${event.utm_source ?? null},
      ${event.utm_medium ?? null},
      ${event.utm_campaign ?? null},
      ${event.utm_content ?? null},
      ${event.utm_term ?? null},
      ${event.fbclid ?? null},
      ${event.fbp ?? null},
      ${event.fbc ?? null},
      ${event.gclid ?? null},
      ${event.gbraid ?? null},
      ${event.wbraid ?? null},
      ${event.client_ip ?? null},
      ${event.client_user_agent ?? null},
      ${JSON.stringify(event.raw_payload)}
    )
    ON CONFLICT (event_id) DO NOTHING
    RETURNING id
  `;

  if (insertedRows.length === 0) {
    return {
      inserted: false,
      eventId: event.event_id,
      reason: "duplicate",
      deliveries: [],
    };
  }

  const deliveries = await dispatchEvent(event);

  return {
    inserted: true,
    eventId: event.event_id,
    eventType: event.event_type,
    deliveries,
  };
}
