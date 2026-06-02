> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get User

> Get the currently authenticated user profile.



## OpenAPI

````yaml /api/openapi.json get /v1/users/me
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
  /v1/users/me:
    get:
      tags:
        - Users
      summary: Get User
      description: Get the currently authenticated user profile.
      responses:
        '200':
          description: Current user profile
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MeResponse'
        '404':
          description: User not found
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
    MeResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          $ref: '#/components/schemas/TeamMember'
      required:
        - success
        - data
    TeamMember:
      type: object
      properties:
        id:
          type: string
          example: abc123
        account_id:
          type: string
          example: ov:26AbCdEfGhIjKlMnOp
        fullname:
          type: string
          example: Jane Smith
        email:
          type: string
          format: email
          example: jane@example.com
        email_verified:
          type: boolean
          example: true
        role:
          type: string
          example: admin
        avatar_url:
          type:
            - string
            - 'null'
          example: /img/profilePicture.jpg
        allowed_projects:
          type:
            - array
            - 'null'
          items:
            type: string
          example: []
        language:
          type:
            - string
            - 'null'
          example: en
        theme:
          type:
            - string
            - 'null'
          example: dark
        created_at:
          type:
            - string
            - 'null'
          example: '2024-01-01T00:00:00.000Z'
      required:
        - id
        - account_id
        - fullname
        - email
        - email_verified
        - role
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````