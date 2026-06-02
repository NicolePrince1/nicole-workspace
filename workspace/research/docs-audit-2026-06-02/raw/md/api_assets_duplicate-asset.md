> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Duplicate Asset

> Duplicate an asset with a new name



## OpenAPI

````yaml /api/openapi.json post /v1/assets/:id/duplicate
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
  /v1/assets/:id/duplicate:
    post:
      tags:
        - Assets
      summary: Duplicate Asset
      description: Duplicate an asset with a new name
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
              $ref: '#/components/schemas/DuplicateAssetRequest'
      responses:
        '201':
          description: Asset duplicated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DuplicateAssetResponse'
        '404':
          description: Source asset not found
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
    DuplicateAssetRequest:
      type: object
      properties:
        name:
          type: string
          minLength: 1
          example: GA4 Traffic Widget (copy)
        description:
          type: string
        tags:
          type: array
          items:
            type: string
      required:
        - name
    DuplicateAssetResponse:
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