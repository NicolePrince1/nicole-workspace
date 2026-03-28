import { NextRequest, NextResponse } from "next/server";
import { getServerEnv } from "@/lib/env";
import { setAdminCookie } from "@/lib/auth";

export const runtime = "nodejs";

export async function POST(request: NextRequest) {
  const env = getServerEnv();

  if (!env.ADMIN_TOKEN) {
    return NextResponse.redirect(new URL("/", request.url));
  }

  const contentType = request.headers.get("content-type") ?? "";
  let submittedToken = "";

  if (contentType.includes("application/json")) {
    const body = await request.json().catch(() => ({}));
    submittedToken = typeof body?.token === "string" ? body.token : "";
  } else {
    const form = await request.formData();
    submittedToken = String(form.get("token") ?? "");
  }

  if (submittedToken !== env.ADMIN_TOKEN) {
    return NextResponse.redirect(new URL("/?login=failed", request.url));
  }

  const response = NextResponse.redirect(new URL("/", request.url));
  setAdminCookie(response, env.ADMIN_TOKEN);
  return response;
}
