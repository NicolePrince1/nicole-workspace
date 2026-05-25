> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Send Email

> Send a transactional email via Resend



## OpenAPI

````yaml /api/openapi.json post /v1/email/send
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
  /v1/email/send:
    post:
      tags:
        - Email
      summary: Send Email
      description: Send a transactional email via Resend
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SendEmailRequest'
      responses:
        '200':
          description: Email sent
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SendEmailResponse'
components:
  schemas:
    SendEmailRequest:
      type: object
      properties:
        from:
          type: string
          minLength: 1
          example: reports@acme.com
        to:
          anyOf:
            - type: string
              format: email
            - type: array
              items:
                type: string
                format: email
          example: client@example.com
        subject:
          type: string
          minLength: 1
          example: Your monthly report
        html:
          type: string
          minLength: 1
          example: <p>Hello!</p>
      required:
        - from
        - to
        - subject
        - html
    SendEmailResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: object
          properties:
            id:
              type: string
          required:
            - id
      required:
        - success
        - data
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````