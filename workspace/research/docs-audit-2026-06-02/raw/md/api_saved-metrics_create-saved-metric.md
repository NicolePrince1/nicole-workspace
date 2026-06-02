> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Saved Metric

> Create a new saved metric.



## OpenAPI

````yaml /api/openapi.json post /v1/saved-metrics
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
  /v1/saved-metrics:
    post:
      tags:
        - Saved Metrics
      summary: Create Saved Metric
      description: Create a new saved metric.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateSavedMetricRequest'
      responses:
        '201':
          description: Saved metric created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateSavedMetricResponse'
components:
  schemas:
    CreateSavedMetricRequest:
      type: object
      properties:
        name:
          type: string
          minLength: 1
          example: Weekly Sessions
        description:
          type: string
        query:
          type: object
          additionalProperties: {}
      required:
        - name
        - query
    CreateSavedMetricResponse:
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