> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Custom Data

> Update a custom dataset



## OpenAPI

````yaml /api/openapi.json put /v1/custom-data/{id}
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
    put:
      tags:
        - Custom Data
      summary: Update Custom Data
      description: Update a custom dataset
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
              $ref: '#/components/schemas/UpdateCustomDataRequest'
      responses:
        '200':
          description: Dataset updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
        '400':
          description: Validation error
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                required:
                  - error
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
    UpdateCustomDataRequest:
      type: object
      properties:
        name:
          type: string
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
    SuccessResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
      required:
        - success
    CustomDataColumn:
      type: object
      additionalProperties: {}
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````