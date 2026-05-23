> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Test SMTP

> Send a test email using the account SMTP configuration



## OpenAPI

````yaml /api/openapi.json post /v1/email/smtp/test
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
  /v1/email/smtp/test:
    post:
      tags:
        - Email
      summary: Test SMTP
      description: Send a test email using the account SMTP configuration
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TestSmtpRequest'
      responses:
        '200':
          description: Test email sent
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
        '422':
          description: SMTP not configured
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
    TestSmtpRequest:
      type: object
      properties:
        to:
          type: string
          format: email
          example: user@example.com
      required:
        - to
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