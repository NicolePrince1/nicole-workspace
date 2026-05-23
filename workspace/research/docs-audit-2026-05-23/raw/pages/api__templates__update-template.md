> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Template

> Update a template.



## OpenAPI

````yaml /api/openapi.json put /v1/templates/:id
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
  /v1/templates/:id:
    put:
      tags:
        - Templates
      summary: Update Template
      description: Update a template.
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
              $ref: '#/components/schemas/UpdateTemplateRequest'
      responses:
        '200':
          description: Template updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
        '404':
          description: Template not found
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
    UpdateTemplateRequest:
      type: object
      properties:
        name:
          type: string
        thumbnail:
          type: string
        type:
          type: string
        description:
          type: string
        ranking:
          type: number
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