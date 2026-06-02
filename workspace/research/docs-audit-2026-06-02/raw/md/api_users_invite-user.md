> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Invite User

> Invite a new user to the account.



## OpenAPI

````yaml /api/openapi.json post /v1/users/invite
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
  /v1/users/invite:
    post:
      tags:
        - Users
      summary: Invite User
      description: Invite a new user to the account.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/InviteUserRequest'
      responses:
        '201':
          description: User invited
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/InviteUserResponse'
        '409':
          description: User already exists
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
    InviteUserRequest:
      type: object
      properties:
        email:
          type: string
          format: email
          example: colleague@example.com
        fullname:
          type: string
          minLength: 1
          example: John Doe
        role:
          type: string
          enum:
            - admin
            - projects
            - readonly
          example: admin
        allowed_projects:
          type: array
          items:
            type: string
          example: []
        avatar_url:
          type: string
          description: >-
            Optional starting avatar URL; defaults to a placeholder the user can
            replace.
      required:
        - email
        - fullname
        - role
    InviteUserResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: object
          properties:
            email:
              type: string
          required:
            - email
      required:
        - success
        - data
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````