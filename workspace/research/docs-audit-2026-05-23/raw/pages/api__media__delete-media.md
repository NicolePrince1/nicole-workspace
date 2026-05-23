> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Media

> Soft-delete a media item. The underlying file is retained in S3 for potential restore.



## OpenAPI

````yaml /api/openapi.json delete /v1/media/:id
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
  /v1/media/:id:
    delete:
      tags:
        - Media
      summary: Delete Media
      description: >-
        Soft-delete a media item. The underlying file is retained in S3 for
        potential restore.
      parameters:
        - schema:
            type: string
          required: true
          name: id
          in: path
      responses:
        '200':
          description: Media deleted
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
        '404':
          description: Media not found
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