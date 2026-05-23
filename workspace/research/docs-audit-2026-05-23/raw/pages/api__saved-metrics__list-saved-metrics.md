> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Saved Metrics

> List all saved metrics for the current account.



## OpenAPI

````yaml /api/openapi.json get /v1/saved-metrics
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
    get:
      tags:
        - Saved Metrics
      summary: List Saved Metrics
      description: List all saved metrics for the current account.
      responses:
        '200':
          description: Saved metrics list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListSavedMetricsResponse'
components:
  schemas:
    ListSavedMetricsResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: array
          items:
            $ref: '#/components/schemas/SavedMetric'
      required:
        - success
        - data
    SavedMetric:
      type: object
      properties:
        id:
          type: string
          example: savedMetric123
        name:
          type: string
          example: Weekly Sessions
        description:
          type: string
        query:
          type: object
          additionalProperties: {}
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