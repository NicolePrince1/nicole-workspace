> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Custom Data

> Create a new custom dataset (max 10,000 rows)



## OpenAPI

````yaml /api/openapi.json post /v1/custom-data
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
  /v1/custom-data:
    post:
      tags:
        - Custom Data
      summary: Create Custom Data
      description: Create a new custom dataset (max 10,000 rows)
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateCustomDataRequest'
      responses:
        '201':
          description: Dataset created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateCustomDataResponse'
        '400':
          description: Validation error (e.g. row limit exceeded)
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
    CreateCustomDataRequest:
      type: object
      properties:
        name:
          type: string
          minLength: 1
          example: Monthly Revenue
        file_name:
          type: string
        raw_data:
          type: array
          items:
            type: array
            items: {}
          maxItems: 10000
        columns:
          type: array
          items:
            $ref: '#/components/schemas/CustomDataColumn'
        file_size:
          type: number
      required:
        - name
        - file_name
        - raw_data
        - columns
        - file_size
    CreateCustomDataResponse:
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
    CustomDataColumn:
      type: object
      additionalProperties: {}
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````