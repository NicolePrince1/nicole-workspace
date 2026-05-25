> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Client

> Update a client



## OpenAPI

````yaml /api/openapi.json put /v1/clients/:id
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
  /v1/clients/:id:
    put:
      tags:
        - Clients
      summary: Update Client
      description: Update a client
      parameters:
        - schema:
            type: string
          required: true
          name: id
          in: path
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateClientRequest'
      responses:
        '200':
          description: Client updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
        '404':
          description: Client not found
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
    UpdateClientRequest:
      type: object
      properties:
        name:
          type: string
          example: Acme Corp Updated
        website:
          type: string
        currency_code:
          type: string
        currency_symbol:
          type: string
        timezone:
          type: string
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
    SuccessResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
      required:
        - success
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````