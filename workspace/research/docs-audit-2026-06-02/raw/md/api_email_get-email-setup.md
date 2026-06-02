> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Email Setup

> Get email setup configuration for the current account



## OpenAPI

````yaml /api/openapi.json get /v1/email/setup
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
    get:
      tags:
        - Email
      summary: Get Email Setup
      description: Get email setup configuration for the current account
      responses:
        '200':
          description: Email setup document
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EmailSetupResponse'
components:
  schemas:
    EmailSetupResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          $ref: '#/components/schemas/EmailSetup'
      required:
        - success
        - data
    EmailSetup:
      type:
        - object
        - 'null'
      properties:
        id:
          type: string
        account_id:
          type: string
        resend:
          type:
            - object
            - 'null'
          additionalProperties: {}
        senders:
          type:
            - array
            - 'null'
          items:
            type: object
            additionalProperties: {}
        smtp:
          type:
            - object
            - 'null'
          additionalProperties: {}
        use_smtp:
          type:
            - boolean
            - 'null'
        default_subject:
          type:
            - string
            - 'null'
        default_from:
          type:
            - string
            - 'null'
        default_from_name:
          type:
            - string
            - 'null'
        default_message:
          type:
            - string
            - 'null'
        default_button_text:
          type:
            - string
            - 'null'
        button_top:
          type:
            - boolean
            - 'null'
      required:
        - account_id
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````