> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Template

> Create a new template, optionally copying pages and widgets from a project.



## OpenAPI

````yaml /api/openapi.json post /v1/templates
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
  /v1/templates:
    post:
      tags:
        - Templates
      summary: Create Template
      description: >-
        Create a new template, optionally copying pages and widgets from a
        project.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateTemplateRequest'
      responses:
        '201':
          description: Template created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateTemplateResponse'
        '404':
          description: Source project not found
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
    CreateTemplateRequest:
      type: object
      properties:
        name:
          type: string
          minLength: 1
          example: Monthly SEO Report
        project_id:
          type: string
          description: Copy pages/widgets from this project
        type:
          type: string
          description: Defaults to the source project's type when omitted
        description:
          type: string
        thumbnail:
          type: string
        ranking:
          type: number
      required:
        - name
        - project_id
    CreateTemplateResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: object
          properties:
            id:
              type: string
          required:
            - id
      required:
        - success
        - data
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````