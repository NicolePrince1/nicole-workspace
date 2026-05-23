> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Media Folders

> List media folders for the current account.



## OpenAPI

````yaml /api/openapi.json get /v1/media/folders
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
    get:
      tags:
        - Media
      summary: List Media Folders
      description: List media folders for the current account.
      responses:
        '200':
          description: Folder list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListMediaFoldersResponse'
components:
  schemas:
    ListMediaFoldersResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: array
          items:
            $ref: '#/components/schemas/MediaFolder'
      required:
        - success
        - data
    MediaFolder:
      type: object
      properties:
        id:
          type: string
        account_id:
          type: string
        name:
          type: string
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