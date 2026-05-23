> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Media Folder

> Create a new media folder.



## OpenAPI

````yaml /api/openapi.json post /v1/media/folders
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
  /v1/media/folders:
    post:
      tags:
        - Media
      summary: Create Media Folder
      description: Create a new media folder.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateMediaFolderRequest'
      responses:
        '201':
          description: Folder created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateMediaFolderResponse'
components:
  schemas:
    CreateMediaFolderRequest:
      type: object
      properties:
        name:
          type: string
          minLength: 1
          example: Client Logos
      required:
        - name
    CreateMediaFolderResponse:
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