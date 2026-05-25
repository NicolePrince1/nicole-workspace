> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List All Clients

> List all clients with optional field selection



## OpenAPI

````yaml /api/openapi.json get /v1/clients/all
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
  /v1/clients/all:
    get:
      tags:
        - Clients
      summary: List All Clients
      description: List all clients with optional field selection
      parameters:
        - schema:
            type: string
            example: id,name,client_integrations
          required: false
          name: fields
          in: query
      responses:
        '200':
          description: All clients
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