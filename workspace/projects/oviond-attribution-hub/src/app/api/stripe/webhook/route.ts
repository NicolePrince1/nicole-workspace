import { NextRequest, NextResponse } from "next/server";
import Stripe from "stripe";
import { canonicalEventSchema, type CanonicalEventType } from "@/lib/canonical-events";
import { getServerEnv } from "@/lib/env";
import { recordEvent } from "@/lib/record-event";

export const runtime = "nodejs";

const env = getServerEnv();
const stripe = new Stripe(env.STRIPE_SECRET_KEY ?? "sk_not_configured", {
  apiVersion: "2026-03-25.dahlia",
});

type MappedStripeEvent = {
  eventType: CanonicalEventType;
  amountCents?: number;
  currency?: string;
  userId?: string;
  userEmail?: string;
  planName?: string;
  billingModel?: string;
  trialDays?: number;
  rawPayload: Record<string, unknown>;
};

function asRecord(value: unknown): Record<string, unknown> {
  return typeof value === "object" && value !== null
    ? (value as Record<string, unknown>)
    : {};
}

function getString(value: unknown) {
  return typeof value === "string" && value.length > 0 ? value : undefined;
}

function getNumber(value: unknown) {
  return typeof value === "number" ? value : undefined;
}

function mapStripeEvent(event: Stripe.Event): MappedStripeEvent | null {
  const object = asRecord(event.data.object);
  const metadata = asRecord(object.metadata);
  const subscriptionStatus = getString(object.status);
  const planName = getString(metadata.plan_name) ?? getString(object.plan);
  const customerId = getString(object.customer);
  const customerEmail =
    getString(object.customer_email) ?? getString(metadata.customer_email);
  const currency = getString(object.currency)?.toUpperCase();
  const amountPaid = getNumber(object.amount_paid) ?? getNumber(object.amount_due);

  switch (event.type) {
    case "customer.subscription.created":
      return {
        eventType: subscriptionStatus === "trialing" ? "trial_started" : "subscription_started",
        userId: customerId,
        userEmail: customerEmail,
        planName,
        billingModel: subscriptionStatus === "trialing" ? "free_trial" : "paid_subscription",
        trialDays: getNumber(metadata.trial_days),
        rawPayload: {
          stripe_type: event.type,
          stripe_id: event.id,
          status: subscriptionStatus,
        },
      };
    case "customer.subscription.updated":
      if (subscriptionStatus === "active") {
        return {
          eventType: "subscription_started",
          userId: customerId,
          userEmail: customerEmail,
          planName,
          billingModel: "paid_subscription",
          rawPayload: {
            stripe_type: event.type,
            stripe_id: event.id,
            status: subscriptionStatus,
          },
        };
      }

      if (subscriptionStatus === "canceled") {
        return {
          eventType: "subscription_cancelled",
          userId: customerId,
          userEmail: customerEmail,
          planName,
          rawPayload: {
            stripe_type: event.type,
            stripe_id: event.id,
            status: subscriptionStatus,
          },
        };
      }

      return null;
    case "customer.subscription.deleted":
      return {
        eventType: "subscription_cancelled",
        userId: customerId,
        userEmail: customerEmail,
        planName,
        rawPayload: {
          stripe_type: event.type,
          stripe_id: event.id,
          status: subscriptionStatus,
        },
      };
    case "invoice.paid":
      return {
        eventType: "invoice_paid",
        userId: customerId,
        userEmail: customerEmail,
        planName,
        amountCents: amountPaid,
        currency,
        rawPayload: {
          stripe_type: event.type,
          stripe_id: event.id,
          subscription: getString(object.subscription),
        },
      };
    default:
      return null;
  }
}

export async function POST(request: NextRequest) {
  const webhookSecret = env.STRIPE_WEBHOOK_SECRET;
  if (!webhookSecret) {
    return NextResponse.json({ error: "STRIPE_WEBHOOK_SECRET is not configured" }, { status: 503 });
  }

  const signature = request.headers.get("stripe-signature");
  if (!signature) {
    return NextResponse.json({ error: "Missing stripe-signature header" }, { status: 400 });
  }

  const rawBody = await request.text();

  let stripeEvent: Stripe.Event;
  try {
    stripeEvent = stripe.webhooks.constructEvent(rawBody, signature, webhookSecret);
  } catch (error) {
    console.error("Stripe signature verification failed", error);
    return NextResponse.json({ error: "Invalid Stripe signature" }, { status: 400 });
  }

  const mapped = mapStripeEvent(stripeEvent);
  if (!mapped) {
    return NextResponse.json({ received: true, mapped: false, stripeType: stripeEvent.type });
  }

  const canonicalEvent = canonicalEventSchema.parse({
    event_type: mapped.eventType,
    event_id: `stripe_${stripeEvent.id}`,
    source: "stripe",
    occurred_at: new Date(stripeEvent.created * 1000),
    user_id: mapped.userId,
    user_email: mapped.userEmail,
    plan_name: mapped.planName,
    billing_model: mapped.billingModel,
    trial_days: mapped.trialDays,
    amount_cents: mapped.amountCents,
    currency: mapped.currency,
    raw_payload: mapped.rawPayload,
  });

  try {
    const result = await recordEvent(canonicalEvent);
    return NextResponse.json({
      received: true,
      mapped: true,
      stripeType: stripeEvent.type,
      result,
    });
  } catch (error) {
    console.error("Stripe webhook processing failed", error);
    return NextResponse.json({ error: "Failed to record Stripe event" }, { status: 500 });
  }
}
