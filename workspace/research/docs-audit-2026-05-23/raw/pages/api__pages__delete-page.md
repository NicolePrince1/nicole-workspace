> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Page

> Delete a page.



## OpenAPI

````yaml /api/openapi.json delete /v1/pages/{page_id}
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
  /v1/pages/{page_id}:
    delete:
      tags:
        - Pages
      summary: Delete Page
      description: Delete a page.
      parameters:
        - schema:
            type: string
          required: true
          name: page_id
          in: path
      responses:
        '200':
          description: Page deleted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
        '404':
          description: Page not found
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