import type { CanonicalEvent } from "@/lib/canonical-events";
import { sql } from "@/lib/db";
import { deliverToMeta } from "@/lib/adapters/meta";
import { deliverToGA4 } from "@/lib/adapters/ga4";
import { deliverToGoogleAds } from "@/lib/adapters/google-ads";
import type { DeliveryResult } from "@/lib/delivery";

const adapters = [deliverToMeta, deliverToGA4, deliverToGoogleAds] as const;

export async function dispatchEvent(event: CanonicalEvent) {
  const db = sql();
  const results: DeliveryResult[] = [];

  for (const adapter of adapters) {
    const result = await adapter(event);
    results.push(result);

    await db`
      INSERT INTO delivery_attempts (
        event_id,
        platform,
        destination_event_name,
        status,
        request_payload,
        response_code,
        response_body,
        error
      )
      VALUES (
        ${event.event_id},
        ${result.platform},
        ${result.destinationEventName ?? null},
        ${result.status},
        ${result.requestPayload ? JSON.stringify(result.requestPayload) : null},
        ${result.responseCode ?? null},
        ${result.responseBody ?? null},
        ${result.error ?? null}
      )
    `;
  }

  return results;
}
