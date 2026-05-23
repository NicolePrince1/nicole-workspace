> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Folder

> Create a new client folder



## OpenAPI

````yaml /api/openapi.json post /v1/folders/clients
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
    post:
      tags:
        - Folders
      summary: Create Folder
      description: Create a new client folder
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateFolderRequest'
      responses:
        '201':
          description: Folder created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateFolderResponse'
components:
  schemas:
    CreateFolderRequest:
      type: object
      properties:
        name:
          type: string
          minLength: 1
          example: Top Clients
      required:
        - name
    CreateFolderResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: object
          properties:
            id:
              type: string
          required:
            - id
      required:
        - success
        - data
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````