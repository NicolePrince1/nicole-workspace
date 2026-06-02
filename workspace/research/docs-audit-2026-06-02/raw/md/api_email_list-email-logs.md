> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Email Logs

> Get email logs



## OpenAPI

````yaml /api/openapi.json get /v1/email/logs
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
  /v1/email/logs:
    get:
      tags:
        - Email
      summary: List Email Logs
      description: Get email logs
      parameters:
        - schema:
            type:
              - number
              - 'null'
            default: 1
          required: false
          name: page
          in: query
        - schema:
            type:
              - number
              - 'null'
            default: 20
          required: false
          name: limit
          in: query
      responses:
        '200':
          description: Email logs
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  data:
                    type: array
                    items: {}
                  meta: {}
                required:
                  - success
                  - data
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````