> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Folders

> List all client folders for the current account



## OpenAPI

````yaml /api/openapi.json get /v1/folders/clients
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
  /v1/folders/clients:
    get:
      tags:
        - Folders
      summary: List Folders
      description: List all client folders for the current account
      responses:
        '200':
          description: Client folder list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListFoldersResponse'
components:
  schemas:
    ListFoldersResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: array
          items:
            $ref: '#/components/schemas/Folder'
      required:
        - success
        - data
    Folder:
      type: object
      properties:
        _id:
          type: string
          example: folderXyz
        folderName:
          type: string
          example: Top Clients
        account_id:
          type: string
          example: ov:26AbCdEfGhIjKlMnOp
      required:
        - _id
        - folderName
        - account_id
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````