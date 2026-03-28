import type { StripeLifecycleEvent } from "@/lib/stripe-events";
import { stitchAttribution } from "@/lib/attribution";
import { ensureTables, sql } from "@/lib/db";
import { dispatchEvent } from "@/lib/dispatch";
import type { StitchedEvent } from "@/lib/stitched-event";

let tablesReady = false;

/**
 * Record a Stripe lifecycle event, stitch attribution, and dispatch downstream.
 */
export async function recordStripeLifecycleEvent(event: StripeLifecycleEvent) {
  if (!tablesReady) {
    await ensureTables();
    tablesReady = true;
  }

  const db = sql();

  // 1. Stitch attribution from captures table
  const attribution = await stitchAttribution({
    stripe_customer_id: event.stripe_customer_id,
    stripe_subscription_id: event.stripe_subscription_id,
    user_id: event.user_id,
    account_id: event.account_id,
    email: event.user_email,
  });

  const attributed = attribution !== null;

  // 2. Persist the lifecycle event
  const insertedRows = await db`
    INSERT INTO stripe_lifecycle_events (
      event_id, event_type, source, occurred_at,
      stripe_customer_id, stripe_subscription_id,
      user_id, user_email, account_id,
      plan_name, trial_days, billing_model,
      amount_cents, currency, attributed, raw_payload
    ) VALUES (
      ${event.event_id},
      ${event.event_type},
      ${event.source},
      ${event.occurred_at},
      ${event.stripe_customer_id ?? null},
      ${event.stripe_subscription_id ?? null},
      ${event.user_id ?? null},
      ${event.user_email ?? null},
      ${event.account_id ?? null},
      ${event.plan_name ?? null},
      ${event.trial_days ?? null},
      ${event.billing_model ?? null},
      ${event.amount_cents ?? null},
      ${event.currency ?? null},
      ${attributed},
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
      attributed,
      deliveries: [],
    };
  }

  // 3. Dispatch stitched event to downstream adapters
  const stitched: StitchedEvent = { ...event, attribution };
  const deliveries = await dispatchEvent(stitched);

  return {
    inserted: true,
    eventId: event.event_id,
    eventType: event.event_type,
    attributed,
    deliveries,
  };
}
