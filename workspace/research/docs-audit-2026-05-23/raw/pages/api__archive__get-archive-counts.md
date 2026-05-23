> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Archive Counts

> Archived item counts per type



## OpenAPI

````yaml /api/openapi.json get /v1/archive/counts
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
  /v1/archive/counts:
    get:
      tags:
        - Archive
      summary: Get Archive Counts
      description: Archived item counts per type
      responses:
        '200':
          description: Archived counts per type
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    enum:
                      - true
                  data:
                    type: object
                    properties:
                      clients:
                        type: number
                      projects:
                        type: number
                      media:
                        type: number
                      automations:
                        type: number
                      total:
                        type: number
                    required:
                      - clients
                      - projects
                      - media
                      - automations
                      - total
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