export type DeliveryPlatform = "meta" | "ga4" | "google_ads";

export type DeliveryStatus = "sent" | "skipped" | "disabled" | "error";

export interface DeliveryResult {
  platform: DeliveryPlatform;
  status: DeliveryStatus;
  destinationEventName?: string;
  requestPayload?: Record<string, unknown>;
  responseCode?: number;
  responseBody?: string;
  error?: string;
}
