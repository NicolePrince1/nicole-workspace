> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Email Domain

> Remove a sending domain from Resend and the account config



## OpenAPI

````yaml /api/openapi.json delete /v1/email/domains/:id
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
  /v1/email/domains/:id:
    delete:
      tags:
        - Email
      summary: Delete Email Domain
      description: Remove a sending domain from Resend and the account config
      parameters:
        - schema:
            type: string
          required: true
          name: id
          in: path
      responses:
        '200':
          description: Domain removed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
components:
  schemas:
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