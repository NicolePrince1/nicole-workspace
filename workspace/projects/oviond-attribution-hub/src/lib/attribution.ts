import { randomUUID } from "node:crypto";
import { z } from "zod";
import { ensureTables, sql } from "@/lib/db";

/**
 * Attribution capture schema.
 * These records are collected from the frontend / app backend and later
 * stitched onto Stripe lifecycle events for downstream delivery.
 */
export const attributionCaptureSchema = z
  .object({
    // Identity keys (at least one should be provided for stitching)
    email: z.string().trim().email().optional(),
    user_id: z.string().trim().min(1).max(256).optional(),
    account_id: z.string().trim().min(1).max(256).optional(),
    stripe_customer_id: z.string().trim().min(1).max(256).optional(),
    stripe_subscription_id: z.string().trim().min(1).max(256).optional(),

    // UTM parameters
    utm_source: z.string().trim().max(256).optional(),
    utm_medium: z.string().trim().max(256).optional(),
    utm_campaign: z.string().trim().max(256).optional(),
    utm_content: z.string().trim().max(256).optional(),
    utm_term: z.string().trim().max(256).optional(),

    // Ad click identifiers
    fbclid: z.string().trim().max(512).optional(),
    fbc: z.string().trim().max(512).optional(),
    fbp: z.string().trim().max(512).optional(),
    gclid: z.string().trim().max(512).optional(),
    gbraid: z.string().trim().max(512).optional(),
    wbraid: z.string().trim().max(512).optional(),

    // Page context
    landing_page: z.string().trim().max(2048).optional(),
    page_path: z.string().trim().max(512).optional(),
    page_location: z.string().trim().max(2048).optional(),
    referrer: z.string().trim().max(2048).optional(),

    // Client info (can also be set server-side from request headers)
    client_ip: z.string().trim().max(128).optional(),
    user_agent: z.string().trim().max(2048).optional(),

    // Optional raw dump
    raw_payload: z.record(z.string(), z.unknown()).optional(),
  })
  .transform((v) => ({
    ...v,
    email: v.email?.toLowerCase(),
    raw_payload: v.raw_payload ?? {},
  }));

export type AttributionCaptureInput = z.input<typeof attributionCaptureSchema>;
export type AttributionCapture = z.output<typeof attributionCaptureSchema>;

/**
 * Insert an attribution capture into Postgres.
 */
export async function insertAttributionCapture(capture: AttributionCapture) {
  await ensureTables();
  const db = sql();
  const id = randomUUID();

  await db`
    INSERT INTO attribution_captures (
      id, email, user_id, account_id,
      stripe_customer_id, stripe_subscription_id,
      utm_source, utm_medium, utm_campaign, utm_content, utm_term,
      fbclid, fbc, fbp, gclid, gbraid, wbraid,
      landing_page, page_path, page_location, referrer,
      client_ip, user_agent, raw_payload
    ) VALUES (
      ${id},
      ${capture.email ?? null},
      ${capture.user_id ?? null},
      ${capture.account_id ?? null},
      ${capture.stripe_customer_id ?? null},
      ${capture.stripe_subscription_id ?? null},
      ${capture.utm_source ?? null},
      ${capture.utm_medium ?? null},
      ${capture.utm_campaign ?? null},
      ${capture.utm_content ?? null},
      ${capture.utm_term ?? null},
      ${capture.fbclid ?? null},
      ${capture.fbc ?? null},
      ${capture.fbp ?? null},
      ${capture.gclid ?? null},
      ${capture.gbraid ?? null},
      ${capture.wbraid ?? null},
      ${capture.landing_page ?? null},
      ${capture.page_path ?? null},
      ${capture.page_location ?? null},
      ${capture.referrer ?? null},
      ${capture.client_ip ?? null},
      ${capture.user_agent ?? null},
      ${JSON.stringify(capture.raw_payload)}
    )
  `;

  return id;
}

/**
 * Stitched attribution: the attribution data joined onto a Stripe lifecycle event.
 */
export interface StitchedAttribution {
  utm_source?: string;
  utm_medium?: string;
  utm_campaign?: string;
  utm_content?: string;
  utm_term?: string;
  fbclid?: string;
  fbc?: string;
  fbp?: string;
  gclid?: string;
  gbraid?: string;
  wbraid?: string;
  landing_page?: string;
  page_path?: string;
  page_location?: string;
  referrer?: string;
  client_ip?: string;
  user_agent?: string;
}

/**
 * Find the best matching attribution capture for a Stripe lifecycle event.
 *
 * Priority order:
 *  1. stripe_customer_id (explicit match)
 *  2. stripe_subscription_id
 *  3. user_id or account_id
 *  4. email
 *
 * Within each tier, pick the most recent capture (captured_at DESC).
 */
export async function stitchAttribution(keys: {
  stripe_customer_id?: string;
  stripe_subscription_id?: string;
  user_id?: string;
  account_id?: string;
  email?: string;
}): Promise<StitchedAttribution | null> {
  await ensureTables();
  const db = sql();

  // Build prioritised queries — first match wins
  const matchers: Array<{ column: string; value: string | undefined }> = [
    { column: "stripe_customer_id", value: keys.stripe_customer_id },
    { column: "stripe_subscription_id", value: keys.stripe_subscription_id },
    { column: "user_id", value: keys.user_id },
    { column: "account_id", value: keys.account_id },
    { column: "email", value: keys.email },
  ];

  for (const matcher of matchers) {
    if (!matcher.value) continue;

    const rows = await db`
      SELECT
        utm_source, utm_medium, utm_campaign, utm_content, utm_term,
        fbclid, fbc, fbp, gclid, gbraid, wbraid,
        landing_page, page_path, page_location, referrer,
        client_ip, user_agent
      FROM attribution_captures
      WHERE ${db(matcher.column)} = ${matcher.value}
      ORDER BY captured_at DESC
      LIMIT 1
    `;

    if (rows.length > 0) {
      const row = rows[0];
      return {
        utm_source: row.utm_source ?? undefined,
        utm_medium: row.utm_medium ?? undefined,
        utm_campaign: row.utm_campaign ?? undefined,
        utm_content: row.utm_content ?? undefined,
        utm_term: row.utm_term ?? undefined,
        fbclid: row.fbclid ?? undefined,
        fbc: row.fbc ?? undefined,
        fbp: row.fbp ?? undefined,
        gclid: row.gclid ?? undefined,
        gbraid: row.gbraid ?? undefined,
        wbraid: row.wbraid ?? undefined,
        landing_page: row.landing_page ?? undefined,
        page_path: row.page_path ?? undefined,
        page_location: row.page_location ?? undefined,
        referrer: row.referrer ?? undefined,
        client_ip: row.client_ip ?? undefined,
        user_agent: row.user_agent ?? undefined,
      };
    }
  }

  return null;
}
