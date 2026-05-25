> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Test Connection

> Proxy an integration connection test to api.oviond.com



## OpenAPI

````yaml /api/openapi.json post /v1/data/test
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
  /v1/data/test:
    post:
      tags:
        - Data
      summary: Test Connection
      description: Proxy an integration connection test to api.oviond.com
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DataTestRequest'
      responses:
        '200':
          description: Test result from upstream API
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DataProxyResponse'
        '502':
          description: Upstream API error
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                required:
                  - error
components:
  schemas:
    DataTestRequest:
      type: object
      properties:
        integration_id:
          type: string
          example: ga4
        client_id:
          type: string
          example: cliAbc123
        credentials:
          type: object
          additionalProperties: {}
      required:
        - integration_id
        - client_id
    DataProxyResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data: {}
      required:
        - success
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````