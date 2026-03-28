import { NextRequest, NextResponse } from "next/server";
import { verifyIngestKey } from "@/lib/auth";
import { canonicalEventSchema } from "@/lib/canonical-events";
import { recordEvent } from "@/lib/record-event";

export const runtime = "nodejs";

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

  const parsed = canonicalEventSchema.safeParse(body);
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
    const result = await recordEvent(parsed.data);

    return NextResponse.json(result, {
      status: result.inserted ? 201 : 200,
    });
  } catch (error) {
    console.error("Event ingest failed", error);
    return NextResponse.json({ error: "Internal server error" }, { status: 500 });
  }
}
