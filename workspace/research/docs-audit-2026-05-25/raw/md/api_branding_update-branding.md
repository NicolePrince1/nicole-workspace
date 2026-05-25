> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Branding

> Update branding settings



## OpenAPI

````yaml /api/openapi.json put /v1/branding
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
  /v1/branding:
    put:
      tags:
        - Branding
      summary: Update Branding
      description: Update branding settings
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateBrandingRequest'
      responses:
        '200':
          description: Updated
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    enum:
                      - true
                required:
                  - success
components:
  schemas:
    UpdateBrandingRequest:
      type: object
      properties:
        app_title:
          type: string
        logo_url:
          type: string
        favicon_url:
          type: string
        brand_color:
          type: string
        brand_palette:
          type: object
          additionalProperties: {}
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````