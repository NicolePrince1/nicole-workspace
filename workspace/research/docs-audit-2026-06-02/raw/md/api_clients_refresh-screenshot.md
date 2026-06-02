> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Refresh Screenshot

> Re-fetches the screenshot synchronously using the client's stored website and returns the new URL. Use this for user-triggered refresh on the dashboard card.



## OpenAPI

````yaml /api/openapi.json post /v1/clients/:id/screenshot/refresh
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
  /v1/clients/:id/screenshot/refresh:
    post:
      tags:
        - Clients
      summary: Refresh Screenshot
      description: >-
        Re-fetches the screenshot synchronously using the client's stored
        website and returns the new URL. Use this for user-triggered refresh on
        the dashboard card.
      parameters:
        - schema:
            type: string
          required: true
          name: id
          in: path
      responses:
        '200':
          description: Screenshot refreshed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RefreshScreenshotResponse'
        '400':
          description: Client has no website configured
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                required:
                  - error
        '404':
          description: Client not found
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
    RefreshScreenshotResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: object
          properties:
            screenshot:
              type:
                - string
                - 'null'
          required:
            - screenshot
      required:
        - success
        - data
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````