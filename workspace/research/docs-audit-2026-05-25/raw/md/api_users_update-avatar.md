> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Avatar

> Update the current user profile picture.



## OpenAPI

````yaml /api/openapi.json put /v1/users/me/avatar
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
  /v1/users/me/avatar:
    put:
      tags:
        - Users
      summary: Update Avatar
      description: Update the current user profile picture.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateAvatarRequest'
      responses:
        '200':
          description: Avatar updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
components:
  schemas:
    UpdateAvatarRequest:
      type: object
      properties:
        avatar_url:
          type: string
          example: https://cdn.example.com/avatar.jpg
      required:
        - avatar_url
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