import { PRIMARY_EVENT_TYPES } from "@/lib/canonical-events";
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
  recentEvents: Array<{
    id: string;
    event_type: string;
    event_id: string;
    source: string;
    user_email: string | null;
    session_source: string | null;
    session_medium: string | null;
    session_campaign: string | null;
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
  const keyCounts = PRIMARY_EVENT_TYPES.map((eventType) => ({
    eventType,
    count: 0,
  }));

  if (!env.DATABASE_URL) {
    return {
      dbOk: false,
      env,
      keyCounts,
      recentEvents: [],
      recentDeliveries: [],
    };
  }

  try {
    await ensureTables();
    const db = sql();

    const counts = await db<EventCountRow[]>`
      SELECT event_type, COUNT(*)::text AS count
      FROM events
      WHERE occurred_at >= now() - interval '7 days'
      GROUP BY event_type
    `;

    const countMap = new Map(counts.map((row) => [row.event_type, Number(row.count)]));

    const recentEvents = (await db`
      SELECT
        id::text,
        event_type,
        event_id,
        source,
        user_email,
        session_source,
        session_medium,
        session_campaign,
        occurred_at::text
      FROM events
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
      recentEvents,
      recentDeliveries,
    };
  } catch (error) {
    console.error("Dashboard query failed", error);

    return {
      dbOk: false,
      env,
      keyCounts,
      recentEvents: [],
      recentDeliveries: [],
    };
  }
}
