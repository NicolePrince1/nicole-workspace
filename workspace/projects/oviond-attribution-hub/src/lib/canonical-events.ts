import { randomUUID } from "node:crypto";
import { z } from "zod";

export const CANONICAL_EVENT_TYPES = [
  "trial_started",
  "subscription_started",
  "invoice_paid",
  "trial_expired",
  "subscription_cancelled",
  "signup_started",
  "email_verified",
] as const;

export const PRIMARY_EVENT_TYPES: readonly CanonicalEventType[] = [
  "signup_started",
  "email_verified",
  "trial_started",
  "subscription_started",
  "invoice_paid",
  "trial_expired",
  "subscription_cancelled",
] as const;

export type CanonicalEventType = (typeof CANONICAL_EVENT_TYPES)[number];

const canonicalEventInputSchema = z.object({
  event_type: z.enum(CANONICAL_EVENT_TYPES),
  event_id: z.string().trim().min(1).max(256).optional(),
  source: z.string().trim().min(1).max(64).default("api"),
  occurred_at: z.coerce.date().optional(),
  user_id: z.string().trim().min(1).max(256).optional(),
  user_email: z.string().trim().email().optional(),
  account_id: z.string().trim().min(1).max(256).optional(),
  plan_name: z.string().trim().min(1).max(128).optional(),
  trial_days: z.number().int().min(0).max(365).optional(),
  billing_model: z.string().trim().min(1).max(64).optional(),
  amount_cents: z.number().int().min(0).optional(),
  currency: z.string().trim().length(3).optional(),
  page_path: z.string().trim().max(512).optional(),
  page_location: z.string().trim().max(2048).optional(),
  landing_page: z.string().trim().max(2048).optional(),
  session_source: z.string().trim().max(256).optional(),
  session_medium: z.string().trim().max(256).optional(),
  session_campaign: z.string().trim().max(256).optional(),
  utm_source: z.string().trim().max(256).optional(),
  utm_medium: z.string().trim().max(256).optional(),
  utm_campaign: z.string().trim().max(256).optional(),
  utm_content: z.string().trim().max(256).optional(),
  utm_term: z.string().trim().max(256).optional(),
  fbclid: z.string().trim().max(512).optional(),
  fbp: z.string().trim().max(512).optional(),
  fbc: z.string().trim().max(512).optional(),
  gclid: z.string().trim().max(512).optional(),
  gbraid: z.string().trim().max(512).optional(),
  wbraid: z.string().trim().max(512).optional(),
  client_ip: z.string().trim().max(128).optional(),
  client_user_agent: z.string().trim().max(2048).optional(),
  raw_payload: z.record(z.string(), z.unknown()).optional(),
});

export const canonicalEventSchema = canonicalEventInputSchema.transform((value) => ({
  ...value,
  event_id: value.event_id ?? randomUUID(),
  occurred_at: (value.occurred_at ?? new Date()).toISOString(),
  currency: value.currency?.toUpperCase(),
  user_email: value.user_email?.toLowerCase(),
  raw_payload: value.raw_payload ?? {},
}));

export type CanonicalEventInput = z.input<typeof canonicalEventSchema>;
export type CanonicalEvent = z.output<typeof canonicalEventSchema>;
