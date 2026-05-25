> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Account

> Irreversible. Cancels the active Stripe subscription, deletes all data across every table for this account, removes all team members from the users table, purges all S3 media files, and deletes all Supabase Auth users. Requires the account owner's current password as a confirmation gate.



## OpenAPI

````yaml /api/openapi.json delete /v1/account
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
  /v1/account:
    delete:
      tags:
        - Account
      summary: Delete Account
      description: >-
        Irreversible. Cancels the active Stripe subscription, deletes all data
        across every table for this account, removes all team members from the
        users table, purges all S3 media files, and deletes all Supabase Auth
        users. Requires the account owner's current password as a confirmation
        gate.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DeleteAccountRequest'
      responses:
        '200':
          description: Account deleted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteAccountResponse'
        '401':
          description: Unauthorized or wrong password
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
          description: Account or user not found
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
    DeleteAccountRequest:
      type: object
      properties:
        password:
          type: string
          minLength: 1
          example: correct-horse-battery-staple
      required:
        - password
    DeleteAccountResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        message:
          type: string
      required:
        - success
        - message
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````