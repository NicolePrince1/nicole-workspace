> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Company

> Update company settings



## OpenAPI

````yaml /api/openapi.json put /v1/company
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
  /v1/company:
    put:
      tags:
        - Company
      summary: Update Company
      description: Update company settings
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateCompanyRequest'
      responses:
        '200':
          description: Company settings updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
components:
  schemas:
    UpdateCompanyRequest:
      type: object
      properties:
        company_name:
          type: string
          example: Acme Corp
        timezone:
          type: string
          example: America/New_York
        website:
          type: string
          format: uri
          example: https://acme.com
        address:
          type: string
        state:
          type: string
        city:
          type: string
        zip:
          type: string
        country:
          type: string
        phone:
          type: string
      required:
        - company_name
        - timezone
        - website
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