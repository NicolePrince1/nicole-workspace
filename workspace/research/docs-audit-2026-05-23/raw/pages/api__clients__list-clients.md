> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Clients

> List clients for the current account



## OpenAPI

````yaml /api/openapi.json get /v1/clients
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
  /v1/clients:
    get:
      tags:
        - Clients
      summary: List Clients
      description: List clients for the current account
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
            example: acme
          required: false
          name: search
          in: query
        - schema:
            type: string
            example: folderXyz
          required: false
          name: folder_id
          in: query
        - schema:
            type: string
            default: updated_at
            example: updated_at
          required: false
          name: sort_by
          in: query
        - schema:
            type: string
            enum:
              - asc
              - desc
            default: desc
            example: desc
          required: false
          name: order
          in: query
      responses:
        '200':
          description: Paginated client list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListClientsResponse'
components:
  schemas:
    ListClientsResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: array
          items:
            $ref: '#/components/schemas/Client'
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
    Client:
      type: object
      properties:
        id:
          type: string
          example: cliAbc123
        account_id:
          type: string
          example: ov:26AbCdEfGhIjKlMnOp
        name:
          type: string
          example: Acme Website
        website:
          type: string
        timezone:
          type: string
        screenshot:
          type:
            - string
            - 'null'
        folders:
          type: array
          items:
            type: string
        created_at:
          type: string
        updated_at:
          type: string
        is_deleted:
          type: boolean
        deleted_at:
          type:
            - string
            - 'null'
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