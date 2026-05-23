> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk Delete Clients

> Delete multiple clients by ID



## OpenAPI

````yaml /api/openapi.json delete /v1/clients/bulk
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
  /v1/clients/bulk:
    delete:
      tags:
        - Clients
      summary: Bulk Delete Clients
      description: Delete multiple clients by ID
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/BulkDeleteClientsRequest'
      responses:
        '200':
          description: Clients deleted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
components:
  schemas:
    BulkDeleteClientsRequest:
      type: object
      properties:
        ids:
          type: array
          items:
            type: string
          minItems: 1
          example:
            - cliAbc123
            - cliDef456
      required:
        - ids
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