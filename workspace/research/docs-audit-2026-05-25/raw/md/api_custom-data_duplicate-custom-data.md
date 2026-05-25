> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Duplicate Custom Data

> Duplicate a custom dataset



## OpenAPI

````yaml /api/openapi.json post /v1/custom-data/{id}/duplicate
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
  /v1/custom-data/{id}/duplicate:
    post:
      tags:
        - Custom Data
      summary: Duplicate Custom Data
      description: Duplicate a custom dataset
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
              $ref: '#/components/schemas/DuplicateCustomDataRequest'
      responses:
        '201':
          description: Duplicate dataset created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DuplicateCustomDataResponse'
        '404':
          description: Source dataset not found
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
    DuplicateCustomDataRequest:
      type: object
      properties:
        new_name:
          type: string
          minLength: 1
          example: Monthly Revenue (Copy)
      required:
        - new_name
    DuplicateCustomDataResponse:
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