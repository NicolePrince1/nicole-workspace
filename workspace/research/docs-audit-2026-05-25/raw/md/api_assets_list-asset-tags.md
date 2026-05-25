> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Asset Tags

> List all unique tags across assets for the current account



## OpenAPI

````yaml /api/openapi.json get /v1/assets/tags
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
  /v1/assets/tags:
    get:
      tags:
        - Assets
      summary: List Asset Tags
      description: List all unique tags across assets for the current account
      responses:
        '200':
          description: Tag list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AssetTagsResponse'
components:
  schemas:
    AssetTagsResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: array
          items:
            type: string
      required:
        - success
        - data
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````