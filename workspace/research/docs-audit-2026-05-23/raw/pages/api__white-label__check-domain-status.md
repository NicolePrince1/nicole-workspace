> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Check Domain Status

> Check domain verification status via Vercel.



## OpenAPI

````yaml /api/openapi.json get /v1/white-label/domains/:domain_id/status
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
  /v1/white-label/domains/:domain_id/status:
    get:
      tags:
        - White Label
      summary: Check Domain Status
      description: Check domain verification status via Vercel.
      parameters:
        - schema:
            type: string
          required: true
          name: domain_id
          in: path
      responses:
        '200':
          description: Domain status
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DomainResponse'
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
    DomainResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          $ref: '#/components/schemas/WhiteLabelDomain'
      required:
        - success
        - data
    WhiteLabelDomain:
      type: object
      properties:
        id:
          type: string
        domain:
          type: string
        status:
          $ref: '#/components/schemas/DomainStatus'
        provider:
          $ref: '#/components/schemas/DnsProvider'
        created_at:
          anyOf:
            - type: string
            - type: string
            - type: 'null'
        domain_records:
          type: array
          items:
            type: object
            properties:
              type:
                type: string
              name:
                type: string
              value:
                type: string
            required:
              - type
              - name
              - value
        vercel_verification:
          type: array
          items:
            type: object
            properties:
              type:
                type: string
              domain:
                type: string
              value:
                type: string
            required:
              - type
              - domain
              - value
        dns_records:
          type: array
          items:
            type: object
            properties:
              type:
                type: string
              name:
                type: string
              value:
                type: string
            required:
              - type
              - name
              - value
      required:
        - id
        - domain
        - status
    DomainStatus:
      type: string
      enum:
        - pending
        - verifying
        - active
        - failed
    DnsProvider:
      type:
        - string
        - 'null'
      enum:
        - cloudflare
        - godaddy
        - namecheap
        - route53
        - google
        - squarespace
        - unknown
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````