> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Asset

> Update an asset



## OpenAPI

````yaml /api/openapi.json put /v1/assets/:id
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
    put:
      tags:
        - Assets
      summary: Update Asset
      description: Update an asset
      parameters:
        - schema:
            type: string
          required: true
          name: id
          in: path
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateAssetRequest'
      responses:
        '200':
          description: Asset updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
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
    UpdateAssetRequest:
      type: object
      properties:
        name:
          type: string
        type:
          type: string
        description:
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
          type: number
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