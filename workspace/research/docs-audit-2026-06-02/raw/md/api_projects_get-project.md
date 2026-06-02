> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Project

> Get a single project by ID.



## OpenAPI

````yaml /api/openapi.json get /v1/projects/{id}
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
  /v1/projects/{id}:
    get:
      tags:
        - Projects
      summary: Get Project
      description: Get a single project by ID.
      parameters:
        - schema:
            type: string
          required: true
          name: id
          in: path
      responses:
        '200':
          description: Project document
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ProjectResponse'
        '404':
          description: Project not found
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
    ProjectResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          $ref: '#/components/schemas/Project'
      required:
        - success
        - data
    Project:
      type: object
      properties:
        id:
          type: string
          example: proj123
        name:
          type: string
          example: Q1 Report
        account_id:
          type: string
          example: ov:26AbCdEfGhIjKlMnOp
        client_id:
          type: string
        type:
          type: string
          example: REPORT
        status:
          type: string
        nano_id:
          type: string
        created_at: {}
        is_deleted:
          type: boolean
        deleted_at:
          type:
            - string
            - 'null'
      required:
        - id
        - name
        - account_id
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````