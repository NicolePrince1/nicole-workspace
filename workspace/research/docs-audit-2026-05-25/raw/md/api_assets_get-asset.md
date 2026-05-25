> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Asset

> Get a single asset by ID



## OpenAPI

````yaml /api/openapi.json get /v1/assets/:id
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
  /v1/assets/:id:
    get:
      tags:
        - Assets
      summary: Get Asset
      description: Get a single asset by ID
      parameters:
        - schema:
            type: string
          required: true
          name: id
          in: path
      responses:
        '200':
          description: Asset
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetAssetResponse'
        '404':
          description: Asset not found
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
    GetAssetResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          $ref: '#/components/schemas/Asset'
      required:
        - success
        - data
    Asset:
      type: object
      properties:
        id:
          type: string
        account_id:
          type: string
        name:
          type: string
        description:
          type: string
        type:
          type: string
        tags:
          type: array
          items:
            type: string
        datasources:
          type: array
          items:
            type: string
        ranking:
          type:
            - number
            - 'null'
        created_at: {}
      required:
        - id
        - account_id
        - name
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````