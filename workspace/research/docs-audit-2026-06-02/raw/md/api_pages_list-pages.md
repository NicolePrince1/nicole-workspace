> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Pages

> List pages for a project or template.



## OpenAPI

````yaml /api/openapi.json get /v1/pages
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
  /v1/pages:
    get:
      tags:
        - Pages
      summary: List Pages
      description: List pages for a project or template.
      parameters:
        - schema:
            type: string
            example: proj123
          required: true
          name: source_id
          in: query
        - schema:
            type: string
            enum:
              - project
              - template
            example: project
          required: false
          name: source_type
          in: query
      responses:
        '200':
          description: Pages list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListPagesResponse'
        '404':
          description: Source not found
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
    ListPagesResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: array
          items:
            $ref: '#/components/schemas/Page'
      required:
        - success
        - data
    Page:
      type: object
      properties:
        page_id:
          type: string
          example: pg_abc123
        source_id:
          type: string
        source_type:
          type: string
          enum:
            - project
            - template
        name:
          type: string
          example: Overview
        position:
          type: integer
        visible:
          type: boolean
      required:
        - page_id
        - source_id
        - source_type
        - name
        - position
        - visible
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````