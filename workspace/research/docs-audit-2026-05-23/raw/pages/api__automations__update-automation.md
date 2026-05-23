> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Automation

> Update automation schedule and notification settings



## OpenAPI

````yaml /api/openapi.json put /v1/automations/:id
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
  /v1/automations/:id:
    put:
      tags:
        - Automations
      summary: Update Automation
      description: Update automation schedule and notification settings
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
              $ref: '#/components/schemas/UpdateAutomationRequest'
      responses:
        '200':
          description: Automation updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
        '404':
          description: Automation or project not found
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
    UpdateAutomationRequest:
      type: object
      properties:
        name:
          type: string
        frequency:
          type: string
          enum:
            - daily
            - weekly
            - monthly
        hours:
          type: string
        minutes:
          type: string
        timezone:
          type: string
        time_format:
          type: string
        recipients:
          type: array
          items:
            type: string
            format: email
        subject:
          type: string
        sender_email:
          type: string
        sender_name:
          type: string
        message:
          type: string
        date_text:
          type: string
        day:
          type: string
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