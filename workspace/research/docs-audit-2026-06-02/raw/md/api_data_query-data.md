> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Query Data

> Proxy an integration data query to api.oviond.com



## OpenAPI

````yaml /api/openapi.json post /v1/data/query
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
  /v1/data/query:
    post:
      tags:
        - Data
      summary: Query Data
      description: Proxy an integration data query to api.oviond.com
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DataQueryRequest'
      responses:
        '200':
          description: Query result from upstream API
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DataProxyResponse'
        '502':
          description: Upstream API error
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
    DataQueryRequest:
      type: object
      properties:
        integration_id:
          type: string
          example: ga4
        client_id:
          type: string
          example: cliAbc123
        date_current_start:
          type: string
          example: '2026-03-01'
        date_current_end:
          type: string
          example: '2026-03-31'
        date_previous_start:
          type: string
          example: '2026-02-01'
        date_previous_end:
          type: string
          example: '2026-02-28'
        metrics:
          type: array
          items:
            type: string
          example:
            - sessions
            - pageviews
        dimensions:
          type: array
          items:
            type: string
          example:
            - DATE
        data_view:
          type: string
          example: OVERVIEW
        filters:
          type: array
          items:
            $ref: '#/components/schemas/DataFilter'
        timezone:
          type: string
          default: UTC
        extra:
          type: object
          additionalProperties: {}
      required:
        - integration_id
        - client_id
        - date_current_start
        - date_current_end
        - metrics
        - dimensions
        - data_view
    DataProxyResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data: {}
      required:
        - success
    DataFilter:
      type: object
      properties:
        field:
          type: string
        operator:
          type: string
        value: {}
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````