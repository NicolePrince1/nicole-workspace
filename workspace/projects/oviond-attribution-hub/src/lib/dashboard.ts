import { ensureTables, sql } from "@/lib/db";
import { envReadiness } from "@/lib/env";

const DAY_MS = 1000 * 60 * 60 * 24;
const THIRTY_DAYS_MS = 30 * DAY_MS;
const NINETY_DAYS_MS = 90 * DAY_MS;

interface LifecycleRow {
  id: string;
  event_type: string;
  event_id: string;
  source: string;
  occurred_at: string;
  stripe_customer_id: string | null;
  stripe_subscription_id: string | null;
  user_email: string | null;
  plan_name: string | null;
  trial_days: number | null;
  amount_cents: number | null;
  currency: string | null;
  attributed: boolean;
}

interface CaptureRow {
  id: string;
  email: string | null;
  user_id: string | null;
  account_id: string | null;
  stripe_customer_id: string | null;
  stripe_subscription_id: string | null;
  utm_source: string | null;
  utm_medium: string | null;
  utm_campaign: string | null;
  utm_content: string | null;
  utm_term: string | null;
  landing_page: string | null;
  page_path: string | null;
  page_location: string | null;
  captured_at: string;
}

interface DeliveryRow {
  id: string;
  event_id: string;
  platform: string;
  destination_event_name: string | null;
  status: string;
  response_code: number | null;
  error: string | null;
  created_at: string;
}

interface CustomerOutcome {
  key: string;
  stripeCustomerId: string | null;
  stripeSubscriptionId: string | null;
  userEmail: string | null;
  planName: string | null;
  trialDays: number;
  trialStartedAt: Date | null;
  convertedAt: Date | null;
  firstPaidAt: Date | null;
  firstPaidAmountCents: number | null;
  trialExpiredAt: Date | null;
  cancelledAt: Date | null;
  latestAt: Date;
  matchedCapture: CaptureRow | null;
  matchedAttribution: boolean;
}

export interface DashboardData {
  dbOk: boolean;
  env: ReturnType<typeof envReadiness>;
  hero: {
    trialsStarted30d: number;
    paidConversions30d: number;
    cohortConversionRate: number;
    matureTrialsCount: number;
    maturePaidCount: number;
    firstPaymentRevenue30d: number;
    trialsInFlight: number;
  };
  attribution: {
    captures30d: number;
    attributedTrials30d: number;
    attributedPaid30d: number;
    unattributedPaid30d: number;
    paidAttributionCoverage30d: number;
  };
  funnel: {
    totalTrackedTrials: number;
    inTrial: number;
    paid: number;
    lostPrePay: number;
    paidThenCancelled: number;
  };
  recentOutcomes: Array<{
    key: string;
    userEmail: string | null;
    planName: string | null;
    trialStartedAt: string | null;
    currentState: "trialing" | "paid" | "expired" | "cancelled";
    currentStateLabel: string;
    convertedAt: string | null;
    firstPaidAmountCents: number | null;
    daysToConvert: number | null;
    attributed: boolean;
    source: string | null;
    campaign: string | null;
    landingPage: string | null;
  }>;
  recentDeliveries: DeliveryRow[];
}

function outcomeKey(row: LifecycleRow) {
  return row.stripe_subscription_id ?? row.stripe_customer_id ?? row.event_id;
}

function isWithinWindow(date: Date | null, since: number) {
  return Boolean(date && date.getTime() >= since);
}

function matchCapture(
  captures: CaptureRow[],
  outcome: Pick<CustomerOutcome, "stripeCustomerId" | "stripeSubscriptionId" | "userEmail">,
) {
  for (const capture of captures) {
    if (outcome.stripeCustomerId && capture.stripe_customer_id === outcome.stripeCustomerId) {
      return capture;
    }
    if (
      outcome.stripeSubscriptionId &&
      capture.stripe_subscription_id === outcome.stripeSubscriptionId
    ) {
      return capture;
    }
    if (outcome.userEmail && capture.email === outcome.userEmail) {
      return capture;
    }
  }

  return null;
}

function getCurrentState(outcome: CustomerOutcome) {
  if (outcome.cancelledAt && outcome.convertedAt) {
    return { state: "cancelled" as const, label: "Cancelled after paid" };
  }

  if (outcome.convertedAt) {
    return { state: "paid" as const, label: "Paid" };
  }

  if (outcome.trialExpiredAt) {
    return { state: "expired" as const, label: "Expired" };
  }

  if (outcome.cancelledAt) {
    return { state: "cancelled" as const, label: "Cancelled" };
  }

  return { state: "trialing" as const, label: "In trial" };
}

function daysBetween(start: Date | null, end: Date | null) {
  if (!start || !end) {
    return null;
  }

  return Number(((end.getTime() - start.getTime()) / DAY_MS).toFixed(1));
}

export async function getDashboardData(): Promise<DashboardData> {
  const env = envReadiness();

  const empty: DashboardData = {
    dbOk: false,
    env,
    hero: {
      trialsStarted30d: 0,
      paidConversions30d: 0,
      cohortConversionRate: 0,
      matureTrialsCount: 0,
      maturePaidCount: 0,
      firstPaymentRevenue30d: 0,
      trialsInFlight: 0,
    },
    attribution: {
      captures30d: 0,
      attributedTrials30d: 0,
      attributedPaid30d: 0,
      unattributedPaid30d: 0,
      paidAttributionCoverage30d: 0,
    },
    funnel: {
      totalTrackedTrials: 0,
      inTrial: 0,
      paid: 0,
      lostPrePay: 0,
      paidThenCancelled: 0,
    },
    recentOutcomes: [],
    recentDeliveries: [],
  };

  if (!env.DATABASE_URL) {
    return empty;
  }

  try {
    await ensureTables();
    const db = sql();

    const [lifecycleRows, captureRows, recentDeliveries] = await Promise.all([
      db<LifecycleRow[]>`
        SELECT
          id::text,
          event_type,
          event_id,
          source,
          occurred_at::text,
          stripe_customer_id,
          stripe_subscription_id,
          user_email,
          plan_name,
          trial_days,
          amount_cents,
          currency,
          attributed
        FROM stripe_lifecycle_events
        WHERE occurred_at >= now() - interval '365 days'
        ORDER BY occurred_at ASC
      `,
      db<CaptureRow[]>`
        SELECT
          id,
          email,
          user_id,
          account_id,
          stripe_customer_id,
          stripe_subscription_id,
          utm_source,
          utm_medium,
          utm_campaign,
          utm_content,
          utm_term,
          landing_page,
          page_path,
          page_location,
          captured_at::text
        FROM attribution_captures
        WHERE captured_at >= now() - interval '365 days'
        ORDER BY captured_at DESC
      `,
      db<DeliveryRow[]>`
        SELECT
          id::text,
          event_id,
          platform,
          destination_event_name,
          status,
          response_code,
          error,
          created_at::text
        FROM delivery_attempts
        ORDER BY created_at DESC
        LIMIT 20
      `,
    ]);

    const outcomes = new Map<string, CustomerOutcome>();

    for (const row of lifecycleRows) {
      const key = outcomeKey(row);
      const occurredAt = new Date(row.occurred_at);
      const existing = outcomes.get(key);

      const outcome: CustomerOutcome = existing ?? {
        key,
        stripeCustomerId: row.stripe_customer_id,
        stripeSubscriptionId: row.stripe_subscription_id,
        userEmail: row.user_email,
        planName: row.plan_name,
        trialDays: row.trial_days ?? 15,
        trialStartedAt: null,
        convertedAt: null,
        firstPaidAt: null,
        firstPaidAmountCents: null,
        trialExpiredAt: null,
        cancelledAt: null,
        latestAt: occurredAt,
        matchedCapture: null,
        matchedAttribution: row.attributed,
      };

      outcome.stripeCustomerId ??= row.stripe_customer_id;
      outcome.stripeSubscriptionId ??= row.stripe_subscription_id;
      outcome.userEmail ??= row.user_email;
      outcome.planName ??= row.plan_name;
      outcome.trialDays = outcome.trialDays || row.trial_days || 15;
      outcome.latestAt = occurredAt > outcome.latestAt ? occurredAt : outcome.latestAt;
      outcome.matchedAttribution = outcome.matchedAttribution || row.attributed;

      switch (row.event_type) {
        case "trial_started":
          outcome.trialStartedAt =
            !outcome.trialStartedAt || occurredAt < outcome.trialStartedAt
              ? occurredAt
              : outcome.trialStartedAt;
          break;
        case "subscription_started":
          outcome.convertedAt =
            !outcome.convertedAt || occurredAt < outcome.convertedAt
              ? occurredAt
              : outcome.convertedAt;
          break;
        case "invoice_paid":
          if ((row.amount_cents ?? 0) > 0) {
            outcome.firstPaidAt =
              !outcome.firstPaidAt || occurredAt < outcome.firstPaidAt
                ? occurredAt
                : outcome.firstPaidAt;
            outcome.firstPaidAmountCents =
              outcome.firstPaidAt?.getTime() === occurredAt.getTime() ||
              outcome.firstPaidAmountCents == null
                ? row.amount_cents ?? null
                : outcome.firstPaidAmountCents;
            outcome.convertedAt =
              !outcome.convertedAt || occurredAt < outcome.convertedAt
                ? occurredAt
                : outcome.convertedAt;
          }
          break;
        case "trial_expired":
          outcome.trialExpiredAt =
            !outcome.trialExpiredAt || occurredAt < outcome.trialExpiredAt
              ? occurredAt
              : outcome.trialExpiredAt;
          break;
        case "subscription_cancelled":
          outcome.cancelledAt =
            !outcome.cancelledAt || occurredAt < outcome.cancelledAt
              ? occurredAt
              : outcome.cancelledAt;
          break;
        default:
          break;
      }

      outcomes.set(key, outcome);
    }

    const outcomesArray = Array.from(outcomes.values())
      .filter((outcome) => outcome.trialStartedAt)
      .map((outcome) => {
        const matchedCapture = matchCapture(captureRows, outcome);
        return {
          ...outcome,
          matchedCapture,
          matchedAttribution: outcome.matchedAttribution || Boolean(matchedCapture),
        };
      });

    const now = Date.now();
    const thirtyDaysAgo = now - THIRTY_DAYS_MS;
    const ninetyDaysAgo = now - NINETY_DAYS_MS;

    const trialsStarted30d = outcomesArray.filter((outcome) =>
      isWithinWindow(outcome.trialStartedAt, thirtyDaysAgo),
    );
    const paidConversions30d = outcomesArray.filter((outcome) =>
      isWithinWindow(outcome.convertedAt, thirtyDaysAgo),
    );
    const captures30d = captureRows.filter(
      (capture) => new Date(capture.captured_at).getTime() >= thirtyDaysAgo,
    ).length;

    const matureCohort = outcomesArray.filter((outcome) => {
      if (!outcome.trialStartedAt) {
        return false;
      }
      return now - outcome.trialStartedAt.getTime() >= outcome.trialDays * DAY_MS;
    });

    const maturePaidCount = matureCohort.filter((outcome) => outcome.convertedAt).length;
    const paidAttributionCoverage30d =
      paidConversions30d.length === 0
        ? 0
        : paidConversions30d.filter((outcome) => outcome.matchedAttribution).length /
          paidConversions30d.length;

    const inTrialCount = outcomesArray.filter(
      (outcome) =>
        !outcome.convertedAt && !outcome.trialExpiredAt && !outcome.cancelledAt,
    ).length;

    const paidCount = outcomesArray.filter((outcome) => outcome.convertedAt).length;
    const lostPrePayCount = outcomesArray.filter(
      (outcome) =>
        !outcome.convertedAt && (outcome.trialExpiredAt || outcome.cancelledAt),
    ).length;

    const paidThenCancelledCount = outcomesArray.filter(
      (outcome) => outcome.convertedAt && outcome.cancelledAt,
    ).length;

    const recentOutcomes = outcomesArray
      .filter((outcome) => outcome.latestAt.getTime() >= ninetyDaysAgo)
      .sort((a, b) => b.latestAt.getTime() - a.latestAt.getTime())
      .slice(0, 15)
      .map((outcome) => {
        const state = getCurrentState(outcome);
        return {
          key: outcome.key,
          userEmail: outcome.userEmail,
          planName: outcome.planName,
          trialStartedAt: outcome.trialStartedAt?.toISOString() ?? null,
          currentState: state.state,
          currentStateLabel: state.label,
          convertedAt: outcome.convertedAt?.toISOString() ?? null,
          firstPaidAmountCents: outcome.firstPaidAmountCents,
          daysToConvert: daysBetween(outcome.trialStartedAt, outcome.convertedAt),
          attributed: outcome.matchedAttribution,
          source: outcome.matchedCapture?.utm_source ?? null,
          campaign: outcome.matchedCapture?.utm_campaign ?? null,
          landingPage:
            outcome.matchedCapture?.landing_page ?? outcome.matchedCapture?.page_location ?? null,
        };
      });

    return {
      dbOk: true,
      env,
      hero: {
        trialsStarted30d: trialsStarted30d.length,
        paidConversions30d: paidConversions30d.length,
        cohortConversionRate:
          matureCohort.length === 0 ? 0 : maturePaidCount / matureCohort.length,
        matureTrialsCount: matureCohort.length,
        maturePaidCount,
        firstPaymentRevenue30d:
          paidConversions30d.reduce(
            (sum, outcome) => sum + (outcome.firstPaidAmountCents ?? 0),
            0,
          ) / 100,
        trialsInFlight: inTrialCount,
      },
      attribution: {
        captures30d,
        attributedTrials30d: trialsStarted30d.filter((outcome) => outcome.matchedAttribution).length,
        attributedPaid30d: paidConversions30d.filter((outcome) => outcome.matchedAttribution).length,
        unattributedPaid30d: paidConversions30d.filter((outcome) => !outcome.matchedAttribution).length,
        paidAttributionCoverage30d,
      },
      funnel: {
        totalTrackedTrials: outcomesArray.length,
        inTrial: inTrialCount,
        paid: paidCount,
        lostPrePay: lostPrePayCount,
        paidThenCancelled: paidThenCancelledCount,
      },
      recentOutcomes,
      recentDeliveries,
    };
  } catch (error) {
    console.error("Dashboard query failed", error);
    return empty;
  }
}
