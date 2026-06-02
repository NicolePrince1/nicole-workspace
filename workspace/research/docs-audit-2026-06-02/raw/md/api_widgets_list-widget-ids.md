> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Widget IDs

> Get widget IDs for a source.



## OpenAPI

````yaml /api/openapi.json get /v1/widgets/ids
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
  /v1/widgets/ids:
    get:
      tags:
        - Widgets
      summary: List Widget IDs
      description: Get widget IDs for a source.
      parameters:
        - schema:
            type: string
            example: proj123
          required: true
          name: source_id
          in: query
        - schema:
            type: string
            example: page123
          required: false
          name: page_id
          in: query
      responses:
        '200':
          description: Array of widget IDs
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListWidgetIDsResponse'
components:
  schemas:
    ListWidgetIDsResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: array
          items:
            type: string
      required:
        - success
        - data
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````