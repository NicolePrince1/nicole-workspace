> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oviond.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Widgets

> List widgets for a source.



## OpenAPI

````yaml /api/openapi.json get /v1/widgets
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
  /v1/widgets:
    get:
      tags:
        - Widgets
      summary: List Widgets
      description: List widgets for a source.
      parameters:
        - schema:
            type: string
            example: project
          required: false
          name: source_type
          in: query
        - schema:
            type: string
            example: proj123
          required: true
          name: source_id
          in: query
        - schema:
            type: string
            example: page123
          required: false
          name: page_id
          in: query
      responses:
        '200':
          description: Widget list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListWidgetsResponse'
components:
  schemas:
    ListWidgetsResponse:
      type: object
      properties:
        success:
          type: boolean
          enum:
            - true
        data:
          type: array
          items:
            $ref: '#/components/schemas/Widget'
      required:
        - success
        - data
    Widget:
      type: object
      properties:
        id:
          type: string
          example: widget123
        account_id:
          type: string
          example: ov:26AbCd
        source_type:
          type: string
          example: project
        source_id:
          type: string
          example: proj123
        page_id:
          type: string
        client_id:
          type: string
        type:
          type: string
          enum:
            - DATA
            - TEXT
            - TEXT_V2
            - IMAGE
            - HTML
            - VIDEO
            - EMBED
            - TITLE
            - BUTTON
            - GOAL
          example: DATA
        chart:
          type: string
        chart_type:
          type: string
        chart_group:
          type: string
        state:
          type: string
        name:
          type: string
        title:
          type: string
        heading:
          type: string
        text:
          type: string
        align:
          type: string
        link:
          type: string
        link_url:
          type: string
        image_fit:
          type: string
        embed_type:
          type: string
        size:
          type: string
        x:
          type: number
        'y':
          type: number
        width:
          type: number
        height:
          type: number
        is_secondary:
          type: boolean
        icon_position:
          type: string
        options_3d:
          type: boolean
        kpi:
          type: boolean
        blended:
          type: boolean
        row_limit:
          type: string
        sort_order:
          type: string
        sort_by:
          type: string
        datasource_id:
          type: string
        datasource_type:
          type: string
        data_view:
          type: string
        metrics:
          type: array
          items:
            type: object
            additionalProperties: {}
        dimensions:
          type: array
          items:
            type: object
            additionalProperties: {}
        filters: {}
        advanced:
          type: object
          additionalProperties: {}
        show_header:
          type: boolean
        show_icon:
          type: boolean
        show_date:
          type: boolean
        show_grid_lines:
          type: boolean
        show_legends:
          type: boolean
        show_x_axis:
          type: boolean
        show_y_axis:
          type: boolean
        show_trendline:
          type: boolean
        show_totals:
          type: boolean
        show_table_filters:
          type: boolean
        show_logarithmic:
          type: boolean
        show_multiple_axes:
          type: boolean
        show_custom_date_range:
          type: boolean
        expand_rows:
          type: boolean
        date_text:
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
        created_at: {}
      required:
        - id
        - account_id
        - source_type
        - source_id
        - type
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````