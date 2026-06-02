> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List All Projects

> List all projects (id + name only) for dropdown selectors.



## OpenAPI

````yaml /api/openapi.json get /v1/projects/all
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
  /v1/projects/all:
    get:
      tags:
        - Projects
      summary: List All Projects
      description: List all projects (id + name only) for dropdown selectors.
      parameters:
        - schema:
            type: string
          required: false
          name: client_id
          in: query
      responses:
        '200':
          description: All projects
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
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                        name:
                          type: string
                      required:
                        - id
                        - name
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