> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Project

> Update a project.



## OpenAPI

````yaml /api/openapi.json put /v1/projects/{id}
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
    put:
      tags:
        - Projects
      summary: Update Project
      description: Update a project.
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
              $ref: '#/components/schemas/UpdateProjectRequest'
      responses:
        '200':
          description: Project updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
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
    UpdateProjectRequest:
      type: object
      properties:
        name:
          type: string
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
        pages:
          type: array
          items:
            type: object
            additionalProperties: {}
        is_active:
          type: boolean
        editing:
          type: boolean
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