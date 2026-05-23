> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Queue Emails

> Enqueue a batch of emails to SQS for async delivery, falling back to direct Resend when SQS is not configured



## OpenAPI

````yaml /api/openapi.json post /v1/email/queue
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
  /v1/email/queue:
    post:
      tags:
        - Email
      summary: Queue Emails
      description: >-
        Enqueue a batch of emails to SQS for async delivery, falling back to
        direct Resend when SQS is not configured
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/QueueEmailRequest'
      responses:
        '200':
          description: Emails queued or sent
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/QueueEmailResponse'
components:
  schemas:
    QueueEmailRequest:
      type: object
      properties:
        emails:
          type: array
          items:
            $ref: '#/components/schemas/QueueEmailItem'
          minItems: 1
          example: []
      required:
        - emails
    QueueEmailResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: object
          properties:
            queued:
              type: number
              example: 3
            sent:
              type: number
              example: 0
            method:
              type: string
              enum:
                - sqs
                - direct
              example: sqs
          required:
            - queued
            - sent
            - method
      required:
        - success
        - data
    QueueEmailItem:
      type: object
      properties:
        to:
          type: string
          format: email
          example: client@example.com
        from:
          type: string
          minLength: 1
          example: reports@acme.com
        subject:
          type: string
          minLength: 1
          example: Your monthly report
        html:
          type: string
          minLength: 1
          example: <p>Hello!</p>
        account_id:
          type: string
          minLength: 1
          example: account_123
      required:
        - to
        - from
        - subject
        - html
        - account_id
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````