> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Health Check



## OpenAPI

````yaml /api/openapi.json get /v1/health
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
  /v1/health:
    get:
      tags:
        - Health
      summary: Health Check
      responses:
        '200':
          description: Service is healthy or degraded
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    enum:
                      - healthy
                      - degraded
                      - unhealthy
                  timestamp:
                    type: string
                  uptime:
                    type: number
                  version:
                    type: string
                  checks:
                    type: object
                    properties:
                      supabase:
                        type: boolean
                    required:
                      - supabase
                required:
                  - status
                  - timestamp
                  - uptime
                  - version
                  - checks
      security: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````