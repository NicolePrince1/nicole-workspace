#!/usr/bin/env python3
from __future__ import annotations

import argparse
from collections import defaultdict
from typing import Any

from meta_common import (
    DEFAULTS,
    action_map,
    date_window,
    ensure_act_prefix,
    extract_action_value,
    float_or_none,
    get_page_token,
    graph_request,
    int_or_none,
    numeric_delta,
    paginate,
    previous_window,
    print_json,
)

NUMERIC_FIELDS = [
    "spend",
    "impressions",
    "clicks",
    "reach",
    "ctr",
    "cpc",
    "cpm",
    "frequency",
]

LEVEL_FIELDS = {
    "account": ["account_id", "account_name"],
    "campaign": ["campaign_id", "campaign_name"],
    "adset": ["campaign_id", "campaign_name", "adset_id", "adset_name"],
    "ad": [
        "campaign_id",
        "campaign_name",
        "adset_id",
        "adset_name",
        "ad_id",
        "ad_name",
    ],
}

DEFAULT_ACTION_SNAPSHOT = [
    "link_click",
    "landing_page_view",
    "omni_landing_page_view",
    "lead",
    "purchase",
    "page_engagement",
    "post_engagement",
    "video_view",
]


def coerce_primary_types(values: list[str] | None) -> list[str]:
    return [value.strip() for value in (values or []) if value and value.strip()]


def insight_rows(
    *,
    account_id: str,
    since: str,
    until: str,
    level: str,
    fields: list[str],
    limit: int | None = None,
    breakdowns: list[str] | None = None,
    all_pages: bool = True,
) -> list[dict[str, Any]]:
    params: dict[str, Any] = {
        "fields": ",".join(fields),
        "time_range": {"since": since, "until": until},
        "level": level,
    }
    if breakdowns:
        params["breakdowns"] = ",".join(breakdowns)
    if limit:
        params["limit"] = limit

    path = f"{ensure_act_prefix(account_id)}/insights"
    if all_pages:
        return paginate(path, params)
    return graph_request(path, params).get("data", [])


def flatten_insight_row(row: dict[str, Any], primary_action_types: list[str]) -> dict[str, Any]:
    action_values = action_map(row.get("actions"))
    cost_per_action = action_map(row.get("cost_per_action_type"))
    outbound_clicks = action_map(row.get("outbound_clicks"))

    flat: dict[str, Any] = {}
    for key in LEVEL_FIELDS["account"] + LEVEL_FIELDS["campaign"] + LEVEL_FIELDS["adset"] + LEVEL_FIELDS["ad"]:
        if key in row:
            flat[key] = row.get(key)

    for key in [
        "date_start",
        "date_stop",
        "publisher_platform",
        "platform_position",
        "impression_device",
        "country",
        "region",
        "age",
        "gender",
    ]:
        if key in row:
            flat[key] = row.get(key)

    for metric in NUMERIC_FIELDS:
        if metric in row:
            value = float_or_none(row.get(metric))
            if metric in {"impressions", "clicks", "reach"}:
                flat[metric] = int_or_none(value)
            else:
                flat[metric] = None if value is None else round(value, 4)

    for action_type in DEFAULT_ACTION_SNAPSHOT:
        value = action_values.get(action_type, 0.0)
        flat[action_type] = int(value) if float(value).is_integer() else round(value, 4)
        cpa = cost_per_action.get(action_type)
        flat[f"cost_per_{action_type}"] = None if cpa is None else round(cpa, 4)

    custom_actions = {
        key: (int(value) if float(value).is_integer() else round(value, 4))
        for key, value in action_values.items()
        if key.startswith("offsite_conversion.custom")
    }
    if custom_actions:
        flat["custom_conversion_actions"] = custom_actions

    if outbound_clicks:
        flat["outbound_clicks"] = {
            key: (int(value) if float(value).is_integer() else round(value, 4))
            for key, value in outbound_clicks.items()
        }

    if primary_action_types:
        primary_total = sum(action_values.get(name, 0.0) for name in primary_action_types)
        flat["primary_action_types"] = primary_action_types
        flat["primary_actions"] = int(primary_total) if float(primary_total).is_integer() else round(primary_total, 4)
        spend = float_or_none(row.get("spend")) or 0.0
        flat["cost_per_primary_action"] = None if primary_total == 0 else round(spend / primary_total, 4)

    flat["actions"] = {
        key: (int(value) if float(value).is_integer() else round(value, 4))
        for key, value in action_values.items()
    }
    flat["cost_per_action_type"] = {
        key: (int(value) if float(value).is_integer() else round(value, 4))
        for key, value in cost_per_action.items()
    }
    return flat


def sort_rows(rows: list[dict[str, Any]], sort_key: str | None) -> list[dict[str, Any]]:
    if not sort_key:
        return rows

    def metric(row: dict[str, Any]) -> tuple[int, float]:
        value = row.get(sort_key)
        if value is None:
            return (1, 0.0)
        try:
            return (0, float(value))
        except (TypeError, ValueError):
            return (0, 0.0)

    return sorted(rows, key=metric, reverse=True)


def summarize_flat_rows(rows: list[dict[str, Any]], primary_action_types: list[str]) -> dict[str, Any]:
    totals: dict[str, float] = defaultdict(float)
    distinct_actions: set[str] = set()

    for row in rows:
        for metric in ["spend", "impressions", "clicks", "reach", "link_click", "landing_page_view", "omni_landing_page_view", "lead", "purchase", "page_engagement", "post_engagement", "video_view"]:
            value = row.get(metric)
            if value is not None:
                totals[metric] += float(value)
        if row.get("actions"):
            distinct_actions.update(row["actions"].keys())

    summary: dict[str, Any] = {
        "row_count": len(rows),
        "spend": round(totals.get("spend", 0.0), 4),
        "impressions": int(totals.get("impressions", 0.0)),
        "clicks": int(totals.get("clicks", 0.0)),
        "reach": int(totals.get("reach", 0.0)) if totals.get("reach") else None,
        "link_clicks": int(totals.get("link_click", 0.0)),
        "landing_page_views": int(totals.get("landing_page_view", 0.0)),
        "omni_landing_page_views": int(totals.get("omni_landing_page_view", 0.0)),
        "leads": int(totals.get("lead", 0.0)),
        "purchases": int(totals.get("purchase", 0.0)),
        "page_engagements": int(totals.get("page_engagement", 0.0)),
        "post_engagements": int(totals.get("post_engagement", 0.0)),
        "video_views": int(totals.get("video_view", 0.0)),
        "action_types_seen": sorted(distinct_actions),
    }

    if summary["impressions"] > 0:
        summary["ctr"] = round((summary["clicks"] / summary["impressions"]) * 100.0, 4)
        summary["cpm"] = round((summary["spend"] / summary["impressions"]) * 1000.0, 4)
    else:
        summary["ctr"] = None
        summary["cpm"] = None

    if summary["clicks"] > 0:
        summary["cpc"] = round(summary["spend"] / summary["clicks"], 4)
    else:
        summary["cpc"] = None

    if primary_action_types:
        primary_actions = 0.0
        for row in rows:
            primary_actions += sum((row.get("actions") or {}).get(name, 0.0) for name in primary_action_types)
        summary["primary_action_types"] = primary_action_types
        summary["primary_actions"] = int(primary_actions) if float(primary_actions).is_integer() else round(primary_actions, 4)
        summary["cost_per_primary_action"] = None if primary_actions == 0 else round(summary["spend"] / primary_actions, 4)

    return summary


def command_overview(args: argparse.Namespace) -> dict[str, Any]:
    since, until = date_window(args.days)
    prev_since, prev_until = previous_window(since, until)
    primary = coerce_primary_types(args.primary_action_type)
    fields = [
        "account_id",
        "account_name",
        "spend",
        "impressions",
        "clicks",
        "reach",
        "ctr",
        "cpc",
        "cpm",
        "frequency",
        "actions",
        "cost_per_action_type",
    ]

    current_rows = insight_rows(
        account_id=args.account_id,
        since=since,
        until=until,
        level="account",
        fields=fields,
        all_pages=False,
        limit=1,
    )
    previous_rows = insight_rows(
        account_id=args.account_id,
        since=prev_since,
        until=prev_until,
        level="account",
        fields=fields,
        all_pages=False,
        limit=1,
    )

    current = flatten_insight_row(current_rows[0], primary) if current_rows else {}
    previous = flatten_insight_row(previous_rows[0], primary) if previous_rows else {}

    delta = {
        "spend": numeric_delta(float_or_none(current.get("spend")), float_or_none(previous.get("spend"))),
        "impressions": numeric_delta(float_or_none(current.get("impressions")), float_or_none(previous.get("impressions"))),
        "clicks": numeric_delta(float_or_none(current.get("clicks")), float_or_none(previous.get("clicks"))),
        "link_clicks": numeric_delta(float_or_none(current.get("link_click")), float_or_none(previous.get("link_click"))),
        "landing_page_views": numeric_delta(float_or_none(current.get("landing_page_view")), float_or_none(previous.get("landing_page_view"))),
        "leads": numeric_delta(float_or_none(current.get("lead")), float_or_none(previous.get("lead"))),
        "purchases": numeric_delta(float_or_none(current.get("purchase")), float_or_none(previous.get("purchase"))),
        "ctr": numeric_delta(float_or_none(current.get("ctr")), float_or_none(previous.get("ctr"))),
        "cpc": numeric_delta(float_or_none(current.get("cpc")), float_or_none(previous.get("cpc"))),
        "cpm": numeric_delta(float_or_none(current.get("cpm")), float_or_none(previous.get("cpm"))),
    }
    if primary:
        delta["primary_actions"] = numeric_delta(
            float_or_none(current.get("primary_actions")),
            float_or_none(previous.get("primary_actions")),
        )
        delta["cost_per_primary_action"] = numeric_delta(
            float_or_none(current.get("cost_per_primary_action")),
            float_or_none(previous.get("cost_per_primary_action")),
        )

    return {
        "report": "overview",
        "account_id": ensure_act_prefix(args.account_id),
        "window": {"since": since, "until": until, "days": args.days},
        "previous_window": {"since": prev_since, "until": prev_until, "days": args.days},
        "current": current,
        "previous": previous,
        "delta": delta,
    }


def default_fields_for_level(level: str) -> list[str]:
    return LEVEL_FIELDS[level] + [
        "spend",
        "impressions",
        "clicks",
        "reach",
        "ctr",
        "cpc",
        "cpm",
        "frequency",
        "actions",
        "cost_per_action_type",
        "outbound_clicks",
        "date_start",
        "date_stop",
    ]


def command_insights(args: argparse.Namespace) -> dict[str, Any]:
    since, until = date_window(args.days)
    primary = coerce_primary_types(args.primary_action_type)
    fields = default_fields_for_level(args.level)
    rows = insight_rows(
        account_id=args.account_id,
        since=since,
        until=until,
        level=args.level,
        fields=fields,
        limit=args.limit,
        all_pages=not args.first_page_only,
    )
    flat_rows = [flatten_insight_row(row, primary) for row in rows]
    flat_rows = sort_rows(flat_rows, args.sort)
    if args.limit and args.first_page_only is False:
        flat_rows = flat_rows[: args.limit]
    return {
        "report": "insights",
        "level": args.level,
        "account_id": ensure_act_prefix(args.account_id),
        "window": {"since": since, "until": until, "days": args.days},
        "summary": summarize_flat_rows(flat_rows, primary),
        "rows": flat_rows,
    }


def command_breakdown(args: argparse.Namespace) -> dict[str, Any]:
    since, until = date_window(args.days)
    primary = coerce_primary_types(args.primary_action_type)
    breakdowns = [part.strip() for part in args.breakdowns.split(",") if part.strip()]
    fields = LEVEL_FIELDS[args.level] + [
        "spend",
        "impressions",
        "clicks",
        "ctr",
        "cpc",
        "actions",
        "cost_per_action_type",
        "date_start",
        "date_stop",
    ]
    rows = insight_rows(
        account_id=args.account_id,
        since=since,
        until=until,
        level=args.level,
        fields=fields,
        limit=args.limit,
        breakdowns=breakdowns,
        all_pages=not args.first_page_only,
    )
    flat_rows = [flatten_insight_row(row, primary) for row in rows]
    flat_rows = sort_rows(flat_rows, args.sort)
    if args.limit and args.first_page_only is False:
        flat_rows = flat_rows[: args.limit]
    return {
        "report": "breakdown",
        "level": args.level,
        "breakdowns": breakdowns,
        "account_id": ensure_act_prefix(args.account_id),
        "window": {"since": since, "until": until, "days": args.days},
        "summary": summarize_flat_rows(flat_rows, primary),
        "rows": flat_rows,
    }


def command_action_types(args: argparse.Namespace) -> dict[str, Any]:
    since, until = date_window(args.days)
    rows = insight_rows(
        account_id=args.account_id,
        since=since,
        until=until,
        level=args.level,
        fields=LEVEL_FIELDS[args.level] + ["actions", "cost_per_action_type", "spend", "date_start", "date_stop"],
        limit=args.limit,
        all_pages=not args.first_page_only,
    )

    totals: dict[str, float] = defaultdict(float)
    cpas: dict[str, list[float]] = defaultdict(list)
    row_counts: dict[str, int] = defaultdict(int)

    for row in rows:
        action_values = action_map(row.get("actions"))
        cost_values = action_map(row.get("cost_per_action_type"))
        for action_type, value in action_values.items():
            totals[action_type] += value
            row_counts[action_type] += 1
        for action_type, value in cost_values.items():
            cpas[action_type].append(value)

    ranked = []
    for action_type, total in totals.items():
        values = cpas.get(action_type, [])
        avg_cpa = None if not values else round(sum(values) / len(values), 4)
        ranked.append(
            {
                "action_type": action_type,
                "total_value": int(total) if float(total).is_integer() else round(total, 4),
                "rows_present": row_counts[action_type],
                "average_cost_per_action": avg_cpa,
            }
        )

    ranked.sort(key=lambda row: row["total_value"], reverse=True)
    return {
        "report": "action-types",
        "level": args.level,
        "account_id": ensure_act_prefix(args.account_id),
        "window": {"since": since, "until": until, "days": args.days},
        "rows": ranked,
    }


def command_page_overview(args: argparse.Namespace) -> dict[str, Any]:
    page_token = get_page_token(args.page_id)
    profile = graph_request(
        args.page_id,
        {"fields": "id,name,fan_count,followers_count,link"},
        token=page_token,
    )
    posts = graph_request(
        f"{args.page_id}/feed",
        {
            "fields": "id,message,created_time,permalink_url,likes.summary(true),comments.summary(true),shares",
            "limit": args.limit,
        },
        token=page_token,
    ).get("data", [])
    return {
        "report": "page-overview",
        "page_id": args.page_id,
        "profile": profile,
        "recent_posts": posts,
    }


def command_instagram_overview(args: argparse.Namespace) -> dict[str, Any]:
    profile = graph_request(
        args.instagram_id,
        {"fields": "id,username,followers_count,media_count"},
    )
    media = graph_request(
        f"{args.instagram_id}/media",
        {
            "fields": "id,caption,timestamp,media_type,permalink,like_count,comments_count",
            "limit": args.limit,
        },
    ).get("data", [])
    return {
        "report": "instagram-overview",
        "instagram_account_id": args.instagram_id,
        "profile": profile,
        "recent_media": media,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run reusable Meta reporting workflows for Oviond.")
    parser.add_argument("--account-id", default=DEFAULTS["ad_account_id"])
    subparsers = parser.add_subparsers(dest="command", required=True)

    overview = subparsers.add_parser("overview", help="Current-period vs prior-period account summary.")
    overview.add_argument("--days", type=int, default=7)
    overview.add_argument("--primary-action-type", action="append")
    overview.set_defaults(func=command_overview)

    insights = subparsers.add_parser("insights", help="Flat insights table for account, campaign, ad set, or ad level.")
    insights.add_argument("level", choices=["account", "campaign", "adset", "ad"])
    insights.add_argument("--days", type=int, default=30)
    insights.add_argument("--limit", type=int)
    insights.add_argument("--sort", default="spend")
    insights.add_argument("--primary-action-type", action="append")
    insights.add_argument("--first-page-only", action="store_true")
    insights.set_defaults(func=command_insights)

    breakdown = subparsers.add_parser("breakdown", help="Break performance down by platform, age/gender, country, device, or placement.")
    breakdown.add_argument("level", choices=["account", "campaign", "adset", "ad"])
    breakdown.add_argument("breakdowns", help="Comma-separated Meta breakdowns, e.g. publisher_platform or age,gender")
    breakdown.add_argument("--days", type=int, default=30)
    breakdown.add_argument("--limit", type=int)
    breakdown.add_argument("--sort", default="spend")
    breakdown.add_argument("--primary-action-type", action="append")
    breakdown.add_argument("--first-page-only", action="store_true")
    breakdown.set_defaults(func=command_breakdown)

    action_types = subparsers.add_parser("action-types", help="List action types present in recent reporting, including custom conversions.")
    action_types.add_argument("level", choices=["account", "campaign", "adset", "ad"], default="campaign")
    action_types.add_argument("--days", type=int, default=30)
    action_types.add_argument("--limit", type=int)
    action_types.add_argument("--first-page-only", action="store_true")
    action_types.set_defaults(func=command_action_types)

    page = subparsers.add_parser("page-overview", help="Read the connected Facebook Page basics and recent posts.")
    page.add_argument("--page-id", default=DEFAULTS["page_id"])
    page.add_argument("--limit", type=int, default=5)
    page.set_defaults(func=command_page_overview)

    instagram = subparsers.add_parser("instagram-overview", help="Read the connected Instagram account basics and recent media.")
    instagram.add_argument("--instagram-id", default=DEFAULTS["instagram_account_id"])
    instagram.add_argument("--limit", type=int, default=5)
    instagram.set_defaults(func=command_instagram_overview)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    result = args.func(args)
    print_json(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
