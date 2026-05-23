> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Template

> Get a single template by ID.



## OpenAPI

````yaml /api/openapi.json get /v1/templates/:id
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
    get:
      tags:
        - Templates
      summary: Get Template
      description: Get a single template by ID.
      parameters:
        - schema:
            type: string
          required: true
          name: id
          in: path
      responses:
        '200':
          description: Template document
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TemplateResponse'
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
    TemplateResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          $ref: '#/components/schemas/Template'
      required:
        - success
        - data
    Template:
      type: object
      properties:
        id:
          type: string
        account_id:
          type: string
        name:
          type: string
        description:
          type: string
        type:
          type: string
        ranking:
          type: number
        datasources:
          type: array
          items:
            type: string
        thumbnail:
          type: string
        date_text:
          type: string
        date_compare:
          type: string
        date_include_today:
          type: boolean
        date_current_start:
          type: string
        date_current_end:
          type: string
        date_previous_start:
          type: string
        date_previous_end:
          type: string
        date_custom_days:
          type: number
        date_custom_months:
          type: number
        created_at: {}
      required:
        - id
        - account_id
        - name
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````