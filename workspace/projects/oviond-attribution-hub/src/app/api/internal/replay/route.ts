import { NextRequest, NextResponse } from "next/server";
import { verifyAdminRequest } from "@/lib/auth";
import { ensureTables, sql } from "@/lib/db";
import { dispatchEvent } from "@/lib/dispatch";
import { stripeLifecycleEventSchema } from "@/lib/stripe-events";
import { stitchAttribution } from "@/lib/attribution";
import type { StitchedEvent } from "@/lib/stitched-event";

export const runtime = "nodejs";

export async function POST(request: NextRequest) {
  const authError = verifyAdminRequest(request);
  if (authError) {
    return authError;
  }

  let body: { eventId?: string };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "Invalid JSON body" }, { status: 400 });
  }

  if (!body.eventId) {
    return NextResponse.json({ error: "eventId is required" }, { status: 400 });
  }

  try {
    await ensureTables();
    const db = sql();
    const rows = await db`
      SELECT *
      FROM stripe_lifecycle_events
      WHERE event_id = ${body.eventId}
      LIMIT 1
    `;

    const row = rows[0];
    if (!row) {
      return NextResponse.json({ error: "Event not found" }, { status: 404 });
    }

    const event = stripeLifecycleEventSchema.parse({
      event_type: row.event_type,
      event_id: row.event_id,
      source: row.source,
      occurred_at: row.occurred_at,
      stripe_customer_id: row.stripe_customer_id ?? undefined,
      stripe_subscription_id: row.stripe_subscription_id ?? undefined,
      user_id: row.user_id ?? undefined,
      user_email: row.user_email ?? undefined,
      account_id: row.account_id ?? undefined,
      plan_name: row.plan_name ?? undefined,
      trial_days: row.trial_days ?? undefined,
      billing_model: row.billing_model ?? undefined,
      amount_cents: row.amount_cents ?? undefined,
      currency: row.currency ?? undefined,
      raw_payload: row.raw_payload ?? {},
    });

    const attribution = await stitchAttribution({
      stripe_customer_id: event.stripe_customer_id,
      stripe_subscription_id: event.stripe_subscription_id,
      user_id: event.user_id,
      account_id: event.account_id,
      email: event.user_email,
    });

    const stitched: StitchedEvent = {
      ...event,
      attribution,
    };

    const deliveries = await dispatchEvent(stitched);

    return NextResponse.json({
      replayed: true,
      eventId: event.event_id,
      attributed: Boolean(attribution),
      deliveries,
    });
  } catch (error) {
    console.error("Replay failed", error);
    return NextResponse.json({ error: "Replay failed" }, { status: 500 });
  }
}
