> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Calculated Metrics

> List all calculated metrics for the current account



## OpenAPI

````yaml /api/openapi.json get /v1/calculated-metrics
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
    get:
      tags:
        - Calculated Metrics
      summary: List Calculated Metrics
      description: List all calculated metrics for the current account
      responses:
        '200':
          description: Calculated metrics list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListCalculatedMetricsResponse'
components:
  schemas:
    ListCalculatedMetricsResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: array
          items:
            $ref: '#/components/schemas/CalculatedMetric'
      required:
        - success
        - data
    CalculatedMetric:
      type: object
      properties:
        id:
          type: string
          example: metric123
        name:
          type: string
          example: CTR
        formula:
          example:
            expression: clicks / impressions * 100
        symbol:
          type: string
          example: '%'
        accountid:
          type: string
        created_at: {}
        updated_at: {}
      required:
        - id
        - name
        - accountid
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````