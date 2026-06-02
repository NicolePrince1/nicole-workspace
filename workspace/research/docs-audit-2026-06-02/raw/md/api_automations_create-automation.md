> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Automation

> Create a new automation for a project



## OpenAPI

````yaml /api/openapi.json post /v1/automations
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
  /v1/automations:
    post:
      tags:
        - Automations
      summary: Create Automation
      description: Create a new automation for a project
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateAutomationRequest'
      responses:
        '201':
          description: Automation created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateAutomationResponse'
        '404':
          description: Parent project not found
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
    CreateAutomationRequest:
      type: object
      properties:
        parent_id:
          type: string
          minLength: 1
          description: Project ID this automation belongs to
        name:
          type: string
        frequency:
          type: string
          enum:
            - daily
            - weekly
            - monthly
          example: weekly
        day:
          type: string
          example: monday
        hours:
          type: string
          example: '9'
        minutes:
          type: string
          example: '00'
        timezone:
          type: string
          example: America/New_York
        time_format:
          type: string
        recipients:
          type: array
          items:
            type: string
            format: email
          minItems: 1
        subject:
          type: string
          minLength: 1
        sender_email:
          type: string
        sender_name:
          type: string
        message:
          type: string
        date_text:
          type: string
      required:
        - parent_id
        - name
        - frequency
        - hours
        - minutes
        - timezone
        - time_format
        - recipients
        - subject
        - sender_email
        - sender_name
        - message
        - date_text
    CreateAutomationResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: object
          properties:
            automation_id:
              type: string
          required:
            - automation_id
      required:
        - success
        - data
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````