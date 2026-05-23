> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Branding

> Get branding settings



## OpenAPI

````yaml /api/openapi.json get /v1/branding
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
  /v1/branding:
    get:
      tags:
        - Branding
      summary: Get Branding
      description: Get branding settings
      responses:
        '200':
          description: Branding data
          content:
            application/json:
              schema:
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
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````