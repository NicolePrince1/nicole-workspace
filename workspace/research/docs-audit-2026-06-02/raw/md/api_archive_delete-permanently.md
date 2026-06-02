> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Permanently

> Permanently delete archived items



## OpenAPI

````yaml /api/openapi.json delete /v1/archive/permanent
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
  /v1/archive/permanent:
    delete:
      tags:
        - Archive
      summary: Delete Permanently
      description: Permanently delete archived items
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ArchiveBulkBody'
      responses:
        '200':
          description: Items permanently deleted
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