> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Theme

> Create a new theme.



## OpenAPI

````yaml /api/openapi.json post /v1/themes
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
  /v1/themes:
    post:
      tags:
        - Themes
      summary: Create Theme
      description: Create a new theme.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateThemeRequest'
      responses:
        '201':
          description: Theme created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateThemeResponse'
components:
  schemas:
    CreateThemeRequest:
      type: object
      properties:
        name:
          type: string
          minLength: 1
          example: Dark Corporate
        primary_color:
          type: string
        chart_1:
          type: string
        chart_2:
          type: string
        chart_3:
          type: string
        chart_4:
          type: string
        chart_5:
          type: string
        chart_6:
          type: string
        chart_7:
          type: string
        chart_8:
          type: string
        chart_9:
          type: string
        chart_10:
          type: string
        font:
          type: string
        radius:
          type: string
        shadow:
          type: string
          enum:
            - none
            - sm
            - md
            - lg
      required:
        - name
        - primary_color
    CreateThemeResponse:
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