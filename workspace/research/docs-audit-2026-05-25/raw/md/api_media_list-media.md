> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Media

> List media assets for the current account (paginated)



## OpenAPI

````yaml /api/openapi.json get /v1/media
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
  /v1/media:
    get:
      tags:
        - Media
      summary: List Media
      description: List media assets for the current account (paginated)
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
            example: logo
          required: false
          name: search
          in: query
        - schema:
            type: string
            example: folderAbc
          required: false
          name: folder_id
          in: query
      responses:
        '200':
          description: Media list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListMediaResponse'
components:
  schemas:
    ListMediaResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: array
          items:
            $ref: '#/components/schemas/MediaItem'
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
    MediaItem:
      type: object
      properties:
        id:
          type: string
        account_id:
          type: string
        name:
          type: string
        url:
          type: string
        key:
          type: string
        mime_type:
          type: string
        size:
          type: number
        is_deleted:
          type: boolean
        deleted_at:
          type:
            - string
            - 'null'
        created_at: {}
      required:
        - id
        - account_id
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````