import type { CanonicalEvent } from "@/lib/canonical-events";
import { getServerEnv } from "@/lib/env";
import type { DeliveryResult } from "@/lib/delivery";

export async function deliverToGA4(event: CanonicalEvent): Promise<DeliveryResult> {
  const env = getServerEnv();

  if (!env.GA4_MEASUREMENT_ID || !env.GA4_API_SECRET) {
    return {
      platform: "ga4",
      status: "disabled",
      error: "GA4_MEASUREMENT_ID or GA4_API_SECRET is not configured",
    };
  }

  const requestPayload = {
    client_id: event.user_id ?? event.account_id ?? event.event_id,
    user_id: event.user_id ?? undefined,
    timestamp_micros: String(new Date(event.occurred_at).getTime() * 1000),
    events: [
      {
        name: event.event_type,
        params: {
          event_id: event.event_id,
          value: event.amount_cents != null ? event.amount_cents / 100 : undefined,
          currency: event.currency ?? undefined,
          source: event.source,
          plan_name: event.plan_name ?? undefined,
          billing_model: event.billing_model ?? undefined,
          account_id: event.account_id ?? undefined,
          session_source: event.session_source ?? event.utm_source ?? undefined,
          session_medium: event.session_medium ?? event.utm_medium ?? undefined,
          session_campaign: event.session_campaign ?? event.utm_campaign ?? undefined,
        },
      },
    ],
  };

  try {
    const response = await fetch(
      `https://www.google-analytics.com/mp/collect?measurement_id=${env.GA4_MEASUREMENT_ID}&api_secret=${env.GA4_API_SECRET}`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(requestPayload),
      },
    );

    const responseBody = await response.text();

    return {
      platform: "ga4",
      status: response.ok ? "sent" : "error",
      destinationEventName: event.event_type,
      requestPayload,
      responseCode: response.status,
      responseBody: responseBody.slice(0, 4000),
      error: response.ok ? undefined : "GA4 Measurement Protocol rejected the event",
    };
  } catch (error) {
    return {
      platform: "ga4",
      status: "error",
      destinationEventName: event.event_type,
      requestPayload,
      error: error instanceof Error ? error.message : String(error),
    };
  }
}
