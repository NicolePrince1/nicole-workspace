import { createHash } from "node:crypto";
import type { CanonicalEvent, CanonicalEventType } from "@/lib/canonical-events";
import { getServerEnv } from "@/lib/env";
import type { DeliveryResult } from "@/lib/delivery";

const META_EVENT_MAP: Partial<Record<CanonicalEventType, string>> = {
  signup_started: "Lead",
  email_verified: "CompleteRegistration",
  trial_started: "StartTrial",
  subscription_started: "Subscribe",
  invoice_paid: "Purchase",
};

function sha256(value: string) {
  return createHash("sha256").update(value.trim().toLowerCase()).digest("hex");
}

export async function deliverToMeta(event: CanonicalEvent): Promise<DeliveryResult> {
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

  const userData: Record<string, string> = {};

  if (event.user_email) {
    userData.em = sha256(event.user_email);
  }

  if (event.user_id) {
    userData.external_id = sha256(event.user_id);
  } else if (event.account_id) {
    userData.external_id = sha256(event.account_id);
  }

  if (event.fbp) {
    userData.fbp = event.fbp;
  }

  if (event.fbc) {
    userData.fbc = event.fbc;
  }

  if (event.client_ip) {
    userData.client_ip_address = event.client_ip;
  }

  if (event.client_user_agent) {
    userData.client_user_agent = event.client_user_agent;
  }

  const requestPayload = {
    data: [
      {
        event_name: metaEventName,
        event_time: Math.floor(new Date(event.occurred_at).getTime() / 1000),
        event_id: event.event_id,
        action_source: "website",
        event_source_url: event.page_location ?? undefined,
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
        headers: {
          "Content-Type": "application/json",
        },
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
