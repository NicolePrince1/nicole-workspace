> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Duplicate Project

> Duplicate a project — deep copy of pages, widgets, and settings.



## OpenAPI

````yaml /api/openapi.json post /v1/projects/{id}/duplicate
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
  /v1/projects/{id}/duplicate:
    post:
      tags:
        - Projects
      summary: Duplicate Project
      description: Duplicate a project — deep copy of pages, widgets, and settings.
      parameters:
        - schema:
            type: string
          required: true
          name: id
          in: path
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DuplicateProjectRequest'
      responses:
        '201':
          description: Duplicate project created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateProjectResponse'
        '404':
          description: Source project not found
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
    DuplicateProjectRequest:
      type: object
      properties:
        name:
          type: string
          minLength: 1
          example: Q1 Report (Copy)
      required:
        - name
    CreateProjectResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: object
          properties:
            id:
              type: string
          required:
            - id
      required:
        - success
        - data
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````