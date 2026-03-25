# Error guide for Oviond Google Ads

Use this reference when a script fails and the raw Google Ads error needs translating into operator action.

## `PROJECT_DISABLED`

Meaning:
- the Cloud project behind the access token is not currently allowed to call Google Ads API

Check:
- correct project is being used by the service-account JSON
- `googleads.googleapis.com` is enabled on that project
- the project is active and intended for the developer token / Google Ads API setup

## `USER_PERMISSION_DENIED`

Meaning:
- the authenticated principal does not have the right kind of access to the requested customer

Check:
- service account email is added in Google Ads access/security
- manager account in `login-customer-id` is correct
- manager is linked to the target client account
- request path customer ID is the intended client/customer

## `DEVELOPER_TOKEN_NOT_APPROVED`

Meaning:
- the developer token is real but not approved for the requested access pattern

Check:
- developer token status in Ads API Center
- whether you are hitting production accounts vs test accounts

## `DEVELOPER_TOKEN_INVALID`

Meaning:
- wrong token or malformed token value

Check:
- exact env var value in `GOOGLE_ADS_DEVELOPER_TOKEN`

## `UNAUTHENTICATED`

Meaning:
- the bearer token is bad, expired, or was not accepted

Check:
- service-account JSON is current
- token minting step succeeded
- token is being sent in the `Authorization: Bearer ...` header
