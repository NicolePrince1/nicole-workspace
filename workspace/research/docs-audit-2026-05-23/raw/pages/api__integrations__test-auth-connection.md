> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Test Auth Connection

> Test whether a stored auth connection is valid



## OpenAPI

````yaml /api/openapi.json post /v1/integrations/test
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
  /v1/integrations/test:
    post:
      tags:
        - Integrations
      summary: Test Auth Connection
      description: Test whether a stored auth connection is valid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TestAuthRequest'
      responses:
        '200':
          description: Connection test result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TestAuthResponse'
        '404':
          description: Auth not found
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
    TestAuthRequest:
      type: object
      properties:
        auth_id:
          type: string
          minLength: 1
          example: auth_abc123
        integration:
          type: string
          minLength: 1
          example: google
      required:
        - auth_id
        - integration
    TestAuthResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: object
          properties:
            connected:
              type: boolean
            message:
              type: string
          required:
            - connected
      required:
        - success
        - data
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````