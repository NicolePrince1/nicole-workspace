> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Project

> Create a new project.



## OpenAPI

````yaml /api/openapi.json post /v1/projects
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
  /v1/projects:
    post:
      tags:
        - Projects
      summary: Create Project
      description: Create a new project.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateProjectRequest'
      responses:
        '201':
          description: Project created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateProjectResponse'
components:
  schemas:
    CreateProjectRequest:
      type: object
      properties:
        name:
          type: string
          minLength: 1
          example: Q1 Report
        client_id:
          type: string
          example: cliAbc123
        type:
          type: string
          example: REPORT
        template:
          type: string
        template_id:
          type: string
          description: Clone pages and widgets from this template into the new project
        pages:
          type: array
          items:
            type: object
            additionalProperties: {}
        theme_id:
          type: string
        date_text:
          type: string
        logo_url:
          type: string
        auto_refresh_enabled:
          type: boolean
        show_cover_page:
          type: boolean
        show_cover_page_logo:
          type: boolean
        show_cover_page_name:
          type: boolean
        show_cover_page_date:
          type: boolean
        show_cover_page_bg_image:
          type: boolean
        show_header:
          type: boolean
        show_header_logo:
          type: boolean
        show_header_name:
          type: boolean
        show_header_date:
          type: boolean
        show_page_numbers:
          type: boolean
        show_table_of_contents:
          type: boolean
        show_date:
          type: boolean
        show_thank_you:
          type: boolean
        thank_you_heading:
          type: string
        thank_you_paragraph:
          type: string
        thank_you_logo_url:
          type: string
        description:
          type: string
        status:
          type: string
        og_image_url:
          type: string
        date_compare:
          type: string
        date_include_today:
          type: boolean
        date_current_start:
          type: string
        date_current_end:
          type: string
        date_previous_start:
          type: string
        date_previous_end:
          type: string
        date_custom_days:
          type: number
        date_custom_months:
          type: number
        auto_refresh_interval:
          type: string
        password_enabled:
          type: boolean
        password:
          type: string
        pdf_enabled:
          type: boolean
      required:
        - name
        - type
        - template
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