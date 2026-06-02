> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk Delete Projects

> Delete multiple projects by ID.



## OpenAPI

````yaml /api/openapi.json delete /v1/projects/bulk
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
  /v1/projects/bulk:
    delete:
      tags:
        - Projects
      summary: Bulk Delete Projects
      description: Delete multiple projects by ID.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/BulkDeleteProjectsRequest'
      responses:
        '200':
          description: Projects deleted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
        '403':
          description: One or more projects do not belong to this account
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
    BulkDeleteProjectsRequest:
      type: object
      properties:
        ids:
          type: array
          items:
            type: string
          minItems: 1
          example:
            - proj123
            - proj456
      required:
        - ids
    SuccessResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
      required:
        - success
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````