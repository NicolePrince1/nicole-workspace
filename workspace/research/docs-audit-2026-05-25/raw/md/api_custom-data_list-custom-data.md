> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Custom Data

> List custom datasets for the current account (no raw_data)



## OpenAPI

````yaml /api/openapi.json get /v1/custom-data
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
    get:
      tags:
        - Custom Data
      summary: List Custom Data
      description: List custom datasets for the current account (no raw_data)
      responses:
        '200':
          description: Custom data list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListCustomDataResponse'
components:
  schemas:
    ListCustomDataResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: array
          items:
            $ref: '#/components/schemas/CustomDataSummary'
      required:
        - success
        - data
    CustomDataSummary:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        file_name:
          type:
            - string
            - 'null'
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
    CustomDataColumn:
      type: object
      additionalProperties: {}
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````