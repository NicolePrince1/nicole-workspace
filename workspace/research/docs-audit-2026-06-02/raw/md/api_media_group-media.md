> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Group Media

> Move multiple media items to a folder



## OpenAPI

````yaml /api/openapi.json put /v1/media/group
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
  /v1/media/group:
    put:
      tags:
        - Media
      summary: Group Media
      description: Move multiple media items to a folder
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GroupMediaRequest'
      responses:
        '200':
          description: Media grouped
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
components:
  schemas:
    GroupMediaRequest:
      type: object
      properties:
        ids:
          type: array
          items:
            type: string
          minItems: 1
          example:
            - media1
            - media2
        folder_id:
          type: string
          example: folderAbc
      required:
        - ids
        - folder_id
    SuccessResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
      required:
        - success
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````