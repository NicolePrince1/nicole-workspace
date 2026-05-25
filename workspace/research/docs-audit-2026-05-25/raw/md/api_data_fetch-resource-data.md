> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Fetch Resource Data

> Proxy a resource data fetch (campaigns, videos, etc.) to api.oviond.com



## OpenAPI

````yaml /api/openapi.json post /v1/data/resource
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
  /v1/data/resource:
    post:
      tags:
        - Data
      summary: Fetch Resource Data
      description: Proxy a resource data fetch (campaigns, videos, etc.) to api.oviond.com
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DataResourceRequest'
      responses:
        '200':
          description: Resource data from upstream API
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
    DataResourceRequest:
      type: object
      properties:
        integration_id:
          type: string
          example: fb-ads
        client_id:
          type: string
          example: cliAbc123
        resource:
          type: string
          example: campaigns
        params:
          type: object
          additionalProperties: {}
      required:
        - integration_id
        - client_id
        - resource
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
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````