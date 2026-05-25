> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Themes

> List themes for the current account.



## OpenAPI

````yaml /api/openapi.json get /v1/themes
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
    get:
      tags:
        - Themes
      summary: List Themes
      description: List themes for the current account.
      responses:
        '200':
          description: Theme list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListThemesResponse'
components:
  schemas:
    ListThemesResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: array
          items:
            $ref: '#/components/schemas/Theme'
      required:
        - success
        - data
    Theme:
      type: object
      properties:
        id:
          type: string
        account_id:
          type: string
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