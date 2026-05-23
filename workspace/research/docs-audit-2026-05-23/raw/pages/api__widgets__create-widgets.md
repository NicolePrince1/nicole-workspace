> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Widgets

> Batch create widgets via upsert.



## OpenAPI

````yaml /api/openapi.json post /v1/widgets
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
  /v1/widgets:
    post:
      tags:
        - Widgets
      summary: Create Widgets
      description: Batch create widgets via upsert.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateWidgetsRequest'
      responses:
        '201':
          description: Widgets created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateWidgetsResponse'
components:
  schemas:
    CreateWidgetsRequest:
      type: object
      properties:
        widgets:
          type: array
          items:
            type: object
            additionalProperties: {}
          minItems: 1
        source_type:
          type: string
          example: project
        source_id:
          type: string
          example: proj123
        client_id:
          type: string
        page_id:
          type: string
        account_id:
          type: string
      required:
        - widgets
        - source_type
        - source_id
        - client_id
        - page_id
        - account_id
    CreateWidgetsResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: object
          properties:
            inserted_count:
              type: number
            upserted_count:
              type: number
          required:
            - inserted_count
            - upserted_count
      required:
        - success
        - data
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````