> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Change Email

> Change the current user email address.



## OpenAPI

````yaml /api/openapi.json put /v1/users/me/email
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
  /v1/users/me/email:
    put:
      tags:
        - Users
      summary: Change Email
      description: Change the current user email address.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ChangeEmailRequest'
      responses:
        '200':
          description: Email address updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
        '409':
          description: Email already in use
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
    ChangeEmailRequest:
      type: object
      properties:
        email_address:
          type: string
          format: email
          example: new@example.com
      required:
        - email_address
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