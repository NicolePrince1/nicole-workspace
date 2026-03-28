import { NextRequest, NextResponse } from "next/server";
import { verifyIngestKey } from "@/lib/auth";
import {
  attributionCaptureSchema,
  insertAttributionCapture,
} from "@/lib/attribution";

export const runtime = "nodejs";

/**
 * POST /api/attribution/capture
 *
 * Lightweight endpoint for capturing attribution identifiers.
 * Call this from the app frontend/backend when you know the user's
 * UTMs, click IDs, or identity keys. These records are later stitched
 * onto Stripe lifecycle events before downstream delivery.
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

  const parsed = attributionCaptureSchema.safeParse(body);
  if (!parsed.success) {
    return NextResponse.json(
      { error: "Validation failed", issues: parsed.error.issues },
      { status: 422 },
    );
  }

  // Enrich with request headers if not provided
  const capture = parsed.data;
  if (!capture.client_ip) {
    capture.client_ip =
      request.headers.get("x-forwarded-for")?.split(",")[0]?.trim() ??
      request.headers.get("x-real-ip") ??
      undefined;
  }
  if (!capture.user_agent) {
    capture.user_agent = request.headers.get("user-agent") ?? undefined;
  }

  try {
    const id = await insertAttributionCapture(capture);
    return NextResponse.json({ captured: true, id }, { status: 201 });
  } catch (error) {
    console.error("Attribution capture failed", error);
    return NextResponse.json(
      { error: "Internal server error" },
      { status: 500 },
    );
  }
}
