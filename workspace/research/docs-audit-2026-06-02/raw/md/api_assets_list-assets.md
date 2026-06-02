> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Assets

> List assets for the current account



## OpenAPI

````yaml /api/openapi.json get /v1/assets
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
  /v1/assets:
    get:
      tags:
        - Assets
      summary: List Assets
      description: List assets for the current account
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
            example: chart
          required: false
          name: type
          in: query
        - schema:
            type: string
          required: false
          name: tag
          in: query
        - schema:
            type: string
            description: Comma-separated category names to filter by
          required: false
          name: datasources
          in: query
        - schema:
            type: string
            enum:
              - all
              - mine
              - standard
            default: all
          required: false
          name: source
          in: query
        - schema:
            type: string
            default: created_at
          required: false
          name: sort_by
          in: query
        - schema:
            type:
              - number
              - 'null'
            default: -1
          required: false
          name: sort_order
          in: query
      responses:
        '200':
          description: Asset list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListAssetsResponse'
components:
  schemas:
    ListAssetsResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: array
          items:
            $ref: '#/components/schemas/Asset'
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
    Asset:
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
        tags:
          type: array
          items:
            type: string
        datasources:
          type: array
          items:
            type: string
        ranking:
          type:
            - number
            - 'null'
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