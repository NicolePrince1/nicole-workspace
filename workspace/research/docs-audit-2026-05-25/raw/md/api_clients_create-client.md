> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Client

> Create a new client



## OpenAPI

````yaml /api/openapi.json post /v1/clients
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
  /v1/clients:
    post:
      tags:
        - Clients
      summary: Create Client
      description: Create a new client
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateClientRequest'
      responses:
        '201':
          description: Client created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateClientResponse'
components:
  schemas:
    CreateClientRequest:
      type: object
      properties:
        name:
          type: string
          minLength: 1
          example: Acme Corp
        website:
          type: string
          example: https://acme.com
        currency_code:
          type: string
          example: USD
        currency_symbol:
          type: string
          example: $
        timezone:
          type: string
          example: America/New_York
        manager:
          type: string
        domain_id:
          type: string
        theme_id:
          type: string
        folders:
          type: array
          items:
            type: string
      required:
        - name
        - website
        - currency_code
        - currency_symbol
        - timezone
    CreateClientResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: object
          properties:
            id:
              type: string
            _id:
              type: string
          required:
            - id
            - _id
      required:
        - success
        - data
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````