> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Plans

> List available subscription plans from Stripe



## OpenAPI

````yaml /api/openapi.json get /v1/billing/plans
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
  /v1/billing/plans:
    get:
      tags:
        - Billing
      summary: List Plans
      description: List available subscription plans from Stripe
      responses:
        '200':
          description: Plan list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListPlansResponse'
components:
  schemas:
    ListPlansResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: array
          items:
            $ref: '#/components/schemas/Plan'
      required:
        - success
        - data
    Plan:
      type: object
      properties:
        price:
          type: object
          additionalProperties: {}
        product:
          type: object
          additionalProperties: {}
      required:
        - price
        - product
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````