import { cookies } from "next/headers";
import { NextRequest, NextResponse } from "next/server";
import { getServerEnv, isProduction } from "@/lib/env";

export const ADMIN_COOKIE_NAME = "admin_token";

function jsonError(message: string, status: number) {
  return NextResponse.json({ error: message }, { status });
}

export function verifyIngestKey(req: NextRequest) {
  const env = getServerEnv();
  if (!env.INGEST_API_KEY) {
    return jsonError("Ingest is not configured", 503);
  }

  const bearer = req.headers.get("authorization")?.replace(/^Bearer\s+/i, "");
  const headerKey = req.headers.get("x-ingest-key");
  const provided = bearer ?? headerKey ?? "";

  if (provided !== env.INGEST_API_KEY) {
    return jsonError("Unauthorized", 401);
  }

  return null;
}

export function verifyAdminRequest(req: NextRequest) {
  const env = getServerEnv();
  if (!env.ADMIN_TOKEN) {
    return null;
  }

  const bearer = req.headers.get("authorization")?.replace(/^Bearer\s+/i, "");
  const headerToken = req.headers.get("x-admin-token");
  const cookieToken = req.cookies.get(ADMIN_COOKIE_NAME)?.value;

  if ([bearer, headerToken, cookieToken].includes(env.ADMIN_TOKEN)) {
    return null;
  }

  return jsonError("Forbidden", 403);
}

export async function hasAdminSession() {
  const env = getServerEnv();
  if (!env.ADMIN_TOKEN) {
    return true;
  }

  const cookieStore = await cookies();
  return cookieStore.get(ADMIN_COOKIE_NAME)?.value === env.ADMIN_TOKEN;
}

export function setAdminCookie(response: NextResponse, token: string) {
  response.cookies.set({
    name: ADMIN_COOKIE_NAME,
    value: token,
    httpOnly: true,
    sameSite: "lax",
    secure: isProduction(),
    path: "/",
    maxAge: 60 * 60 * 24 * 14,
  });
}

export function clearAdminCookie(response: NextResponse) {
  response.cookies.set({
    name: ADMIN_COOKIE_NAME,
    value: "",
    httpOnly: true,
    sameSite: "lax",
    secure: isProduction(),
    path: "/",
    maxAge: 0,
  });
}
