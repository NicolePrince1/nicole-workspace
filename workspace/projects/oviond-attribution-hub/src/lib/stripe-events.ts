import { randomUUID } from "node:crypto";
import { z } from "zod";

/**
 * Stripe-first lifecycle event types.
 * These are the only lifecycle events the hub tracks — all derived from Stripe webhooks.
 */
export const STRIPE_LIFECYCLE_TYPES = [
  "trial_started",
  "subscription_started",
  "invoice_paid",
  "trial_expired",
  "subscription_cancelled",
] as const;

export type StripeLifecycleType = (typeof STRIPE_LIFECYCLE_TYPES)[number];

export const stripeLifecycleEventSchema = z
  .object({
    event_type: z.enum(STRIPE_LIFECYCLE_TYPES),
    event_id: z.string().trim().min(1).max(256).optional(),
    source: z.string().trim().min(1).max(64).default("stripe"),
    occurred_at: z.coerce.date().optional(),
    stripe_customer_id: z.string().trim().min(1).max(256).optional(),
    stripe_subscription_id: z.string().trim().min(1).max(256).optional(),
    user_email: z.string().trim().email().optional(),
    user_id: z.string().trim().min(1).max(256).optional(),
    account_id: z.string().trim().min(1).max(256).optional(),
    plan_name: z.string().trim().min(1).max(128).optional(),
    billing_model: z.string().trim().min(1).max(64).optional(),
    trial_days: z.number().int().min(0).max(365).optional(),
    amount_cents: z.number().int().min(0).optional(),
    currency: z.string().trim().length(3).optional(),
    raw_payload: z.record(z.string(), z.unknown()).optional(),
  })
  .transform((v) => ({
    ...v,
    event_id: v.event_id ?? randomUUID(),
    occurred_at: (v.occurred_at ?? new Date()).toISOString(),
    currency: v.currency?.toUpperCase(),
    user_email: v.user_email?.toLowerCase(),
    raw_payload: v.raw_payload ?? {},
  }));

export type StripeLifecycleEventInput = z.input<typeof stripeLifecycleEventSchema>;
export type StripeLifecycleEvent = z.output<typeof stripeLifecycleEventSchema>;
