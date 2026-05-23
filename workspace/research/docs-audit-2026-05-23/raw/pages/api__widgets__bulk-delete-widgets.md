> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk Delete Widgets

> Delete multiple widgets by ID.



## OpenAPI

````yaml /api/openapi.json delete /v1/widgets/bulk
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
  /v1/widgets/bulk:
    delete:
      tags:
        - Widgets
      summary: Bulk Delete Widgets
      description: Delete multiple widgets by ID.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/BulkDeleteWidgetsRequest'
      responses:
        '200':
          description: Widgets deleted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
components:
  schemas:
    BulkDeleteWidgetsRequest:
      type: object
      properties:
        ids:
          type: array
          items:
            type: string
          minItems: 1
          example:
            - widget1
            - widget2
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