> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Asset

> Create a new asset



## OpenAPI

````yaml /api/openapi.json post /v1/assets
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
  /v1/assets:
    post:
      tags:
        - Assets
      summary: Create Asset
      description: Create a new asset
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateAssetRequest'
      responses:
        '201':
          description: Asset created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateAssetResponse'
components:
  schemas:
    CreateAssetRequest:
      type: object
      properties:
        name:
          type: string
          minLength: 1
          example: GA4 Traffic Widget
        description:
          type: string
        type:
          type: string
          example: chart
        tags:
          type: array
          items:
            type: string
        datasources:
          type: array
          items:
            type: string
      required:
        - name
        - type
    CreateAssetResponse:
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