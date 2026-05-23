> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Domain

> Remove a custom domain.



## OpenAPI

````yaml /api/openapi.json delete /v1/white-label/domains/:domain_id
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
  /v1/white-label/domains/:domain_id:
    delete:
      tags:
        - White Label
      summary: Delete Domain
      description: Remove a custom domain.
      parameters:
        - schema:
            type: string
          required: true
          name: domain_id
          in: path
      responses:
        '200':
          description: Domain removed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/WhiteLabelSuccessResponse'
        '404':
          description: Domain not found
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
    WhiteLabelSuccessResponse:
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