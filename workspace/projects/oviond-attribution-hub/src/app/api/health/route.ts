import { NextResponse } from "next/server";
import { ensureTables, sql } from "@/lib/db";
import { envReadiness } from "@/lib/env";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function GET() {
  const env = envReadiness();

  let dbOk = false;
  try {
    if (env.DATABASE_URL) {
      await ensureTables();
      await sql()`SELECT 1`;
      dbOk = true;
    }
  } catch (error) {
    console.error("Health check DB failure", error);
    dbOk = false;
  }

  return NextResponse.json({
    status: dbOk || !env.DATABASE_URL ? "ok" : "degraded",
    timestamp: new Date().toISOString(),
    db: dbOk,
    env,
  });
}
