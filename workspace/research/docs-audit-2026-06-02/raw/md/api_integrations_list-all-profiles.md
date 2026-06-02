> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List All Profiles

> List all auth profiles for every integration



## OpenAPI

````yaml /api/openapi.json get /v1/integrations/profiles
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
  /v1/integrations/profiles:
    get:
      tags:
        - Integrations
      summary: List All Profiles
      description: List all auth profiles for every integration
      responses:
        '200':
          description: Profiles grouped by integration ID
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
                    additionalProperties:
                      type: array
                      items:
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