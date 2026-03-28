import { STRIPE_LIFECYCLE_TYPES } from "@/lib/stripe-events";
import { ensureTables, sql } from "@/lib/db";
import { envReadiness } from "@/lib/env";

interface EventCountRow {
  event_type: string;
  count: string;
}

export interface DashboardData {
  dbOk: boolean;
  env: ReturnType<typeof envReadiness>;
  keyCounts: { eventType: string; count: number }[];
  attributionCaptures7d: number;
  attributedTrialStarts7d: number;
  unattributedTrialStarts7d: number;
  trialAttributionMatchRate: number;
  recentEvents: Array<{
    id: string;
    event_type: string;
    event_id: string;
    source: string;
    user_email: string | null;
    stripe_customer_id: string | null;
    stripe_subscription_id: string | null;
    attributed: boolean;
    occurred_at: string;
  }>;
  recentDeliveries: Array<{
    id: string;
    event_id: string;
    platform: string;
    destination_event_name: string | null;
    status: string;
    response_code: number | null;
    error: string | null;
    created_at: string;
  }>;
}

export async function getDashboardData(): Promise<DashboardData> {
  const env = envReadiness();
  const keyCounts = STRIPE_LIFECYCLE_TYPES.map((eventType) => ({
    eventType,
    count: 0,
  }));

  if (!env.DATABASE_URL) {
    return {
      dbOk: false,
      env,
      keyCounts,
      attributionCaptures7d: 0,
      attributedTrialStarts7d: 0,
      unattributedTrialStarts7d: 0,
      trialAttributionMatchRate: 0,
      recentEvents: [],
      recentDeliveries: [],
    };
  }

  try {
    await ensureTables();
    const db = sql();

    const counts = await db<EventCountRow[]>`
      SELECT event_type, COUNT(*)::text AS count
      FROM stripe_lifecycle_events
      WHERE occurred_at >= now() - interval '7 days'
      GROUP BY event_type
    `;

    const countMap = new Map(counts.map((row) => [row.event_type, Number(row.count)]));

    const captureRows = await db<{ count: string }[]>`
      SELECT COUNT(*)::text AS count
      FROM attribution_captures
      WHERE captured_at >= now() - interval '7 days'
    `;

    const trialRows = await db<{ attributed: boolean; count: string }[]>`
      SELECT attributed, COUNT(*)::text AS count
      FROM stripe_lifecycle_events
      WHERE event_type = 'trial_started'
        AND occurred_at >= now() - interval '7 days'
      GROUP BY attributed
    `;

    const trialMap = new Map(trialRows.map((row) => [String(row.attributed), Number(row.count)]));
    const attributedTrialStarts7d = trialMap.get("true") ?? 0;
    const unattributedTrialStarts7d = trialMap.get("false") ?? 0;
    const totalTrialStarts7d = attributedTrialStarts7d + unattributedTrialStarts7d;

    const recentEvents = (await db`
      SELECT
        id::text,
        event_type,
        event_id,
        source,
        user_email,
        stripe_customer_id,
        stripe_subscription_id,
        attributed,
        occurred_at::text
      FROM stripe_lifecycle_events
      ORDER BY occurred_at DESC
      LIMIT 20
    `) as DashboardData["recentEvents"];

    const recentDeliveries = (await db`
      SELECT
        id::text,
        event_id,
        platform,
        destination_event_name,
        status,
        response_code,
        error,
        created_at::text
      FROM delivery_attempts
      ORDER BY created_at DESC
      LIMIT 20
    `) as DashboardData["recentDeliveries"];

    return {
      dbOk: true,
      env,
      keyCounts: keyCounts.map((item) => ({
        eventType: item.eventType,
        count: countMap.get(item.eventType) ?? 0,
      })),
      attributionCaptures7d: Number(captureRows[0]?.count ?? 0),
      attributedTrialStarts7d,
      unattributedTrialStarts7d,
      trialAttributionMatchRate:
        totalTrialStarts7d === 0 ? 0 : attributedTrialStarts7d / totalTrialStarts7d,
      recentEvents,
      recentDeliveries,
    };
  } catch (error) {
    console.error("Dashboard query failed", error);

    return {
      dbOk: false,
      env,
      keyCounts,
      attributionCaptures7d: 0,
      attributedTrialStarts7d: 0,
      unattributedTrialStarts7d: 0,
      trialAttributionMatchRate: 0,
      recentEvents: [],
      recentDeliveries: [],
    };
  }
}
