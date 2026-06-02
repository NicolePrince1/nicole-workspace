> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Account Usage

> Get account usage statistics vs plan limits



## OpenAPI

````yaml /api/openapi.json get /v1/account/usage
openapi: 3.1.0
info:
  title: Oviond Backend API
  version: 1.0.0
  description: Authentication, account management, billing, and media services for Oviond.
  x-logo:
    url: https://app.oviond.com/img/oviond-full-logo.svg
    altText: Oviond
servers:
  - url: https://api.oviond.com
    description: Production
security:
  - BearerAuth: []
paths:
  /v1/account/usage:
    get:
      tags:
        - Account
      summary: Get Account Usage
      description: Get account usage statistics vs plan limits
      responses:
        '200':
          description: Usage data
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AccountUsageResponse'
components:
  schemas:
    AccountUsageResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: object
          properties:
            CURRENT_PLAN:
              type: object
              properties:
                PLAN:
                  type: string
                PLAN_ID:
                  type: string
                PRICE:
                  type: number
                PROJECTS:
                  anyOf:
                    - type: number
                    - type: string
                  example: 15
                USERS:
                  anyOf:
                    - type: number
                    - type: string
                  example: UNLIMITED
                WHITE_LABEL:
                  type: boolean
                CUSTOM_DOMAIN:
                  type: boolean
                PDF:
                  type: boolean
                AUTOMATIONS:
                  type: boolean
                AGENCY_TOOLS:
                  type: boolean
                EMAIL_SUPPORT:
                  type: boolean
                LIVE_SUPPORT:
                  type: boolean
                ACCOUNT_MANAGER:
                  type: boolean
              required:
                - PROJECTS
                - USERS
            USAGE:
              type: object
              properties:
                PROJECTS:
                  type: number
                  example: 3
                USERS:
                  type: number
                  example: 2
              required:
                - PROJECTS
                - USERS
          required:
            - CURRENT_PLAN
            - USAGE
      required:
        - success
        - data
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````