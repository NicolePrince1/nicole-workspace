> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk Delete Automations

> Soft-delete multiple automations and remove them from the cron scheduler



## OpenAPI

````yaml /api/openapi.json delete /v1/automations/bulk
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
  /v1/automations/bulk:
    delete:
      tags:
        - Automations
      summary: Bulk Delete Automations
      description: Soft-delete multiple automations and remove them from the cron scheduler
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                ids:
                  type: array
                  items:
                    type: string
                  minItems: 1
              required:
                - ids
      responses:
        '200':
          description: Automations deleted
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    enum:
                      - true
                required:
                  - success
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````