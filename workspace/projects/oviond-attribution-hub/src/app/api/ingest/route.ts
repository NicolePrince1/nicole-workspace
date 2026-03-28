import { NextRequest, NextResponse } from "next/server";
import { verifyIngestKey } from "@/lib/auth";
import { stripeLifecycleEventSchema } from "@/lib/stripe-events";
import { recordStripeLifecycleEvent } from "@/lib/record-event";

export const runtime = "nodejs";

/**
 * POST /api/ingest
 *
 * Manual ingest of Stripe lifecycle events. In the new model, Stripe webhooks
 * are the primary source. This endpoint exists for backfills, testing, and
 * edge cases where you need to inject a lifecycle event directly.
 *
 * Requires INGEST_API_KEY bearer auth.
 */
export async function POST(request: NextRequest) {
  const authError = verifyIngestKey(request);
  if (authError) {
    return authError;
  }

  let body: unknown;
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "Invalid JSON body" }, { status: 400 });
  }

  const parsed = stripeLifecycleEventSchema.safeParse(body);
  if (!parsed.success) {
    return NextResponse.json(
      {
        error: "Validation failed",
        issues: parsed.error.issues,
      },
      { status: 422 },
    );
  }

  try {
    const result = await recordStripeLifecycleEvent(parsed.data);
    return NextResponse.json(result, {
      status: result.inserted ? 201 : 200,
    });
  } catch (error) {
    console.error("Event ingest failed", error);
    return NextResponse.json({ error: "Internal server error" }, { status: 500 });
  }
}
