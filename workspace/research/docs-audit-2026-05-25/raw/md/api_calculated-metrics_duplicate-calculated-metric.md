> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Duplicate Calculated Metric

> Duplicate a calculated metric



## OpenAPI

````yaml /api/openapi.json post /v1/calculated-metrics/{id}/duplicate
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
  /v1/calculated-metrics/{id}/duplicate:
    post:
      tags:
        - Calculated Metrics
      summary: Duplicate Calculated Metric
      description: Duplicate a calculated metric
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
              $ref: '#/components/schemas/DuplicateCalculatedMetricRequest'
      responses:
        '201':
          description: Duplicate metric created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateCalculatedMetricResponse'
        '404':
          description: Source metric not found
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
    DuplicateCalculatedMetricRequest:
      type: object
      properties:
        new_name:
          type: string
          example: CTR (Copy)
      required:
        - new_name
    CreateCalculatedMetricResponse:
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