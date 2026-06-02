> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Integrations

> List all OAuth integrations stored for the current account



## OpenAPI

````yaml /api/openapi.json get /v1/integrations/auths
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
  /v1/integrations/auths:
    get:
      tags:
        - Integrations
      summary: List Integrations
      description: List all OAuth integrations stored for the current account
      responses:
        '200':
          description: Auth list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListAuthsResponse'
components:
  schemas:
    ListAuthsResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: array
          items:
            $ref: '#/components/schemas/Auth'
      required:
        - success
        - data
    Auth:
      type: object
      properties:
        id:
          type: string
        account_id:
          type: string
        integration:
          type: string
        name:
          type:
            - string
            - 'null'
        created_at:
          type:
            - string
            - 'null'
      required:
        - id
        - account_id
        - integration
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````