> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Unlink Datasource

> Unlink a datasource from a client



## OpenAPI

````yaml /api/openapi.json post /v1/integrations/:client_id/unlink
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
  /v1/integrations/:client_id/unlink:
    post:
      tags:
        - Integrations
      summary: Unlink Datasource
      description: Unlink a datasource from a client
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
              type: object
              properties:
                integration_id:
                  type: string
              required:
                - integration_id
      responses:
        '200':
          description: Datasource unlinked
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
components:
  schemas:
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