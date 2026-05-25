> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Templates

> List templates for the current account.



## OpenAPI

````yaml /api/openapi.json get /v1/templates
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
    get:
      tags:
        - Templates
      summary: List Templates
      description: List templates for the current account.
      parameters:
        - schema:
            type:
              - integer
              - 'null'
            minimum: 0
            default: 0
            example: 0
          required: false
          name: page
          in: query
        - schema:
            type: integer
            minimum: 1
            maximum: 100
            default: 20
            example: 20
          required: false
          name: limit
          in: query
        - schema:
            type: string
          required: false
          name: search
          in: query
        - schema:
            type: string
            enum:
              - ranking
              - created_at
              - name
            default: ranking
            example: ranking
          required: false
          name: sort_by
          in: query
        - schema:
            anyOf:
              - type: string
                enum:
                  - asc
                  - desc
              - type:
                  - integer
                  - 'null'
                minimum: -1
                maximum: 1
              - type: 'null'
            default: desc
            example: desc
          required: false
          name: sort_order
          in: query
        - schema:
            anyOf:
              - type: string
              - type: array
                items:
                  type: string
            description: Filter by integration IDs
          required: false
          name: datasources
          in: query
        - schema:
            type: string
            enum:
              - standard
              - mine
            default: standard
            description: standard = Oviond templates, mine = user templates
          required: false
          name: source
          in: query
      responses:
        '200':
          description: Template list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListTemplatesResponse'
components:
  schemas:
    ListTemplatesResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: array
          items:
            $ref: '#/components/schemas/Template'
        meta:
          type: object
          properties:
            page:
              type: number
            limit:
              type: number
            total:
              type: number
          required:
            - page
            - limit
            - total
      required:
        - success
        - data
        - meta
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