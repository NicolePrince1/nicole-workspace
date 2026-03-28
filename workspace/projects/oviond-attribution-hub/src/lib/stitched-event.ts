import type { StripeLifecycleEvent } from "@/lib/stripe-events";
import type { StitchedAttribution } from "@/lib/attribution";

/**
 * A stitched event combines Stripe lifecycle truth with the best
 * matching attribution capture. This is what downstream adapters receive.
 */
export interface StitchedEvent extends StripeLifecycleEvent {
  attribution: StitchedAttribution | null;
}
