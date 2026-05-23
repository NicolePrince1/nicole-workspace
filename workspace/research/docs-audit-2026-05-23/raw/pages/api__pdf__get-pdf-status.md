> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get PDF Status

> Poll the status of a PDF generation job.



## OpenAPI

````yaml /api/openapi.json get /v1/pdf/status/:job_id
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
  /v1/pdf/status/:job_id:
    get:
      tags:
        - PDF
      summary: Get PDF Status
      description: Poll the status of a PDF generation job.
      parameters:
        - schema:
            type: string
            minLength: 1
          required: true
          name: job_id
          in: path
      responses:
        '200':
          description: Job status
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PdfStatusResponse'
        '404':
          description: Job not found
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
    PdfStatusResponse:
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
            status:
              type: string
              enum:
                - pending
                - processing
                - complete
                - failed
            url:
              type: string
              example: https://s3.amazonaws.com/bucket/pdf/report.pdf
            error:
              type: string
          required:
            - job_id
            - status
      required:
        - success
        - data
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````