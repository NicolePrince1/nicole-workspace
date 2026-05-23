> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Activity

> List activity logs for the current account



## OpenAPI

````yaml /api/openapi.json get /v1/activity
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
  /v1/activity:
    get:
      tags:
        - Activity
      summary: List Activity
      description: List activity logs for the current account
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
            example: client
          required: false
          name: resource_type
          in: query
        - schema:
            type: string
            example: acme
          required: false
          name: search
          in: query
      responses:
        '200':
          description: Paginated activity log
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
                      additionalProperties: {}
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