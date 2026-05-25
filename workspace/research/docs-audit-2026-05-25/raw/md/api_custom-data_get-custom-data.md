> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Custom Data

> Get a single custom dataset by ID (includes raw_data)



## OpenAPI

````yaml /api/openapi.json get /v1/custom-data/{id}
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
  /v1/custom-data/{id}:
    get:
      tags:
        - Custom Data
      summary: Get Custom Data
      description: Get a single custom dataset by ID (includes raw_data)
      parameters:
        - schema:
            type: string
          required: true
          name: id
          in: path
      responses:
        '200':
          description: Full custom data document
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CustomDataResponse'
        '404':
          description: Custom dataset not found
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
    CustomDataResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          $ref: '#/components/schemas/CustomData'
      required:
        - success
        - data
    CustomData:
      type: object
      properties:
        id:
          type: string
          example: cd123
        name:
          type: string
          example: Monthly Revenue
        file_name:
          type:
            - string
            - 'null'
        accountid:
          type: string
        raw_data:
          type: array
          items:
            type: array
            items: {}
        columns:
          type: array
          items:
            $ref: '#/components/schemas/CustomDataColumn'
        row_count:
          type: number
        file_size:
          type:
            - number
            - 'null'
        created_at: {}
        updated_at: {}
      required:
        - id
        - name
        - accountid
    CustomDataColumn:
      type: object
      additionalProperties: {}
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````