> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Users

> List all team members for the authenticated account.



## OpenAPI

````yaml /api/openapi.json get /v1/users
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
  /v1/users:
    get:
      tags:
        - Users
      summary: List Users
      description: List all team members for the authenticated account.
      parameters:
        - schema:
            type:
              - integer
              - 'null'
            minimum: 0
            default: 0
            example: 0
          required: false
          name: page
          in: query
        - schema:
            type: integer
            minimum: 1
            maximum: 100
            default: 20
            example: 20
          required: false
          name: limit
          in: query
      responses:
        '200':
          description: Paginated list of team members
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListUsersResponse'
components:
  schemas:
    ListUsersResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: array
          items:
            $ref: '#/components/schemas/TeamMember'
        meta:
          type: object
          properties:
            page:
              type: number
            limit:
              type: number
            total:
              type: number
          required:
            - page
            - limit
            - total
      required:
        - success
        - data
        - meta
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