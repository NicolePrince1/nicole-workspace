import { createHash } from "node:crypto";
import type { StitchedEvent } from "@/lib/stitched-event";
import type { StripeLifecycleType } from "@/lib/stripe-events";
import { getServerEnv } from "@/lib/env";
import type { DeliveryResult } from "@/lib/delivery";

const META_EVENT_MAP: Partial<Record<StripeLifecycleType, string>> = {
  trial_started: "StartTrial",
  subscription_started: "Subscribe",
  invoice_paid: "Purchase",
};

function sha256(value: string) {
  return createHash("sha256").update(value.trim().toLowerCase()).digest("hex");
}

export async function deliverToMeta(event: StitchedEvent): Promise<DeliveryResult> {
  const env = getServerEnv();
  const pixelId = env.META_PIXEL_ID;
  const accessToken = env.META_ACCESS_TOKEN;
  const metaEventName = META_EVENT_MAP[event.event_type];

  if (!pixelId || !accessToken) {
    return {
      platform: "meta",
      status: "disabled",
      error: "META_PIXEL_ID or META_ACCESS_TOKEN is not configured",
    };
  }

  if (!metaEventName) {
    return {
      platform: "meta",
      status: "skipped",
      error: `No Meta event mapping for ${event.event_type}`,
    };
  }

  const attr = event.attribution;
  const userData: Record<string, string> = {};

  if (event.user_email) {
    userData.em = sha256(event.user_email);
  }

  if (event.stripe_customer_id) {
    userData.external_id = sha256(event.stripe_customer_id);
  } else if (event.user_id) {
    userData.external_id = sha256(event.user_id);
  } else if (event.account_id) {
    userData.external_id = sha256(event.account_id);
  }

  if (attr?.fbp) userData.fbp = attr.fbp;
  if (attr?.fbc) userData.fbc = attr.fbc;
  if (attr?.client_ip) userData.client_ip_address = attr.client_ip;
  if (attr?.user_agent) userData.client_user_agent = attr.user_agent;

  const requestPayload = {
    data: [
      {
        event_name: metaEventName,
        event_time: Math.floor(new Date(event.occurred_at).getTime() / 1000),
        event_id: event.event_id,
        action_source: "website",
        event_source_url: attr?.page_location ?? undefined,
        user_data: userData,
        custom_data: {
          value: event.amount_cents != null ? event.amount_cents / 100 : undefined,
          currency: event.currency ?? undefined,
          plan_name: event.plan_name ?? undefined,
          billing_model: event.billing_model ?? undefined,
        },
      },
    ],
  };

  try {
    const response = await fetch(
      `https://graph.facebook.com/v19.0/${pixelId}/events?access_token=${accessToken}`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(requestPayload),
      },
    );

    const responseBody = await response.text();

    return {
      platform: "meta",
      status: response.ok ? "sent" : "error",
      destinationEventName: metaEventName,
      requestPayload,
      responseCode: response.status,
      responseBody: responseBody.slice(0, 4000),
      error: response.ok ? undefined : `Meta rejected ${metaEventName}`,
    };
  } catch (error) {
    return {
      platform: "meta",
      status: "error",
      destinationEventName: metaEventName,
      requestPayload,
      error: error instanceof Error ? error.message : String(error),
    };
  }
}
