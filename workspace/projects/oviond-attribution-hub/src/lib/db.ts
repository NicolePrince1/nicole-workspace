import postgres from "postgres";
import { getServerEnv } from "@/lib/env";

let client: ReturnType<typeof postgres> | null = null;
let schemaReady = false;

export function sql() {
  if (client) {
    return client;
  }

  const env = getServerEnv();
  if (!env.DATABASE_URL) {
    throw new Error("DATABASE_URL is not configured");
  }

  client = postgres(env.DATABASE_URL, {
    max: 5,
    prepare: false,
  });

  return client;
}

export async function ensureTables() {
  if (schemaReady) {
    return;
  }

  const db = sql();

  // ── Stripe lifecycle events (source of truth) ────────────────────────
  await db`
    CREATE TABLE IF NOT EXISTS stripe_lifecycle_events (
      id BIGSERIAL PRIMARY KEY,
      event_id TEXT UNIQUE NOT NULL,
      event_type TEXT NOT NULL,
      source TEXT NOT NULL DEFAULT 'stripe',
      occurred_at TIMESTAMPTZ NOT NULL DEFAULT now(),
      stripe_customer_id TEXT,
      stripe_subscription_id TEXT,
      user_id TEXT,
      user_email TEXT,
      account_id TEXT,
      plan_name TEXT,
      trial_days INTEGER,
      billing_model TEXT,
      amount_cents INTEGER,
      currency TEXT,
      attributed BOOLEAN NOT NULL DEFAULT false,
      raw_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
      created_at TIMESTAMPTZ NOT NULL DEFAULT now()
    )
  `;

  // Idempotent column additions for future-proofing
  await db`ALTER TABLE stripe_lifecycle_events ADD COLUMN IF NOT EXISTS stripe_customer_id TEXT`;
  await db`ALTER TABLE stripe_lifecycle_events ADD COLUMN IF NOT EXISTS stripe_subscription_id TEXT`;
  await db`ALTER TABLE stripe_lifecycle_events ADD COLUMN IF NOT EXISTS attributed BOOLEAN NOT NULL DEFAULT false`;

  await db`CREATE INDEX IF NOT EXISTS idx_sle_event_type ON stripe_lifecycle_events (event_type)`;
  await db`CREATE INDEX IF NOT EXISTS idx_sle_occurred_at ON stripe_lifecycle_events (occurred_at DESC)`;
  await db`CREATE INDEX IF NOT EXISTS idx_sle_created_at ON stripe_lifecycle_events (created_at DESC)`;
  await db`CREATE INDEX IF NOT EXISTS idx_sle_stripe_customer ON stripe_lifecycle_events (stripe_customer_id)`;

  // ── Attribution captures ─────────────────────────────────────────────
  await db`
    CREATE TABLE IF NOT EXISTS attribution_captures (
      id TEXT PRIMARY KEY,
      email TEXT,
      user_id TEXT,
      account_id TEXT,
      stripe_customer_id TEXT,
      stripe_subscription_id TEXT,
      utm_source TEXT,
      utm_medium TEXT,
      utm_campaign TEXT,
      utm_content TEXT,
      utm_term TEXT,
      fbclid TEXT,
      fbc TEXT,
      fbp TEXT,
      gclid TEXT,
      gbraid TEXT,
      wbraid TEXT,
      landing_page TEXT,
      page_path TEXT,
      page_location TEXT,
      referrer TEXT,
      client_ip TEXT,
      user_agent TEXT,
      raw_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
      captured_at TIMESTAMPTZ NOT NULL DEFAULT now()
    )
  `;

  await db`CREATE INDEX IF NOT EXISTS idx_ac_stripe_customer ON attribution_captures (stripe_customer_id)`;
  await db`CREATE INDEX IF NOT EXISTS idx_ac_stripe_subscription ON attribution_captures (stripe_subscription_id)`;
  await db`CREATE INDEX IF NOT EXISTS idx_ac_user_id ON attribution_captures (user_id)`;
  await db`CREATE INDEX IF NOT EXISTS idx_ac_account_id ON attribution_captures (account_id)`;
  await db`CREATE INDEX IF NOT EXISTS idx_ac_email ON attribution_captures (email)`;
  await db`CREATE INDEX IF NOT EXISTS idx_ac_captured_at ON attribution_captures (captured_at DESC)`;

  // ── Delivery attempts (downstream fan-out log) ───────────────────────
  await db`
    CREATE TABLE IF NOT EXISTS delivery_attempts (
      id BIGSERIAL PRIMARY KEY,
      event_id TEXT NOT NULL,
      platform TEXT NOT NULL,
      destination_event_name TEXT,
      status TEXT NOT NULL DEFAULT 'pending',
      request_payload JSONB,
      response_code INTEGER,
      response_body TEXT,
      error TEXT,
      created_at TIMESTAMPTZ NOT NULL DEFAULT now()
    )
  `;

  // Stripe-first refactor note:
  // Older versions of the app created delivery_attempts.event_id as a foreign key
  // to the legacy events table. The new model writes lifecycle truth to
  // stripe_lifecycle_events instead, so that FK must be removed or webhook writes fail.
  await db`ALTER TABLE delivery_attempts DROP CONSTRAINT IF EXISTS delivery_attempts_event_id_fkey`;

  await db`ALTER TABLE delivery_attempts ADD COLUMN IF NOT EXISTS destination_event_name TEXT`;
  await db`ALTER TABLE delivery_attempts ADD COLUMN IF NOT EXISTS request_payload JSONB`;
  await db`ALTER TABLE delivery_attempts ADD COLUMN IF NOT EXISTS response_code INTEGER`;
  await db`ALTER TABLE delivery_attempts ADD COLUMN IF NOT EXISTS response_body TEXT`;
  await db`ALTER TABLE delivery_attempts ADD COLUMN IF NOT EXISTS error TEXT`;

  await db`CREATE INDEX IF NOT EXISTS idx_delivery_attempts_event_id ON delivery_attempts (event_id)`;
  await db`CREATE INDEX IF NOT EXISTS idx_delivery_attempts_platform ON delivery_attempts (platform)`;
  await db`CREATE INDEX IF NOT EXISTS idx_delivery_attempts_created_at ON delivery_attempts (created_at DESC)`;

  schemaReady = true;
}
