> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Archive

> List archived items (paginated)



## OpenAPI

````yaml /api/openapi.json get /v1/archive
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
  /v1/archive:
    get:
      tags:
        - Archive
      summary: List Archive
      description: List archived items (paginated)
      parameters:
        - schema:
            type:
              - integer
              - 'null'
            minimum: 0
            default: 0
          required: false
          name: page
          in: query
        - schema:
            type: integer
            minimum: 1
            maximum: 100
            default: 20
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
          required: false
          name: types
          in: query
        - schema:
            type: string
            enum:
              - name
              - deleted_at
            default: deleted_at
          required: false
          name: sort_by
          in: query
        - schema:
            type: string
            enum:
              - asc
              - desc
            default: desc
          required: false
          name: order
          in: query
      responses:
        '200':
          description: Paginated archived items
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    enum:
                      - true
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                        name:
                          type: string
                        deleted_at:
                          type:
                            - string
                            - 'null'
                        type:
                          type: string
                          enum:
                            - clients
                            - projects
                            - media
                            - automations
                      required:
                        - id
                        - name
                        - deleted_at
                        - type
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
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````