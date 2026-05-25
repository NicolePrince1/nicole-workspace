> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update User

> Edit a team member (role, allowed projects, name).



## OpenAPI

````yaml /api/openapi.json put /v1/users/:id
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
  /v1/users/:id:
    put:
      tags:
        - Users
      summary: Update User
      description: Edit a team member (role, allowed projects, name).
      parameters:
        - schema:
            type: string
          required: true
          name: id
          in: path
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EditUserRequest'
      responses:
        '200':
          description: User updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
        '403':
          description: Cannot edit a user from a different account
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                required:
                  - error
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
    EditUserRequest:
      type: object
      properties:
        fullname:
          type: string
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