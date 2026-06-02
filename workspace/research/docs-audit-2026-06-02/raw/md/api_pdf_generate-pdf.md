> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generate PDF

> Enqueue a PDF generation job for a report.



## OpenAPI

````yaml /api/openapi.json post /v1/pdf/generate
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
  /v1/pdf/generate:
    post:
      tags:
        - PDF
      summary: Generate PDF
      description: Enqueue a PDF generation job for a report.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GeneratePdfRequest'
      responses:
        '202':
          description: PDF generation queued
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GeneratePdfResponse'
        '503':
          description: S3 not configured
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
    GeneratePdfRequest:
      type: object
      properties:
        project_id:
          type: string
          minLength: 1
          example: proj_abc123
        client_id:
          type: string
          minLength: 1
          example: client_xyz
        format:
          type: string
          enum:
            - A4
            - Letter
          example: A4
        orientation:
          type: string
          enum:
            - portrait
            - landscape
          example: portrait
      required:
        - project_id
        - client_id
        - format
        - orientation
    GeneratePdfResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: object
          properties:
            job_id:
              type: string
              example: pdf_job_abc123
            message:
              type: string
              example: PDF generation queued
          required:
            - job_id
            - message
      required:
        - success
        - data
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````