> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Theme

> Update a theme.



## OpenAPI

````yaml /api/openapi.json put /v1/themes/:id
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
  /v1/themes/:id:
    put:
      tags:
        - Themes
      summary: Update Theme
      description: Update a theme.
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
              $ref: '#/components/schemas/UpdateThemeRequest'
      responses:
        '200':
          description: Theme updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
        '404':
          description: Theme not found
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
    UpdateThemeRequest:
      type: object
      properties:
        name:
          type: string
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