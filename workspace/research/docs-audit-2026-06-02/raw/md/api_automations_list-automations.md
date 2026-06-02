> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Automations

> List automations across all projects for the current account



## OpenAPI

````yaml /api/openapi.json get /v1/automations
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
    get:
      tags:
        - Automations
      summary: List Automations
      description: List automations across all projects for the current account
      parameters:
        - schema:
            type: string
            description: Filter by project ID
          required: false
          name: project_id
          in: query
        - schema:
            type: string
            description: Filter by client ID
          required: false
          name: client_id
          in: query
      responses:
        '200':
          description: Automation list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListAutomationsResponse'
components:
  schemas:
    ListAutomationsResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: array
          items:
            $ref: '#/components/schemas/Automation'
      required:
        - success
        - data
    Automation:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        parent_id:
          type: string
        frequency:
          type: string
        day:
          type: string
        hours:
          type: string
        minutes:
          type: string
        timezone:
          type: string
        recipients:
          type: array
          items:
            type: string
        subject:
          type: string
        sender_email:
          type: string
        sender_name:
          type: string
        message:
          type: string
        paused:
          type: boolean
        time_format:
          type: string
        date_text:
          type: string
        last_run_status:
          type: string
        last_run_at:
          type:
            - string
            - 'null'
        next_run_at:
          type:
            - string
            - 'null'
        is_deleted:
          type: boolean
        deleted_at:
          type:
            - string
            - 'null'
        created_at: {}
      required:
        - id
        - parent_id
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````