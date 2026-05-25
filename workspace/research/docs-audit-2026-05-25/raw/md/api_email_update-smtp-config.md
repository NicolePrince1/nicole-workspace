> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update SMTP Config

> Store SMTP configuration for the account



## OpenAPI

````yaml /api/openapi.json put /v1/email/smtp
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
  /v1/email/smtp:
    put:
      tags:
        - Email
      summary: Update SMTP Config
      description: Store SMTP configuration for the account
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SmtpConfigRequest'
      responses:
        '200':
          description: SMTP config saved
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
components:
  schemas:
    SmtpConfigRequest:
      type: object
      properties:
        host:
          type: string
          minLength: 1
          example: smtp.example.com
        port:
          type: integer
          minimum: 1
          maximum: 65535
          example: 587
        username:
          type: string
          minLength: 1
          example: smtp_user
        password:
          type: string
          minLength: 1
          example: secret
        secure:
          type: boolean
        from_email:
          type: string
          format: email
          example: noreply@example.com
        from_name:
          type: string
          example: Acme Reports
      required:
        - host
        - port
        - username
        - password
        - secure
        - from_email
        - from_name
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