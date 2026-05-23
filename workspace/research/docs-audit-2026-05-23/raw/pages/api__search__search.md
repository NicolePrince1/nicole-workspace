> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Search

> Search clients and projects by name (powers the command palette).



## OpenAPI

````yaml /api/openapi.json get /v1/search
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
  /v1/search:
    get:
      tags:
        - Search
      summary: Search
      description: Search clients and projects by name (powers the command palette).
      parameters:
        - schema:
            type: string
            minLength: 1
            example: acme
          required: true
          name: q
          in: query
      responses:
        '200':
          description: Search results across clients and projects
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SearchResponse'
        '400':
          description: Query too short
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
    SearchResponse:
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
              type: array
              items:
                type: object
                properties:
                  _id:
                    type: string
                  name:
                    type: string
                required:
                  - _id
                  - name
            projects:
              type: array
              items:
                type: object
                properties:
                  _id:
                    type: string
                  name:
                    type: string
                  client_id:
                    type: string
                  type:
                    type: string
                required:
                  - _id
                  - name
          required:
            - clients
            - projects
      required:
        - success
        - data
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````