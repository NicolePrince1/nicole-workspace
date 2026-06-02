> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Page

> Create a page on a project or template.



## OpenAPI

````yaml /api/openapi.json post /v1/pages
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
    post:
      tags:
        - Pages
      summary: Create Page
      description: Create a page on a project or template.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreatePageRequest'
      responses:
        '201':
          description: Page created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreatePageResponse'
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
    CreatePageRequest:
      type: object
      properties:
        source_id:
          type: string
        source_type:
          type: string
          enum:
            - project
            - template
        name:
          type: string
          minLength: 1
        position:
          type: integer
        visible:
          type: boolean
      required:
        - source_id
        - source_type
        - name
    CreatePageResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: object
          properties:
            page_id:
              type: string
          required:
            - page_id
      required:
        - success
        - data
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````