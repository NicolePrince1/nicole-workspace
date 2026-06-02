> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Test Automation

> Trigger a test execution of an automation



## OpenAPI

````yaml /api/openapi.json post /v1/automations/:id/test
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
  /v1/automations/:id/test:
    post:
      tags:
        - Automations
      summary: Test Automation
      description: Trigger a test execution of an automation
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
              $ref: '#/components/schemas/TestAutomationRequest'
      responses:
        '200':
          description: Test triggered
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TestAutomationResponse'
components:
  schemas:
    TestAutomationRequest:
      type: object
      properties:
        recipients:
          type: array
          items:
            type: string
            format: email
          minItems: 1
          example:
            - test@example.com
      required:
        - recipients
    TestAutomationResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: object
          additionalProperties: {}
      required:
        - success
        - data
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````