#!/usr/bin/env python3
from __future__ import annotations

import argparse

from meta_common import (
    DEFAULTS,
    MetaAPIError,
    clean_action_map,
    ensure_act_prefix,
    get_page_token,
    graph_request,
    load_system_token,
    print_json,
)


def run_check(name, fn):
    try:
        payload = fn()
        return {"ok": True, "data": payload}
    except MetaAPIError as exc:
        return {"ok": False, "error": exc.to_dict()}


def main() -> int:
    parser = argparse.ArgumentParser(description="Diagnose Oviond Meta access and core read paths.")
    parser.add_argument("--account-id", default=DEFAULTS["ad_account_id"])
    parser.add_argument("--page-id", default=DEFAULTS["page_id"])
    parser.add_argument("--instagram-id", default=DEFAULTS["instagram_account_id"])
    args = parser.parse_args()

    system_token = load_system_token()
    account_path = ensure_act_prefix(args.account_id)

    summary = {
        "account": {
            "business_manager_id": DEFAULTS["business_manager_id"],
            "ad_account_id": account_path,
            "page_id": args.page_id,
            "instagram_account_id": args.instagram_id,
            "currency_expected": DEFAULTS["currency"],
        },
        "checks": {},
    }

    summary["checks"]["system_token"] = {"ok": True, "data": {"present": bool(system_token)}}

    summary["checks"]["ad_account"] = run_check(
        "ad_account",
        lambda: graph_request(
            account_path,
            {"fields": "id,name,account_status,currency,business_name"},
            token=system_token,
        ),
    )

    summary["checks"]["campaigns"] = run_check(
        "campaigns",
        lambda: {
            "count": len(
                rows := graph_request(
                    f"{account_path}/campaigns",
                    {"fields": "id,name,status,objective", "limit": 3},
                    token=system_token,
                ).get("data", [])
            ),
            "sample": rows[:2],
        },
    )

    summary["checks"]["ads_insights_last_7d"] = run_check(
        "ads_insights_last_7d",
        lambda: {
            "count": len(
                rows := graph_request(
                    f"{account_path}/insights",
                    {
                        "fields": "spend,impressions,clicks,ctr,cpc,actions,cost_per_action_type,date_start,date_stop",
                        "date_preset": "last_7d",
                        "level": "account",
                        "limit": 1,
                    },
                    token=system_token,
                ).get("data", [])
            ),
            "sample": [
                {
                    **rows[0],
                    "actions": clean_action_map(rows[0].get("actions")),
                    "cost_per_action_type": clean_action_map(rows[0].get("cost_per_action_type")),
                }
            ]
            if rows
            else [],
        },
    )

    page_token_box: dict[str, str] = {}
    summary["checks"]["page_token"] = run_check(
        "page_token",
        lambda: page_token_box.setdefault("token", get_page_token(args.page_id, system_token=system_token))
        and {"present": True},
    )

    def page_token() -> str:
        if "token" not in page_token_box:
            page_token_box["token"] = get_page_token(args.page_id, system_token=system_token)
        return page_token_box["token"]

    summary["checks"]["page_profile"] = run_check(
        "page_profile",
        lambda: graph_request(
            args.page_id,
            {"fields": "id,name,fan_count,followers_count"},
            token=page_token(),
        ),
    )

    summary["checks"]["page_feed"] = run_check(
        "page_feed",
        lambda: {
            "count": len(
                rows := graph_request(
                    f"{args.page_id}/feed",
                    {"fields": "id,message,created_time", "limit": 3},
                    token=page_token(),
                ).get("data", [])
            ),
            "sample": rows[:2],
        },
    )

    summary["checks"]["instagram_profile"] = run_check(
        "instagram_profile",
        lambda: graph_request(
            args.instagram_id,
            {"fields": "id,username,followers_count,media_count"},
            token=system_token,
        ),
    )

    summary["checks"]["instagram_media"] = run_check(
        "instagram_media",
        lambda: {
            "count": len(
                rows := graph_request(
                    f"{args.instagram_id}/media",
                    {
                        "fields": "id,caption,timestamp,media_type,permalink",
                        "limit": 3,
                    },
                    token=system_token,
                ).get("data", [])
            ),
            "sample": rows[:2],
        },
    )

    summary["checks"]["ad_pixels"] = run_check(
        "ad_pixels",
        lambda: {
            "count": len(
                rows := graph_request(
                    f"{account_path}/adspixels",
                    {"fields": "id,name", "limit": 5},
                    token=system_token,
                ).get("data", [])
            ),
            "sample": rows[:5],
        },
    )

    required = [
        "system_token",
        "ad_account",
        "campaigns",
        "ads_insights_last_7d",
        "page_token",
        "page_profile",
        "page_feed",
        "instagram_profile",
        "instagram_media",
    ]
    summary["overall_ok"] = all(summary["checks"][name]["ok"] for name in required)
    print_json(summary)
    return 0 if summary["overall_ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
