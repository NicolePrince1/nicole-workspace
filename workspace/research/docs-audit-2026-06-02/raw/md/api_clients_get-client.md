> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Client

> Get a single client by ID



## OpenAPI

````yaml /api/openapi.json get /v1/clients/:id
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
  /v1/clients/:id:
    get:
      tags:
        - Clients
      summary: Get Client
      description: Get a single client by ID
      parameters:
        - schema:
            type: string
          required: true
          name: id
          in: path
      responses:
        '200':
          description: Client document
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ClientResponse'
        '404':
          description: Client not found
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
    ClientResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          $ref: '#/components/schemas/Client'
      required:
        - success
        - data
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