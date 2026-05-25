> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Automation History

> Get execution history for an automation



## OpenAPI

````yaml /api/openapi.json get /v1/automations/:id/history
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
  /v1/automations/:id/history:
    get:
      tags:
        - Automations
      summary: Get Automation History
      description: Get execution history for an automation
      parameters:
        - schema:
            type: string
          required: true
          name: id
          in: path
        - schema:
            type:
              - integer
              - 'null'
            minimum: 0
            default: 0
          required: false
          name: page
          in: query
        - schema:
            type: integer
            minimum: 1
            maximum: 50
            default: 5
          required: false
          name: limit
          in: query
      responses:
        '200':
          description: Execution history
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AutomationHistoryResponse'
components:
  schemas:
    AutomationHistoryResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: array
          items:
            type: object
            additionalProperties: {}
      required:
        - success
        - data
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````