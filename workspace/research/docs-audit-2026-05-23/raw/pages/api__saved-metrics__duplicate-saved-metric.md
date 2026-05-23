> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Duplicate Saved Metric

> Clone a saved metric.



## OpenAPI

````yaml /api/openapi.json post /v1/saved-metrics/{id}/duplicate
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
  /v1/saved-metrics/{id}/duplicate:
    post:
      tags:
        - Saved Metrics
      summary: Duplicate Saved Metric
      description: Clone a saved metric.
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
              $ref: '#/components/schemas/DuplicateSavedMetricRequest'
      responses:
        '201':
          description: Duplicate saved metric created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateSavedMetricResponse'
        '404':
          description: Source saved metric not found
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
    DuplicateSavedMetricRequest:
      type: object
      properties:
        name:
          type: string
          minLength: 1
          example: Weekly Sessions (Copy)
        description:
          type: string
      required:
        - name
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