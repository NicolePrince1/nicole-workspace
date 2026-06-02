> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Projects

> List projects for the current account (optionally filtered by client).



## OpenAPI

````yaml /api/openapi.json get /v1/projects
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
  /v1/projects:
    get:
      tags:
        - Projects
      summary: List Projects
      description: List projects for the current account (optionally filtered by client).
      parameters:
        - schema:
            type: string
            example: cliAbc123
          required: false
          name: client_id
          in: query
        - schema:
            type: string
            example: AGENCY
          required: false
          name: template
          in: query
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
            maximum: 200
            default: 50
            example: 50
          required: false
          name: limit
          in: query
      responses:
        '200':
          description: Paginated project list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListProjectsResponse'
components:
  schemas:
    ListProjectsResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: array
          items:
            $ref: '#/components/schemas/Project'
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
    Project:
      type: object
      properties:
        id:
          type: string
          example: proj123
        name:
          type: string
          example: Q1 Report
        account_id:
          type: string
          example: ov:26AbCdEfGhIjKlMnOp
        client_id:
          type: string
        type:
          type: string
          example: REPORT
        status:
          type: string
        nano_id:
          type: string
        created_at: {}
        is_deleted:
          type: boolean
        deleted_at:
          type:
            - string
            - 'null'
      required:
        - id
        - name
        - account_id
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````