import { NextRequest, NextResponse } from "next/server";
import { verifyAdminRequest } from "@/lib/auth";
import { ensureTables, sql } from "@/lib/db";
import { dispatchEvent } from "@/lib/dispatch";
import { canonicalEventSchema } from "@/lib/canonical-events";

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
      FROM events
      WHERE event_id = ${body.eventId}
      LIMIT 1
    `;

    const row = rows[0];
    if (!row) {
      return NextResponse.json({ error: "Event not found" }, { status: 404 });
    }

    const event = canonicalEventSchema.parse({
      event_type: row.event_type,
      event_id: row.event_id,
      source: row.source,
      occurred_at: row.occurred_at,
      user_id: row.user_id ?? undefined,
      user_email: row.user_email ?? undefined,
      account_id: row.account_id ?? undefined,
      plan_name: row.plan_name ?? undefined,
      trial_days: row.trial_days ?? undefined,
      billing_model: row.billing_model ?? undefined,
      amount_cents: row.amount_cents ?? undefined,
      currency: row.currency ?? undefined,
      page_path: row.page_path ?? undefined,
      page_location: row.page_location ?? undefined,
      landing_page: row.landing_page ?? undefined,
      session_source: row.session_source ?? undefined,
      session_medium: row.session_medium ?? undefined,
      session_campaign: row.session_campaign ?? undefined,
      utm_source: row.utm_source ?? undefined,
      utm_medium: row.utm_medium ?? undefined,
      utm_campaign: row.utm_campaign ?? undefined,
      utm_content: row.utm_content ?? undefined,
      utm_term: row.utm_term ?? undefined,
      fbclid: row.fbclid ?? undefined,
      fbp: row.fbp ?? undefined,
      fbc: row.fbc ?? undefined,
      gclid: row.gclid ?? undefined,
      gbraid: row.gbraid ?? undefined,
      wbraid: row.wbraid ?? undefined,
      client_ip: row.client_ip ?? undefined,
      client_user_agent: row.client_user_agent ?? undefined,
      raw_payload: row.raw_payload ?? {},
    });

    const deliveries = await dispatchEvent(event);

    return NextResponse.json({
      replayed: true,
      eventId: event.event_id,
      deliveries,
    });
  } catch (error) {
    console.error("Replay failed", error);
    return NextResponse.json({ error: "Replay failed" }, { status: 500 });
  }
}
