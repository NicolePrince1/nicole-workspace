> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Restore Items

> Restore soft-deleted items



## OpenAPI

````yaml /api/openapi.json put /v1/archive/restore
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
  /v1/archive/restore:
    put:
      tags:
        - Archive
      summary: Restore Items
      description: Restore soft-deleted items
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ArchiveBulkBody'
      responses:
        '200':
          description: Items restored
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    enum:
                      - true
                  message:
                    type: string
                required:
                  - success
                  - message
components:
  schemas:
    ArchiveBulkBody:
      type: object
      properties:
        ids:
          type: array
          items:
            type: string
          minItems: 1
        type:
          type: string
          enum:
            - clients
            - projects
            - media
            - automations
      required:
        - ids
        - type
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````