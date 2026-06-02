> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Calculated Metric

> Create a new calculated metric



## OpenAPI

````yaml /api/openapi.json post /v1/calculated-metrics
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
  /v1/calculated-metrics:
    post:
      tags:
        - Calculated Metrics
      summary: Create Calculated Metric
      description: Create a new calculated metric
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateCalculatedMetricRequest'
      responses:
        '201':
          description: Metric created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateCalculatedMetricResponse'
components:
  schemas:
    CreateCalculatedMetricRequest:
      type: object
      properties:
        name:
          type: string
          minLength: 1
          example: CTR
        formula:
          example:
            expression: clicks / impressions * 100
        symbol:
          type: string
          example: '%'
      required:
        - name
        - symbol
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