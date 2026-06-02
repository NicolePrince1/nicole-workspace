> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Profile

> Delete an auth connection



## OpenAPI

````yaml /api/openapi.json delete /v1/integrations/:integrationID/profiles/:profileName
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
  /v1/integrations/:integrationID/profiles/:profileName:
    delete:
      tags:
        - Integrations
      summary: Delete Profile
      description: Delete an auth connection
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
      responses:
        '200':
          description: Profile deleted
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