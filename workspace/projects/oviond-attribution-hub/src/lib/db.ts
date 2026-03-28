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

  await db`
    CREATE TABLE IF NOT EXISTS events (
      id BIGSERIAL PRIMARY KEY,
      event_id TEXT UNIQUE NOT NULL,
      event_type TEXT NOT NULL,
      source TEXT NOT NULL DEFAULT 'api',
      occurred_at TIMESTAMPTZ NOT NULL DEFAULT now(),
      user_id TEXT,
      user_email TEXT,
      account_id TEXT,
      plan_name TEXT,
      trial_days INTEGER,
      billing_model TEXT,
      amount_cents INTEGER,
      currency TEXT,
      page_path TEXT,
      page_location TEXT,
      landing_page TEXT,
      session_source TEXT,
      session_medium TEXT,
      session_campaign TEXT,
      utm_source TEXT,
      utm_medium TEXT,
      utm_campaign TEXT,
      utm_content TEXT,
      utm_term TEXT,
      fbclid TEXT,
      fbp TEXT,
      fbc TEXT,
      gclid TEXT,
      gbraid TEXT,
      wbraid TEXT,
      client_ip TEXT,
      client_user_agent TEXT,
      raw_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
      created_at TIMESTAMPTZ NOT NULL DEFAULT now()
    )
  `;

  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS occurred_at TIMESTAMPTZ NOT NULL DEFAULT now()`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS user_id TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS user_email TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS account_id TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS plan_name TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS trial_days INTEGER`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS billing_model TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS amount_cents INTEGER`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS currency TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS page_path TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS page_location TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS landing_page TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS session_source TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS session_medium TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS session_campaign TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS utm_source TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS utm_medium TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS utm_campaign TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS utm_content TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS utm_term TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS fbclid TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS fbp TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS fbc TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS gclid TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS gbraid TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS wbraid TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS client_ip TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS client_user_agent TEXT`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS raw_payload JSONB NOT NULL DEFAULT '{}'::jsonb`;
  await db`ALTER TABLE events ADD COLUMN IF NOT EXISTS created_at TIMESTAMPTZ NOT NULL DEFAULT now()`;

  await db`CREATE INDEX IF NOT EXISTS idx_events_event_type ON events (event_type)`;
  await db`CREATE INDEX IF NOT EXISTS idx_events_occurred_at ON events (occurred_at DESC)`;
  await db`CREATE INDEX IF NOT EXISTS idx_events_created_at ON events (created_at DESC)`;
  await db`CREATE INDEX IF NOT EXISTS idx_events_source ON events (source)`;

  await db`
    CREATE TABLE IF NOT EXISTS delivery_attempts (
      id BIGSERIAL PRIMARY KEY,
      event_id TEXT NOT NULL REFERENCES events(event_id) ON DELETE CASCADE,
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

  await db`ALTER TABLE delivery_attempts ADD COLUMN IF NOT EXISTS destination_event_name TEXT`;
  await db`ALTER TABLE delivery_attempts ADD COLUMN IF NOT EXISTS request_payload JSONB`;
  await db`ALTER TABLE delivery_attempts ADD COLUMN IF NOT EXISTS response_code INTEGER`;
  await db`ALTER TABLE delivery_attempts ADD COLUMN IF NOT EXISTS response_body TEXT`;
  await db`ALTER TABLE delivery_attempts ADD COLUMN IF NOT EXISTS error TEXT`;
  await db`ALTER TABLE delivery_attempts ADD COLUMN IF NOT EXISTS created_at TIMESTAMPTZ NOT NULL DEFAULT now()`;

  await db`CREATE INDEX IF NOT EXISTS idx_delivery_attempts_event_id ON delivery_attempts (event_id)`;
  await db`CREATE INDEX IF NOT EXISTS idx_delivery_attempts_platform ON delivery_attempts (platform)`;
  await db`CREATE INDEX IF NOT EXISTS idx_delivery_attempts_created_at ON delivery_attempts (created_at DESC)`;

  schemaReady = true;
}
