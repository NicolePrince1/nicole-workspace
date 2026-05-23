> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Invoices

> List Stripe invoices for a customer



## OpenAPI

````yaml /api/openapi.json get /v1/billing/invoices
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
  /v1/billing/invoices:
    get:
      tags:
        - Billing
      summary: List Invoices
      description: List Stripe invoices for a customer
      responses:
        '200':
          description: Invoice list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/InvoicesResponse'
components:
  schemas:
    InvoicesResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: object
          additionalProperties: {}
      required:
        - success
        - data
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````