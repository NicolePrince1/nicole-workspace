import { z } from "zod";

const envSchema = z.object({
  NODE_ENV: z.enum(["development", "test", "production"]).default("development"),
  DATABASE_URL: z.string().optional(),
  INGEST_API_KEY: z.string().optional(),
  ADMIN_TOKEN: z.string().optional(),
  STRIPE_SECRET_KEY: z.string().optional(),
  STRIPE_WEBHOOK_SECRET: z.string().optional(),
  META_PIXEL_ID: z.string().optional(),
  META_ACCESS_TOKEN: z.string().optional(),
  GA4_MEASUREMENT_ID: z.string().optional(),
  GA4_API_SECRET: z.string().optional(),
  GOOGLE_ADS_CUSTOMER_ID: z.string().optional(),
  GOOGLE_ADS_DEVELOPER_TOKEN: z.string().optional(),
  GOOGLE_ADS_REFRESH_TOKEN: z.string().optional(),
  GOOGLE_ADS_CONVERSION_ACTION_ID: z.string().optional(),
  GOOGLE_ADS_LOGIN_CUSTOMER_ID: z.string().optional(),
});

let cachedEnv: z.infer<typeof envSchema> | null = null;

export function getServerEnv() {
  if (cachedEnv) {
    return cachedEnv;
  }

  const parsed = envSchema.safeParse(process.env);
  if (!parsed.success) {
    throw new Error(`Invalid environment configuration: ${parsed.error.message}`);
  }

  cachedEnv = parsed.data;
  return cachedEnv;
}

export function envReadiness() {
  const env = getServerEnv();

  return {
    DATABASE_URL: Boolean(env.DATABASE_URL),
    INGEST_API_KEY: Boolean(env.INGEST_API_KEY),
    ADMIN_TOKEN: Boolean(env.ADMIN_TOKEN),
    STRIPE_SECRET_KEY: Boolean(env.STRIPE_SECRET_KEY),
    STRIPE_WEBHOOK_SECRET: Boolean(env.STRIPE_WEBHOOK_SECRET),
    META_PIXEL_ID: Boolean(env.META_PIXEL_ID),
    META_ACCESS_TOKEN: Boolean(env.META_ACCESS_TOKEN),
    GA4_MEASUREMENT_ID: Boolean(env.GA4_MEASUREMENT_ID),
    GA4_API_SECRET: Boolean(env.GA4_API_SECRET),
    GOOGLE_ADS_CUSTOMER_ID: Boolean(env.GOOGLE_ADS_CUSTOMER_ID),
    GOOGLE_ADS_DEVELOPER_TOKEN: Boolean(env.GOOGLE_ADS_DEVELOPER_TOKEN),
    GOOGLE_ADS_REFRESH_TOKEN: Boolean(env.GOOGLE_ADS_REFRESH_TOKEN),
    GOOGLE_ADS_CONVERSION_ACTION_ID: Boolean(env.GOOGLE_ADS_CONVERSION_ACTION_ID),
  };
}

export function isProduction() {
  return getServerEnv().NODE_ENV === "production";
}
