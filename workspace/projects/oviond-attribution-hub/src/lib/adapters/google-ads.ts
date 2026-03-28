import type { StitchedEvent } from "@/lib/stitched-event";
import type { StripeLifecycleType } from "@/lib/stripe-events";
import { getServerEnv } from "@/lib/env";
import type { DeliveryResult } from "@/lib/delivery";

const GOOGLE_ADS_EVENT_MAP: Partial<Record<StripeLifecycleType, string>> = {
  trial_started: "Trial Started",
  subscription_started: "Subscription Started",
  invoice_paid: "Invoice Paid",
};

export async function deliverToGoogleAds(event: StitchedEvent): Promise<DeliveryResult> {
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

  const attr = event.attribution;
  const clickIdentifier = attr?.gclid ?? attr?.gbraid ?? attr?.wbraid;

  if (!clickIdentifier) {
    return {
      platform: "google_ads",
      status: "skipped",
      destinationEventName,
      error: "No gclid, gbraid, or wbraid was found in stitched attribution",
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
