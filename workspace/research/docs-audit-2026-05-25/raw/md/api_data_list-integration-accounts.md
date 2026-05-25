> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Integration Accounts

> Proxy an integration accounts listing to api.oviond.com



## OpenAPI

````yaml /api/openapi.json post /v1/data/accounts
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
  /v1/data/accounts:
    post:
      tags:
        - Data
      summary: List Integration Accounts
      description: Proxy an integration accounts listing to api.oviond.com
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DataAccountsRequest'
      responses:
        '200':
          description: Accounts from upstream API
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
    DataAccountsRequest:
      type: object
      properties:
        integration_id:
          type: string
          example: ga4
        client_id:
          type: string
          example: cliAbc123
        account_name:
          type: string
        params:
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