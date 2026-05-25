> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add Email Sender

> Add a sender to the email setup configuration



## OpenAPI

````yaml /api/openapi.json post /v1/email/setup
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
  /v1/email/setup:
    post:
      tags:
        - Email
      summary: Add Email Sender
      description: Add a sender to the email setup configuration
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateSenderRequest'
      responses:
        '200':
          description: Sender added
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
components:
  schemas:
    CreateSenderRequest:
      type: object
      properties:
        from_name:
          type: string
          minLength: 1
          example: Acme Reports
        email_address:
          type: string
          format: email
          example: reports@acme.com
        address:
          type: string
        city:
          type: string
        country:
          type: string
      required:
        - from_name
        - email_address
        - address
        - city
        - country
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