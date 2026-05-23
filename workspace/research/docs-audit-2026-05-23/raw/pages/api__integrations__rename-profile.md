> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Rename Profile

> Rename an auth connection



## OpenAPI

````yaml /api/openapi.json put /v1/integrations/:integrationID/profiles/:profileName/rename
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
  /v1/integrations/:integrationID/profiles/:profileName/rename:
    put:
      tags:
        - Integrations
      summary: Rename Profile
      description: Rename an auth connection
      parameters:
        - schema:
            type: string
          required: true
          name: integrationID
          in: path
        - schema:
            type: string
          required: true
          name: profileName
          in: path
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                new_name:
                  type: string
              required:
                - new_name
      responses:
        '200':
          description: Profile renamed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
        '404':
          description: Profile not found
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