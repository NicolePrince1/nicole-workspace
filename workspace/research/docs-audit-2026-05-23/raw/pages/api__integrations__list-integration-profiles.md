> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Integration Profiles

> List auth profiles for a specific integration



## OpenAPI

````yaml /api/openapi.json get /v1/integrations/:integrationID/profiles
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
  /v1/integrations/:integrationID/profiles:
    get:
      tags:
        - Integrations
      summary: List Integration Profiles
      description: List auth profiles for a specific integration
      parameters:
        - schema:
            type: string
          required: true
          name: integrationID
          in: path
      responses:
        '200':
          description: Profile list
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