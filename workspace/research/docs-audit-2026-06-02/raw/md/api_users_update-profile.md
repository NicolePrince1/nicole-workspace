> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Profile

> Update the current user profile name, language, and theme.



## OpenAPI

````yaml /api/openapi.json put /v1/users/me/profile
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
  /v1/users/me/profile:
    put:
      tags:
        - Users
      summary: Update Profile
      description: Update the current user profile name, language, and theme.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateProfileRequest'
      responses:
        '200':
          description: Profile updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
components:
  schemas:
    UpdateProfileRequest:
      type: object
      properties:
        fullname:
          type: string
          minLength: 1
          example: Jane Smith
        language:
          type: string
          example: en
        theme:
          type: string
          enum:
            - light
            - dark
            - system
          example: dark
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