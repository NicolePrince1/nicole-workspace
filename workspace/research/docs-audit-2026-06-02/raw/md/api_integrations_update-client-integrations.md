> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Client Integrations

> Replace the integration rows for a client in client_integrations



## OpenAPI

````yaml /api/openapi.json put /v1/integrations/:client_id
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
  /v1/integrations/:client_id:
    put:
      tags:
        - Integrations
      summary: Update Client Integrations
      description: Replace the integration rows for a client in client_integrations
      parameters:
        - schema:
            type: string
          required: true
          name: client_id
          in: path
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateClientIntegrationRequest'
      responses:
        '200':
          description: Integration config updated
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
    UpdateClientIntegrationRequest:
      type: object
      properties:
        integrations:
          type: array
          items:
            type: object
            additionalProperties: {}
          example:
            - integration: google
              accountId: '12345'
      required:
        - integrations
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