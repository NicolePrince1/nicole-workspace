import type { CanonicalEvent, CanonicalEventType } from "@/lib/canonical-events";
import { getServerEnv } from "@/lib/env";
import type { DeliveryResult } from "@/lib/delivery";

const GOOGLE_ADS_EVENT_MAP: Partial<Record<CanonicalEventType, string>> = {
  trial_started: "Trial Started",
  subscription_started: "Subscription Started",
  invoice_paid: "Invoice Paid",
};

export async function deliverToGoogleAds(event: CanonicalEvent): Promise<DeliveryResult> {
  const env = getServerEnv();
  const destinationEventName = GOOGLE_ADS_EVENT_MAP[event.event_type];

  if (!destinationEventName) {
    return {
      platform: "google_ads",
      status: "skipped",
      error: `No Google Ads mapping for ${event.event_type}`,
    };
  }

  if (
    !env.GOOGLE_ADS_CUSTOMER_ID ||
    !env.GOOGLE_ADS_DEVELOPER_TOKEN ||
    !env.GOOGLE_ADS_REFRESH_TOKEN ||
    !env.GOOGLE_ADS_CONVERSION_ACTION_ID
  ) {
    return {
      platform: "google_ads",
      status: "disabled",
      destinationEventName,
      error:
        "Google Ads is not fully configured. Expected GOOGLE_ADS_CUSTOMER_ID, GOOGLE_ADS_DEVELOPER_TOKEN, GOOGLE_ADS_REFRESH_TOKEN, and GOOGLE_ADS_CONVERSION_ACTION_ID.",
    };
  }

  const clickIdentifier = event.gclid ?? event.gbraid ?? event.wbraid;

  if (!clickIdentifier) {
    return {
      platform: "google_ads",
      status: "skipped",
      destinationEventName,
      error: "No gclid, gbraid, or wbraid was captured for this event",
    };
  }

  const requestPayload = {
    customerId: env.GOOGLE_ADS_CUSTOMER_ID,
    loginCustomerId: env.GOOGLE_ADS_LOGIN_CUSTOMER_ID,
    conversionActionId: env.GOOGLE_ADS_CONVERSION_ACTION_ID,
    eventName: destinationEventName,
    clickIdentifier,
    eventId: event.event_id,
    occurredAt: event.occurred_at,
    value: event.amount_cents != null ? event.amount_cents / 100 : undefined,
    currency: event.currency ?? undefined,
  };

  return {
    platform: "google_ads",
    status: "disabled",
    destinationEventName,
    requestPayload,
    error:
      "Google Ads delivery wiring is prepared, but live upload remains intentionally disabled until account/API access is confirmed.",
  };
}
