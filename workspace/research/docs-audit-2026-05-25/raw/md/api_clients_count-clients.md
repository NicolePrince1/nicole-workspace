> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Count Clients

> Count total clients for the current account



## OpenAPI

````yaml /api/openapi.json get /v1/clients/count
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
  /v1/clients/count:
    get:
      tags:
        - Clients
      summary: Count Clients
      description: Count total clients for the current account
      responses:
        '200':
          description: Client count
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ClientCountResponse'
components:
  schemas:
    ClientCountResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: object
          properties:
            count:
              type: number
          required:
            - count
      required:
        - success
        - data
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````