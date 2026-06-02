{
  "openapi": "3.1.0",
  "info": {
    "title": "Oviond Backend API",
    "version": "1.0.0",
    "description": "Authentication, account management, billing, and media services for Oviond.",
    "x-logo": {
      "url": "https://app.oviond.com/img/oviond-full-logo.svg",
      "altText": "Oviond"
    }
  },
  "servers": [
    {
      "url": "https://api.oviond.com",
      "description": "Production"
    }
  ],
  "security": [
    {
      "BearerAuth": []
    }
  ],
  "components": {
    "securitySchemes": {
      "BearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT"
      }
    },
    "schemas": {
      "TeamMember": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "example": "abc123"
          },
          "account_id": {
            "type": "string",
            "example": "ov:26AbCdEfGhIjKlMnOp"
          },
          "fullname": {
            "type": "string",
            "example": "Jane Smith"
          },
          "email": {
            "type": "string",
            "format": "email",
            "example": "jane@example.com"
          },
          "email_verified": {
            "type": "boolean",
            "example": true
          },
          "role": {
            "type": "string",
            "example": "admin"
          },
          "avatar_url": {
            "type": [
              "string",
              "null"
            ],
            "example": "/img/profilePicture.jpg"
          },
          "allowed_projects": {
            "type": [
              "array",
              "null"
            ],
            "items": {
              "type": "string"
            },
            "example": []
          },
          "language": {
            "type": [
              "string",
              "null"
            ],
            "example": "en"
          },
          "theme": {
            "type": [
              "string",
              "null"
            ],
            "example": "dark"
          },
          "created_at": {
            "type": [
              "string",
              "null"
            ],
            "example": "2024-01-01T00:00:00.000Z"
          }
        },
        "required": [
          "id",
          "account_id",
          "fullname",
          "email",
          "email_verified",
          "role"
        ]
      },
      "MeResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "$ref": "#/components/schemas/TeamMember"
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "SuccessResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          }
        },
        "required": [
          "success"
        ]
      },
      "UpdateProfileRequest": {
        "type": "object",
        "properties": {
          "fullname": {
            "type": "string",
            "minLength": 1,
            "example": "Jane Smith"
          },
          "language": {
            "type": "string",
            "example": "en"
          },
          "theme": {
            "type": "string",
            "enum": [
              "light",
              "dark",
              "system"
            ],
            "example": "dark"
          }
        }
      },
      "UpdateAvatarRequest": {
        "type": "object",
        "properties": {
          "avatar_url": {
            "type": "string",
            "example": "https://cdn.example.com/avatar.jpg"
          }
        },
        "required": [
          "avatar_url"
        ]
      },
      "ChangeEmailRequest": {
        "type": "object",
        "properties": {
          "email_address": {
            "type": "string",
            "format": "email",
            "example": "new@example.com"
          }
        },
        "required": [
          "email_address"
        ]
      },
      "ListUsersResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/TeamMember"
            }
          },
          "meta": {
            "type": "object",
            "properties": {
              "page": {
                "type": "number"
              },
              "limit": {
                "type": "number"
              },
              "total": {
                "type": "number"
              }
            },
            "required": [
              "page",
              "limit",
              "total"
            ]
          }
        },
        "required": [
          "success",
          "data",
          "meta"
        ]
      },
      "InviteUserResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "email": {
                "type": "string"
              }
            },
            "required": [
              "email"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "InviteUserRequest": {
        "type": "object",
        "properties": {
          "email": {
            "type": "string",
            "format": "email",
            "example": "colleague@example.com"
          },
          "fullname": {
            "type": "string",
            "minLength": 1,
            "example": "John Doe"
          },
          "role": {
            "type": "string",
            "enum": [
              "admin",
              "projects",
              "readonly"
            ],
            "example": "admin"
          },
          "allowed_projects": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "example": []
          },
          "avatar_url": {
            "type": "string",
            "description": "Optional starting avatar URL; defaults to a placeholder the user can replace."
          }
        },
        "required": [
          "email",
          "fullname",
          "role"
        ]
      },
      "EditUserRequest": {
        "type": "object",
        "properties": {
          "fullname": {
            "type": "string",
            "example": "John Doe"
          },
          "role": {
            "type": "string",
            "enum": [
              "admin",
              "projects",
              "readonly"
            ],
            "example": "admin"
          },
          "allowed_projects": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "example": []
          }
        }
      },
      "AccountResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "additionalProperties": {}
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "AccountUsageResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "CURRENT_PLAN": {
                "type": "object",
                "properties": {
                  "PLAN": {
                    "type": "string"
                  },
                  "PLAN_ID": {
                    "type": "string"
                  },
                  "PRICE": {
                    "type": "number"
                  },
                  "PROJECTS": {
                    "anyOf": [
                      {
                        "type": "number"
                      },
                      {
                        "type": "string"
                      }
                    ],
                    "example": 15
                  },
                  "USERS": {
                    "anyOf": [
                      {
                        "type": "number"
                      },
                      {
                        "type": "string"
                      }
                    ],
                    "example": "UNLIMITED"
                  },
                  "WHITE_LABEL": {
                    "type": "boolean"
                  },
                  "CUSTOM_DOMAIN": {
                    "type": "boolean"
                  },
                  "PDF": {
                    "type": "boolean"
                  },
                  "AUTOMATIONS": {
                    "type": "boolean"
                  },
                  "AGENCY_TOOLS": {
                    "type": "boolean"
                  },
                  "EMAIL_SUPPORT": {
                    "type": "boolean"
                  },
                  "LIVE_SUPPORT": {
                    "type": "boolean"
                  },
                  "ACCOUNT_MANAGER": {
                    "type": "boolean"
                  }
                },
                "required": [
                  "PROJECTS",
                  "USERS"
                ]
              },
              "USAGE": {
                "type": "object",
                "properties": {
                  "PROJECTS": {
                    "type": "number",
                    "example": 3
                  },
                  "USERS": {
                    "type": "number",
                    "example": 2
                  }
                },
                "required": [
                  "PROJECTS",
                  "USERS"
                ]
              }
            },
            "required": [
              "CURRENT_PLAN",
              "USAGE"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "DeleteAccountResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "message": {
            "type": "string"
          }
        },
        "required": [
          "success",
          "message"
        ]
      },
      "DeleteAccountRequest": {
        "type": "object",
        "properties": {
          "password": {
            "type": "string",
            "minLength": 1,
            "example": "correct-horse-battery-staple"
          }
        },
        "required": [
          "password"
        ]
      },
      "CompanyResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "additionalProperties": {}
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "UpdateCompanyRequest": {
        "type": "object",
        "properties": {
          "company_name": {
            "type": "string",
            "example": "Acme Corp"
          },
          "timezone": {
            "type": "string",
            "example": "America/New_York"
          },
          "website": {
            "type": "string",
            "format": "uri",
            "example": "https://acme.com"
          },
          "address": {
            "type": "string"
          },
          "state": {
            "type": "string"
          },
          "city": {
            "type": "string"
          },
          "zip": {
            "type": "string"
          },
          "country": {
            "type": "string"
          },
          "phone": {
            "type": "string"
          }
        },
        "required": [
          "company_name",
          "timezone",
          "website"
        ]
      },
      "DomainStatus": {
        "type": "string",
        "enum": [
          "pending",
          "verifying",
          "active",
          "failed"
        ]
      },
      "DnsProvider": {
        "type": [
          "string",
          "null"
        ],
        "enum": [
          "cloudflare",
          "godaddy",
          "namecheap",
          "route53",
          "google",
          "squarespace",
          "unknown"
        ]
      },
      "WhiteLabelDomain": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "domain": {
            "type": "string"
          },
          "status": {
            "$ref": "#/components/schemas/DomainStatus"
          },
          "provider": {
            "$ref": "#/components/schemas/DnsProvider"
          },
          "created_at": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ]
          },
          "domain_records": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "type": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                },
                "value": {
                  "type": "string"
                }
              },
              "required": [
                "type",
                "name",
                "value"
              ]
            }
          },
          "vercel_verification": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "type": {
                  "type": "string"
                },
                "domain": {
                  "type": "string"
                },
                "value": {
                  "type": "string"
                }
              },
              "required": [
                "type",
                "domain",
                "value"
              ]
            }
          },
          "dns_records": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "type": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                },
                "value": {
                  "type": "string"
                }
              },
              "required": [
                "type",
                "name",
                "value"
              ]
            }
          }
        },
        "required": [
          "id",
          "domain",
          "status"
        ]
      },
      "DomainsListResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/WhiteLabelDomain"
            }
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "DomainResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "$ref": "#/components/schemas/WhiteLabelDomain"
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "AddDomainRequest": {
        "type": "object",
        "properties": {
          "domain": {
            "type": "string",
            "minLength": 1,
            "pattern": "^[a-zA-Z0-9][a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
          }
        },
        "required": [
          "domain"
        ]
      },
      "WhiteLabelSuccessResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          }
        },
        "required": [
          "success"
        ]
      },
      "UpdateBrandingRequest": {
        "type": "object",
        "properties": {
          "app_title": {
            "type": "string"
          },
          "logo_url": {
            "type": "string"
          },
          "favicon_url": {
            "type": "string"
          },
          "brand_color": {
            "type": "string"
          },
          "brand_palette": {
            "type": "object",
            "additionalProperties": {}
          }
        }
      },
      "Client": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "example": "cliAbc123"
          },
          "account_id": {
            "type": "string",
            "example": "ov:26AbCdEfGhIjKlMnOp"
          },
          "name": {
            "type": "string",
            "example": "Acme Website"
          },
          "website": {
            "type": "string"
          },
          "timezone": {
            "type": "string"
          },
          "screenshot": {
            "type": [
              "string",
              "null"
            ]
          },
          "folders": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "created_at": {
            "type": "string"
          },
          "updated_at": {
            "type": "string"
          },
          "is_deleted": {
            "type": "boolean"
          },
          "deleted_at": {
            "type": [
              "string",
              "null"
            ]
          }
        },
        "required": [
          "id",
          "account_id",
          "name"
        ]
      },
      "ListClientsResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Client"
            }
          },
          "meta": {
            "type": "object",
            "properties": {
              "page": {
                "type": "number"
              },
              "limit": {
                "type": "number"
              },
              "total": {
                "type": "number"
              }
            },
            "required": [
              "page",
              "limit",
              "total"
            ]
          }
        },
        "required": [
          "success",
          "data",
          "meta"
        ]
      },
      "ClientCountResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "count": {
                "type": "number"
              }
            },
            "required": [
              "count"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "BulkDeleteClientsRequest": {
        "type": "object",
        "properties": {
          "ids": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "minItems": 1,
            "example": [
              "cliAbc123",
              "cliDef456"
            ]
          }
        },
        "required": [
          "ids"
        ]
      },
      "ClientResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "$ref": "#/components/schemas/Client"
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateClientResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string"
              },
              "_id": {
                "type": "string"
              }
            },
            "required": [
              "id",
              "_id"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateClientRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "minLength": 1,
            "example": "Acme Corp"
          },
          "website": {
            "type": "string",
            "example": "https://acme.com"
          },
          "currency_code": {
            "type": "string",
            "example": "USD"
          },
          "currency_symbol": {
            "type": "string",
            "example": "$"
          },
          "timezone": {
            "type": "string",
            "example": "America/New_York"
          },
          "manager": {
            "type": "string"
          },
          "domain_id": {
            "type": "string"
          },
          "theme_id": {
            "type": "string"
          },
          "folders": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "name",
          "website",
          "currency_code",
          "currency_symbol",
          "timezone"
        ]
      },
      "UpdateClientRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "example": "Acme Corp Updated"
          },
          "website": {
            "type": "string"
          },
          "currency_code": {
            "type": "string"
          },
          "currency_symbol": {
            "type": "string"
          },
          "timezone": {
            "type": "string"
          },
          "manager": {
            "type": "string"
          },
          "domain_id": {
            "type": "string"
          },
          "theme_id": {
            "type": "string"
          },
          "folders": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        }
      },
      "RefreshScreenshotResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "screenshot": {
                "type": [
                  "string",
                  "null"
                ]
              }
            },
            "required": [
              "screenshot"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "MoveClientToFolderRequest": {
        "type": "object",
        "properties": {
          "folders": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "example": [
              "folderXyz"
            ]
          }
        },
        "required": [
          "folders"
        ]
      },
      "Folder": {
        "type": "object",
        "properties": {
          "_id": {
            "type": "string",
            "example": "folderXyz"
          },
          "folderName": {
            "type": "string",
            "example": "Top Clients"
          },
          "account_id": {
            "type": "string",
            "example": "ov:26AbCdEfGhIjKlMnOp"
          }
        },
        "required": [
          "_id",
          "folderName",
          "account_id"
        ]
      },
      "ListFoldersResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Folder"
            }
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateFolderResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string"
              }
            },
            "required": [
              "id"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateFolderRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "minLength": 1,
            "example": "Top Clients"
          }
        },
        "required": [
          "name"
        ]
      },
      "UpdateFolderRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "minLength": 1,
            "example": "VIP Clients"
          }
        },
        "required": [
          "name"
        ]
      },
      "Project": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "example": "proj123"
          },
          "name": {
            "type": "string",
            "example": "Q1 Report"
          },
          "account_id": {
            "type": "string",
            "example": "ov:26AbCdEfGhIjKlMnOp"
          },
          "client_id": {
            "type": "string"
          },
          "type": {
            "type": "string",
            "example": "REPORT"
          },
          "status": {
            "type": "string"
          },
          "nano_id": {
            "type": "string"
          },
          "created_at": {},
          "is_deleted": {
            "type": "boolean"
          },
          "deleted_at": {
            "type": [
              "string",
              "null"
            ]
          }
        },
        "required": [
          "id",
          "name",
          "account_id"
        ]
      },
      "ListProjectsResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Project"
            }
          },
          "meta": {
            "type": "object",
            "properties": {
              "page": {
                "type": "number"
              },
              "limit": {
                "type": "number"
              },
              "total": {
                "type": "number"
              }
            },
            "required": [
              "page",
              "limit",
              "total"
            ]
          }
        },
        "required": [
          "success",
          "data",
          "meta"
        ]
      },
      "BulkDeleteProjectsRequest": {
        "type": "object",
        "properties": {
          "ids": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "minItems": 1,
            "example": [
              "proj123",
              "proj456"
            ]
          }
        },
        "required": [
          "ids"
        ]
      },
      "ProjectResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "$ref": "#/components/schemas/Project"
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateProjectResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string"
              }
            },
            "required": [
              "id"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateProjectRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "minLength": 1,
            "example": "Q1 Report"
          },
          "client_id": {
            "type": "string",
            "example": "cliAbc123"
          },
          "type": {
            "type": "string",
            "example": "REPORT"
          },
          "template": {
            "type": "string"
          },
          "template_id": {
            "type": "string",
            "description": "Clone pages and widgets from this template into the new project"
          },
          "pages": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            }
          },
          "theme_id": {
            "type": "string"
          },
          "date_text": {
            "type": "string"
          },
          "logo_url": {
            "type": "string"
          },
          "auto_refresh_enabled": {
            "type": "boolean"
          },
          "show_cover_page": {
            "type": "boolean"
          },
          "show_cover_page_logo": {
            "type": "boolean"
          },
          "show_cover_page_name": {
            "type": "boolean"
          },
          "show_cover_page_date": {
            "type": "boolean"
          },
          "show_cover_page_bg_image": {
            "type": "boolean"
          },
          "show_header": {
            "type": "boolean"
          },
          "show_header_logo": {
            "type": "boolean"
          },
          "show_header_name": {
            "type": "boolean"
          },
          "show_header_date": {
            "type": "boolean"
          },
          "show_page_numbers": {
            "type": "boolean"
          },
          "show_table_of_contents": {
            "type": "boolean"
          },
          "show_date": {
            "type": "boolean"
          },
          "show_thank_you": {
            "type": "boolean"
          },
          "thank_you_heading": {
            "type": "string"
          },
          "thank_you_paragraph": {
            "type": "string"
          },
          "thank_you_logo_url": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "status": {
            "type": "string"
          },
          "og_image_url": {
            "type": "string"
          },
          "date_compare": {
            "type": "string"
          },
          "date_include_today": {
            "type": "boolean"
          },
          "date_current_start": {
            "type": "string"
          },
          "date_current_end": {
            "type": "string"
          },
          "date_previous_start": {
            "type": "string"
          },
          "date_previous_end": {
            "type": "string"
          },
          "date_custom_days": {
            "type": "number"
          },
          "date_custom_months": {
            "type": "number"
          },
          "auto_refresh_interval": {
            "type": "string"
          },
          "password_enabled": {
            "type": "boolean"
          },
          "password": {
            "type": "string"
          },
          "pdf_enabled": {
            "type": "boolean"
          }
        },
        "required": [
          "name",
          "type",
          "template"
        ]
      },
      "UpdateProjectRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "theme_id": {
            "type": "string"
          },
          "date_text": {
            "type": "string"
          },
          "logo_url": {
            "type": "string"
          },
          "auto_refresh_enabled": {
            "type": "boolean"
          },
          "show_cover_page": {
            "type": "boolean"
          },
          "show_cover_page_logo": {
            "type": "boolean"
          },
          "show_cover_page_name": {
            "type": "boolean"
          },
          "show_cover_page_date": {
            "type": "boolean"
          },
          "show_cover_page_bg_image": {
            "type": "boolean"
          },
          "show_header": {
            "type": "boolean"
          },
          "show_header_logo": {
            "type": "boolean"
          },
          "show_header_name": {
            "type": "boolean"
          },
          "show_header_date": {
            "type": "boolean"
          },
          "show_page_numbers": {
            "type": "boolean"
          },
          "show_table_of_contents": {
            "type": "boolean"
          },
          "show_date": {
            "type": "boolean"
          },
          "show_thank_you": {
            "type": "boolean"
          },
          "thank_you_heading": {
            "type": "string"
          },
          "thank_you_paragraph": {
            "type": "string"
          },
          "thank_you_logo_url": {
            "type": "string"
          },
          "pages": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            }
          },
          "is_active": {
            "type": "boolean"
          },
          "editing": {
            "type": "boolean"
          },
          "description": {
            "type": "string"
          },
          "status": {
            "type": "string"
          },
          "og_image_url": {
            "type": "string"
          },
          "date_compare": {
            "type": "string"
          },
          "date_include_today": {
            "type": "boolean"
          },
          "date_current_start": {
            "type": "string"
          },
          "date_current_end": {
            "type": "string"
          },
          "date_previous_start": {
            "type": "string"
          },
          "date_previous_end": {
            "type": "string"
          },
          "date_custom_days": {
            "type": "number"
          },
          "date_custom_months": {
            "type": "number"
          },
          "auto_refresh_interval": {
            "type": "string"
          },
          "password_enabled": {
            "type": "boolean"
          },
          "password": {
            "type": "string"
          },
          "pdf_enabled": {
            "type": "boolean"
          }
        }
      },
      "DuplicateProjectRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "minLength": 1,
            "example": "Q1 Report (Copy)"
          }
        },
        "required": [
          "name"
        ]
      },
      "Page": {
        "type": "object",
        "properties": {
          "page_id": {
            "type": "string",
            "example": "pg_abc123"
          },
          "source_id": {
            "type": "string"
          },
          "source_type": {
            "type": "string",
            "enum": [
              "project",
              "template"
            ]
          },
          "name": {
            "type": "string",
            "example": "Overview"
          },
          "position": {
            "type": "integer"
          },
          "visible": {
            "type": "boolean"
          }
        },
        "required": [
          "page_id",
          "source_id",
          "source_type",
          "name",
          "position",
          "visible"
        ]
      },
      "ListPagesResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Page"
            }
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreatePageResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "page_id": {
                "type": "string"
              }
            },
            "required": [
              "page_id"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreatePageRequest": {
        "type": "object",
        "properties": {
          "source_id": {
            "type": "string"
          },
          "source_type": {
            "type": "string",
            "enum": [
              "project",
              "template"
            ]
          },
          "name": {
            "type": "string",
            "minLength": 1
          },
          "position": {
            "type": "integer"
          },
          "visible": {
            "type": "boolean"
          }
        },
        "required": [
          "source_id",
          "source_type",
          "name"
        ]
      },
      "UpdatePageRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "minLength": 1
          },
          "position": {
            "type": "integer"
          },
          "visible": {
            "type": "boolean"
          }
        }
      },
      "SearchResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "clients": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "_id",
                    "name"
                  ]
                }
              },
              "projects": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "_id": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "client_id": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "_id",
                    "name"
                  ]
                }
              }
            },
            "required": [
              "clients",
              "projects"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "ListWidgetIDsResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "Widget": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "example": "widget123"
          },
          "account_id": {
            "type": "string",
            "example": "ov:26AbCd"
          },
          "source_type": {
            "type": "string",
            "example": "project"
          },
          "source_id": {
            "type": "string",
            "example": "proj123"
          },
          "page_id": {
            "type": "string"
          },
          "client_id": {
            "type": "string"
          },
          "type": {
            "type": "string",
            "enum": [
              "DATA",
              "TEXT",
              "TEXT_V2",
              "IMAGE",
              "HTML",
              "VIDEO",
              "EMBED",
              "TITLE",
              "BUTTON",
              "GOAL"
            ],
            "example": "DATA"
          },
          "chart": {
            "type": "string"
          },
          "chart_type": {
            "type": "string"
          },
          "chart_group": {
            "type": "string"
          },
          "state": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "title": {
            "type": "string"
          },
          "heading": {
            "type": "string"
          },
          "text": {
            "type": "string"
          },
          "align": {
            "type": "string"
          },
          "link": {
            "type": "string"
          },
          "link_url": {
            "type": "string"
          },
          "image_fit": {
            "type": "string"
          },
          "embed_type": {
            "type": "string"
          },
          "size": {
            "type": "string"
          },
          "x": {
            "type": "number"
          },
          "y": {
            "type": "number"
          },
          "width": {
            "type": "number"
          },
          "height": {
            "type": "number"
          },
          "is_secondary": {
            "type": "boolean"
          },
          "icon_position": {
            "type": "string"
          },
          "options_3d": {
            "type": "boolean"
          },
          "kpi": {
            "type": "boolean"
          },
          "blended": {
            "type": "boolean"
          },
          "row_limit": {
            "type": "string"
          },
          "sort_order": {
            "type": "string"
          },
          "sort_by": {
            "type": "string"
          },
          "datasource_id": {
            "type": "string"
          },
          "datasource_type": {
            "type": "string"
          },
          "data_view": {
            "type": "string"
          },
          "metrics": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            }
          },
          "dimensions": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            }
          },
          "filters": {},
          "advanced": {
            "type": "object",
            "additionalProperties": {}
          },
          "show_header": {
            "type": "boolean"
          },
          "show_icon": {
            "type": "boolean"
          },
          "show_date": {
            "type": "boolean"
          },
          "show_grid_lines": {
            "type": "boolean"
          },
          "show_legends": {
            "type": "boolean"
          },
          "show_x_axis": {
            "type": "boolean"
          },
          "show_y_axis": {
            "type": "boolean"
          },
          "show_trendline": {
            "type": "boolean"
          },
          "show_totals": {
            "type": "boolean"
          },
          "show_table_filters": {
            "type": "boolean"
          },
          "show_logarithmic": {
            "type": "boolean"
          },
          "show_multiple_axes": {
            "type": "boolean"
          },
          "show_custom_date_range": {
            "type": "boolean"
          },
          "expand_rows": {
            "type": "boolean"
          },
          "date_text": {
            "type": "string"
          },
          "date_compare": {
            "type": "string"
          },
          "date_include_today": {
            "type": "boolean"
          },
          "date_current_start": {
            "type": "string"
          },
          "date_current_end": {
            "type": "string"
          },
          "date_previous_start": {
            "type": "string"
          },
          "date_previous_end": {
            "type": "string"
          },
          "date_custom_days": {
            "type": "number"
          },
          "date_custom_months": {
            "type": "number"
          },
          "created_at": {}
        },
        "required": [
          "id",
          "account_id",
          "source_type",
          "source_id",
          "type"
        ]
      },
      "ListWidgetsResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Widget"
            }
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateWidgetsResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "inserted_count": {
                "type": "number"
              },
              "upserted_count": {
                "type": "number"
              }
            },
            "required": [
              "inserted_count",
              "upserted_count"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateWidgetsRequest": {
        "type": "object",
        "properties": {
          "widgets": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            },
            "minItems": 1
          },
          "source_type": {
            "type": "string",
            "example": "project"
          },
          "source_id": {
            "type": "string",
            "example": "proj123"
          },
          "client_id": {
            "type": "string"
          },
          "page_id": {
            "type": "string"
          },
          "account_id": {
            "type": "string"
          }
        },
        "required": [
          "widgets",
          "source_type",
          "source_id",
          "client_id",
          "page_id",
          "account_id"
        ]
      },
      "WidgetResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "$ref": "#/components/schemas/Widget"
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "UpdateWidgetRequest": {
        "type": "object",
        "additionalProperties": {}
      },
      "BulkDeleteWidgetsRequest": {
        "type": "object",
        "properties": {
          "ids": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "minItems": 1,
            "example": [
              "widget1",
              "widget2"
            ]
          }
        },
        "required": [
          "ids"
        ]
      },
      "DataProxyResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {}
        },
        "required": [
          "success"
        ]
      },
      "DataFilter": {
        "type": "object",
        "properties": {
          "field": {
            "type": "string"
          },
          "operator": {
            "type": "string"
          },
          "value": {}
        }
      },
      "DataQueryRequest": {
        "type": "object",
        "properties": {
          "integration_id": {
            "type": "string",
            "example": "ga4"
          },
          "client_id": {
            "type": "string",
            "example": "cliAbc123"
          },
          "date_current_start": {
            "type": "string",
            "example": "2026-03-01"
          },
          "date_current_end": {
            "type": "string",
            "example": "2026-03-31"
          },
          "date_previous_start": {
            "type": "string",
            "example": "2026-02-01"
          },
          "date_previous_end": {
            "type": "string",
            "example": "2026-02-28"
          },
          "metrics": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "example": [
              "sessions",
              "pageviews"
            ]
          },
          "dimensions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "example": [
              "DATE"
            ]
          },
          "data_view": {
            "type": "string",
            "example": "OVERVIEW"
          },
          "filters": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/DataFilter"
            }
          },
          "timezone": {
            "type": "string",
            "default": "UTC"
          },
          "extra": {
            "type": "object",
            "additionalProperties": {}
          }
        },
        "required": [
          "integration_id",
          "client_id",
          "date_current_start",
          "date_current_end",
          "metrics",
          "dimensions",
          "data_view"
        ]
      },
      "DataTestRequest": {
        "type": "object",
        "properties": {
          "integration_id": {
            "type": "string",
            "example": "ga4"
          },
          "client_id": {
            "type": "string",
            "example": "cliAbc123"
          },
          "credentials": {
            "type": "object",
            "additionalProperties": {}
          }
        },
        "required": [
          "integration_id",
          "client_id"
        ]
      },
      "DataAccountsRequest": {
        "type": "object",
        "properties": {
          "integration_id": {
            "type": "string",
            "example": "ga4"
          },
          "client_id": {
            "type": "string",
            "example": "cliAbc123"
          },
          "account_name": {
            "type": "string"
          },
          "params": {
            "type": "object",
            "additionalProperties": {}
          }
        },
        "required": [
          "integration_id",
          "client_id"
        ]
      },
      "DataResourceRequest": {
        "type": "object",
        "properties": {
          "integration_id": {
            "type": "string",
            "example": "fb-ads"
          },
          "client_id": {
            "type": "string",
            "example": "cliAbc123"
          },
          "resource": {
            "type": "string",
            "example": "campaigns"
          },
          "params": {
            "type": "object",
            "additionalProperties": {}
          }
        },
        "required": [
          "integration_id",
          "client_id",
          "resource"
        ]
      },
      "CalculatedMetric": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "example": "metric123"
          },
          "name": {
            "type": "string",
            "example": "CTR"
          },
          "formula": {
            "example": {
              "expression": "clicks / impressions * 100"
            }
          },
          "symbol": {
            "type": "string",
            "example": "%"
          },
          "accountid": {
            "type": "string"
          },
          "created_at": {},
          "updated_at": {}
        },
        "required": [
          "id",
          "name",
          "accountid"
        ]
      },
      "ListCalculatedMetricsResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CalculatedMetric"
            }
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateCalculatedMetricResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string"
              }
            },
            "required": [
              "id"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateCalculatedMetricRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "minLength": 1,
            "example": "CTR"
          },
          "formula": {
            "example": {
              "expression": "clicks / impressions * 100"
            }
          },
          "symbol": {
            "type": "string",
            "example": "%"
          }
        },
        "required": [
          "name",
          "symbol"
        ]
      },
      "UpdateCalculatedMetricRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "formula": {},
          "symbol": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "symbol"
        ]
      },
      "DuplicateCalculatedMetricRequest": {
        "type": "object",
        "properties": {
          "new_name": {
            "type": "string",
            "example": "CTR (Copy)"
          }
        },
        "required": [
          "new_name"
        ]
      },
      "SavedMetric": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "example": "savedMetric123"
          },
          "name": {
            "type": "string",
            "example": "Weekly Sessions"
          },
          "description": {
            "type": "string"
          },
          "query": {
            "type": "object",
            "additionalProperties": {}
          },
          "accountid": {
            "type": "string"
          },
          "created_at": {},
          "updated_at": {}
        },
        "required": [
          "id",
          "name",
          "accountid"
        ]
      },
      "ListSavedMetricsResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/SavedMetric"
            }
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateSavedMetricResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string"
              }
            },
            "required": [
              "id"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateSavedMetricRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "minLength": 1,
            "example": "Weekly Sessions"
          },
          "description": {
            "type": "string"
          },
          "query": {
            "type": "object",
            "additionalProperties": {}
          }
        },
        "required": [
          "name",
          "query"
        ]
      },
      "UpdateSavedMetricRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "query": {
            "type": "object",
            "additionalProperties": {}
          },
          "description": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "query"
        ]
      },
      "DuplicateSavedMetricRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "minLength": 1,
            "example": "Weekly Sessions (Copy)"
          },
          "description": {
            "type": "string"
          }
        },
        "required": [
          "name"
        ]
      },
      "CustomDataColumn": {
        "type": "object",
        "additionalProperties": {}
      },
      "CustomDataSummary": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "file_name": {
            "type": [
              "string",
              "null"
            ]
          },
          "columns": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CustomDataColumn"
            }
          },
          "row_count": {
            "type": "number"
          },
          "file_size": {
            "type": [
              "number",
              "null"
            ]
          },
          "created_at": {},
          "updated_at": {}
        },
        "required": [
          "id",
          "name"
        ]
      },
      "ListCustomDataResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CustomDataSummary"
            }
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CustomData": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "example": "cd123"
          },
          "name": {
            "type": "string",
            "example": "Monthly Revenue"
          },
          "file_name": {
            "type": [
              "string",
              "null"
            ]
          },
          "accountid": {
            "type": "string"
          },
          "raw_data": {
            "type": "array",
            "items": {
              "type": "array",
              "items": {}
            }
          },
          "columns": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CustomDataColumn"
            }
          },
          "row_count": {
            "type": "number"
          },
          "file_size": {
            "type": [
              "number",
              "null"
            ]
          },
          "created_at": {},
          "updated_at": {}
        },
        "required": [
          "id",
          "name",
          "accountid"
        ]
      },
      "CustomDataResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "$ref": "#/components/schemas/CustomData"
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateCustomDataResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string"
              }
            },
            "required": [
              "id"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateCustomDataRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "minLength": 1,
            "example": "Monthly Revenue"
          },
          "file_name": {
            "type": "string"
          },
          "raw_data": {
            "type": "array",
            "items": {
              "type": "array",
              "items": {}
            },
            "maxItems": 10000
          },
          "columns": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CustomDataColumn"
            }
          },
          "file_size": {
            "type": "number"
          }
        },
        "required": [
          "name",
          "file_name",
          "raw_data",
          "columns",
          "file_size"
        ]
      },
      "UpdateCustomDataRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "file_name": {
            "type": "string"
          },
          "raw_data": {
            "type": "array",
            "items": {
              "type": "array",
              "items": {}
            },
            "maxItems": 10000
          },
          "columns": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CustomDataColumn"
            }
          },
          "file_size": {
            "type": "number"
          }
        },
        "required": [
          "name",
          "file_name",
          "raw_data",
          "columns",
          "file_size"
        ]
      },
      "DuplicateCustomDataResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string"
              }
            },
            "required": [
              "id"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "DuplicateCustomDataRequest": {
        "type": "object",
        "properties": {
          "new_name": {
            "type": "string",
            "minLength": 1,
            "example": "Monthly Revenue (Copy)"
          }
        },
        "required": [
          "new_name"
        ]
      },
      "Plan": {
        "type": "object",
        "properties": {
          "price": {
            "type": "object",
            "additionalProperties": {}
          },
          "product": {
            "type": "object",
            "additionalProperties": {}
          }
        },
        "required": [
          "price",
          "product"
        ]
      },
      "ListPlansResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Plan"
            }
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "InvoicesResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "additionalProperties": {}
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "Auth": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "account_id": {
            "type": "string"
          },
          "integration": {
            "type": "string"
          },
          "name": {
            "type": [
              "string",
              "null"
            ]
          },
          "created_at": {
            "type": [
              "string",
              "null"
            ]
          }
        },
        "required": [
          "id",
          "account_id",
          "integration"
        ]
      },
      "ListAuthsResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Auth"
            }
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "RenameAuthRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "minLength": 1,
            "example": "My Google Account"
          }
        },
        "required": [
          "name"
        ]
      },
      "UpdateClientIntegrationRequest": {
        "type": "object",
        "properties": {
          "integrations": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            },
            "example": [
              {
                "integration": "google",
                "accountId": "12345"
              }
            ]
          }
        },
        "required": [
          "integrations"
        ]
      },
      "TestAuthResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "connected": {
                "type": "boolean"
              },
              "message": {
                "type": "string"
              }
            },
            "required": [
              "connected"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "TestAuthRequest": {
        "type": "object",
        "properties": {
          "auth_id": {
            "type": "string",
            "minLength": 1,
            "example": "auth_abc123"
          },
          "integration": {
            "type": "string",
            "minLength": 1,
            "example": "google"
          }
        },
        "required": [
          "auth_id",
          "integration"
        ]
      },
      "EmailSetup": {
        "type": [
          "object",
          "null"
        ],
        "properties": {
          "id": {
            "type": "string"
          },
          "account_id": {
            "type": "string"
          },
          "resend": {
            "type": [
              "object",
              "null"
            ],
            "additionalProperties": {}
          },
          "senders": {
            "type": [
              "array",
              "null"
            ],
            "items": {
              "type": "object",
              "additionalProperties": {}
            }
          },
          "smtp": {
            "type": [
              "object",
              "null"
            ],
            "additionalProperties": {}
          },
          "use_smtp": {
            "type": [
              "boolean",
              "null"
            ]
          },
          "default_subject": {
            "type": [
              "string",
              "null"
            ]
          },
          "default_from": {
            "type": [
              "string",
              "null"
            ]
          },
          "default_from_name": {
            "type": [
              "string",
              "null"
            ]
          },
          "default_message": {
            "type": [
              "string",
              "null"
            ]
          },
          "default_button_text": {
            "type": [
              "string",
              "null"
            ]
          },
          "button_top": {
            "type": [
              "boolean",
              "null"
            ]
          }
        },
        "required": [
          "account_id"
        ]
      },
      "EmailSetupResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "$ref": "#/components/schemas/EmailSetup"
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateSenderRequest": {
        "type": "object",
        "properties": {
          "from_name": {
            "type": "string",
            "minLength": 1,
            "example": "Acme Reports"
          },
          "email_address": {
            "type": "string",
            "format": "email",
            "example": "reports@acme.com"
          },
          "address": {
            "type": "string"
          },
          "city": {
            "type": "string"
          },
          "country": {
            "type": "string"
          }
        },
        "required": [
          "from_name",
          "email_address",
          "address",
          "city",
          "country"
        ]
      },
      "SmtpConfigRequest": {
        "type": "object",
        "properties": {
          "host": {
            "type": "string",
            "minLength": 1,
            "example": "smtp.example.com"
          },
          "port": {
            "type": "integer",
            "minimum": 1,
            "maximum": 65535,
            "example": 587
          },
          "username": {
            "type": "string",
            "minLength": 1,
            "example": "smtp_user"
          },
          "password": {
            "type": "string",
            "minLength": 1,
            "example": "secret"
          },
          "secure": {
            "type": "boolean"
          },
          "from_email": {
            "type": "string",
            "format": "email",
            "example": "noreply@example.com"
          },
          "from_name": {
            "type": "string",
            "example": "Acme Reports"
          }
        },
        "required": [
          "host",
          "port",
          "username",
          "password",
          "secure",
          "from_email",
          "from_name"
        ]
      },
      "TestSmtpRequest": {
        "type": "object",
        "properties": {
          "to": {
            "type": "string",
            "format": "email",
            "example": "user@example.com"
          }
        },
        "required": [
          "to"
        ]
      },
      "SendEmailResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string"
              }
            },
            "required": [
              "id"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "SendEmailRequest": {
        "type": "object",
        "properties": {
          "from": {
            "type": "string",
            "minLength": 1,
            "example": "reports@acme.com"
          },
          "to": {
            "anyOf": [
              {
                "type": "string",
                "format": "email"
              },
              {
                "type": "array",
                "items": {
                  "type": "string",
                  "format": "email"
                }
              }
            ],
            "example": "client@example.com"
          },
          "subject": {
            "type": "string",
            "minLength": 1,
            "example": "Your monthly report"
          },
          "html": {
            "type": "string",
            "minLength": 1,
            "example": "<p>Hello!</p>"
          }
        },
        "required": [
          "from",
          "to",
          "subject",
          "html"
        ]
      },
      "QueueEmailResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "queued": {
                "type": "number",
                "example": 3
              },
              "sent": {
                "type": "number",
                "example": 0
              },
              "method": {
                "type": "string",
                "enum": [
                  "sqs",
                  "direct"
                ],
                "example": "sqs"
              }
            },
            "required": [
              "queued",
              "sent",
              "method"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "QueueEmailItem": {
        "type": "object",
        "properties": {
          "to": {
            "type": "string",
            "format": "email",
            "example": "client@example.com"
          },
          "from": {
            "type": "string",
            "minLength": 1,
            "example": "reports@acme.com"
          },
          "subject": {
            "type": "string",
            "minLength": 1,
            "example": "Your monthly report"
          },
          "html": {
            "type": "string",
            "minLength": 1,
            "example": "<p>Hello!</p>"
          },
          "account_id": {
            "type": "string",
            "minLength": 1,
            "example": "account_123"
          }
        },
        "required": [
          "to",
          "from",
          "subject",
          "html",
          "account_id"
        ]
      },
      "QueueEmailRequest": {
        "type": "object",
        "properties": {
          "emails": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/QueueEmailItem"
            },
            "minItems": 1,
            "example": []
          }
        },
        "required": [
          "emails"
        ]
      },
      "MediaItem": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "account_id": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "url": {
            "type": "string"
          },
          "key": {
            "type": "string"
          },
          "mime_type": {
            "type": "string"
          },
          "size": {
            "type": "number"
          },
          "is_deleted": {
            "type": "boolean"
          },
          "deleted_at": {
            "type": [
              "string",
              "null"
            ]
          },
          "created_at": {}
        },
        "required": [
          "id",
          "account_id"
        ]
      },
      "ListMediaResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/MediaItem"
            }
          },
          "meta": {
            "type": "object",
            "properties": {
              "page": {
                "type": "number"
              },
              "limit": {
                "type": "number"
              },
              "total": {
                "type": "number"
              }
            },
            "required": [
              "page",
              "limit",
              "total"
            ]
          }
        },
        "required": [
          "success",
          "data",
          "meta"
        ]
      },
      "GroupMediaRequest": {
        "type": "object",
        "properties": {
          "ids": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "minItems": 1,
            "example": [
              "media1",
              "media2"
            ]
          },
          "folder_id": {
            "type": "string",
            "example": "folderAbc"
          }
        },
        "required": [
          "ids",
          "folder_id"
        ]
      },
      "UpdateMediaRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "minLength": 1,
            "example": "updated-logo.png"
          }
        },
        "required": [
          "name"
        ]
      },
      "MediaFolder": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "account_id": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "created_at": {}
        },
        "required": [
          "id",
          "account_id",
          "name"
        ]
      },
      "ListMediaFoldersResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/MediaFolder"
            }
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateMediaFolderResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string"
              }
            },
            "required": [
              "id"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateMediaFolderRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "minLength": 1,
            "example": "Client Logos"
          }
        },
        "required": [
          "name"
        ]
      },
      "RenameMediaFolderRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "minLength": 1,
            "example": "Brand Assets"
          }
        },
        "required": [
          "name"
        ]
      },
      "AssetTagsResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "Asset": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "account_id": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "type": {
            "type": "string"
          },
          "tags": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "datasources": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "ranking": {
            "type": [
              "number",
              "null"
            ]
          },
          "created_at": {}
        },
        "required": [
          "id",
          "account_id",
          "name"
        ]
      },
      "ListAssetsResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Asset"
            }
          },
          "meta": {
            "type": "object",
            "properties": {
              "page": {
                "type": "number"
              },
              "limit": {
                "type": "number"
              },
              "total": {
                "type": "number"
              }
            },
            "required": [
              "page",
              "limit",
              "total"
            ]
          }
        },
        "required": [
          "success",
          "data",
          "meta"
        ]
      },
      "CreateAssetResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string"
              }
            },
            "required": [
              "id"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateAssetRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "minLength": 1,
            "example": "GA4 Traffic Widget"
          },
          "description": {
            "type": "string"
          },
          "type": {
            "type": "string",
            "example": "chart"
          },
          "tags": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "datasources": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "name",
          "type"
        ]
      },
      "DuplicateAssetResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string"
              }
            },
            "required": [
              "id"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "DuplicateAssetRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "minLength": 1,
            "example": "GA4 Traffic Widget (copy)"
          },
          "description": {
            "type": "string"
          },
          "tags": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "name"
        ]
      },
      "ListAssetWidgetsResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Widget"
            }
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "GetAssetResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "$ref": "#/components/schemas/Asset"
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "UpdateAssetRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "type": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "tags": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "datasources": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "ranking": {
            "type": "number"
          }
        }
      },
      "GeneratePdfResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "job_id": {
                "type": "string",
                "example": "pdf_job_abc123"
              },
              "message": {
                "type": "string",
                "example": "PDF generation queued"
              }
            },
            "required": [
              "job_id",
              "message"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "GeneratePdfRequest": {
        "type": "object",
        "properties": {
          "project_id": {
            "type": "string",
            "minLength": 1,
            "example": "proj_abc123"
          },
          "client_id": {
            "type": "string",
            "minLength": 1,
            "example": "client_xyz"
          },
          "format": {
            "type": "string",
            "enum": [
              "A4",
              "Letter"
            ],
            "example": "A4"
          },
          "orientation": {
            "type": "string",
            "enum": [
              "portrait",
              "landscape"
            ],
            "example": "portrait"
          }
        },
        "required": [
          "project_id",
          "client_id",
          "format",
          "orientation"
        ]
      },
      "PdfStatusResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "job_id": {
                "type": "string"
              },
              "status": {
                "type": "string",
                "enum": [
                  "pending",
                  "processing",
                  "complete",
                  "failed"
                ]
              },
              "url": {
                "type": "string",
                "example": "https://s3.amazonaws.com/bucket/pdf/report.pdf"
              },
              "error": {
                "type": "string"
              }
            },
            "required": [
              "job_id",
              "status"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "Template": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "account_id": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "type": {
            "type": "string"
          },
          "ranking": {
            "type": "number"
          },
          "datasources": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "thumbnail": {
            "type": "string"
          },
          "date_text": {
            "type": "string"
          },
          "date_compare": {
            "type": "string"
          },
          "date_include_today": {
            "type": "boolean"
          },
          "date_current_start": {
            "type": "string"
          },
          "date_current_end": {
            "type": "string"
          },
          "date_previous_start": {
            "type": "string"
          },
          "date_previous_end": {
            "type": "string"
          },
          "date_custom_days": {
            "type": "number"
          },
          "date_custom_months": {
            "type": "number"
          },
          "created_at": {}
        },
        "required": [
          "id",
          "account_id",
          "name"
        ]
      },
      "ListTemplatesResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Template"
            }
          },
          "meta": {
            "type": "object",
            "properties": {
              "page": {
                "type": "number"
              },
              "limit": {
                "type": "number"
              },
              "total": {
                "type": "number"
              }
            },
            "required": [
              "page",
              "limit",
              "total"
            ]
          }
        },
        "required": [
          "success",
          "data",
          "meta"
        ]
      },
      "TemplateResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "$ref": "#/components/schemas/Template"
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateTemplateResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string"
              }
            },
            "required": [
              "id"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateTemplateRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "minLength": 1,
            "example": "Monthly SEO Report"
          },
          "project_id": {
            "type": "string",
            "description": "Copy pages/widgets from this project"
          },
          "type": {
            "type": "string",
            "description": "Defaults to the source project's type when omitted"
          },
          "description": {
            "type": "string"
          },
          "thumbnail": {
            "type": "string"
          },
          "ranking": {
            "type": "number"
          }
        },
        "required": [
          "name",
          "project_id"
        ]
      },
      "UpdateTemplateRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "thumbnail": {
            "type": "string"
          },
          "type": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "ranking": {
            "type": "number"
          }
        }
      },
      "Theme": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "account_id": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "primary_color": {
            "type": "string"
          },
          "chart_1": {
            "type": "string"
          },
          "chart_2": {
            "type": "string"
          },
          "chart_3": {
            "type": "string"
          },
          "chart_4": {
            "type": "string"
          },
          "chart_5": {
            "type": "string"
          },
          "chart_6": {
            "type": "string"
          },
          "chart_7": {
            "type": "string"
          },
          "chart_8": {
            "type": "string"
          },
          "chart_9": {
            "type": "string"
          },
          "chart_10": {
            "type": "string"
          },
          "font": {
            "type": "string"
          },
          "radius": {
            "type": "string"
          },
          "shadow": {
            "type": "string"
          },
          "created_at": {}
        },
        "required": [
          "id",
          "account_id",
          "name"
        ]
      },
      "ListThemesResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Theme"
            }
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "ThemeResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "$ref": "#/components/schemas/Theme"
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateThemeResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string"
              }
            },
            "required": [
              "id"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateThemeRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "minLength": 1,
            "example": "Dark Corporate"
          },
          "primary_color": {
            "type": "string"
          },
          "chart_1": {
            "type": "string"
          },
          "chart_2": {
            "type": "string"
          },
          "chart_3": {
            "type": "string"
          },
          "chart_4": {
            "type": "string"
          },
          "chart_5": {
            "type": "string"
          },
          "chart_6": {
            "type": "string"
          },
          "chart_7": {
            "type": "string"
          },
          "chart_8": {
            "type": "string"
          },
          "chart_9": {
            "type": "string"
          },
          "chart_10": {
            "type": "string"
          },
          "font": {
            "type": "string"
          },
          "radius": {
            "type": "string"
          },
          "shadow": {
            "type": "string",
            "enum": [
              "none",
              "sm",
              "md",
              "lg"
            ]
          }
        },
        "required": [
          "name",
          "primary_color"
        ]
      },
      "UpdateThemeRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "primary_color": {
            "type": "string"
          },
          "chart_1": {
            "type": "string"
          },
          "chart_2": {
            "type": "string"
          },
          "chart_3": {
            "type": "string"
          },
          "chart_4": {
            "type": "string"
          },
          "chart_5": {
            "type": "string"
          },
          "chart_6": {
            "type": "string"
          },
          "chart_7": {
            "type": "string"
          },
          "chart_8": {
            "type": "string"
          },
          "chart_9": {
            "type": "string"
          },
          "chart_10": {
            "type": "string"
          },
          "font": {
            "type": "string"
          },
          "radius": {
            "type": "string"
          },
          "shadow": {
            "type": "string",
            "enum": [
              "none",
              "sm",
              "md",
              "lg"
            ]
          }
        }
      },
      "Automation": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "parent_id": {
            "type": "string"
          },
          "frequency": {
            "type": "string"
          },
          "day": {
            "type": "string"
          },
          "hours": {
            "type": "string"
          },
          "minutes": {
            "type": "string"
          },
          "timezone": {
            "type": "string"
          },
          "recipients": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "subject": {
            "type": "string"
          },
          "sender_email": {
            "type": "string"
          },
          "sender_name": {
            "type": "string"
          },
          "message": {
            "type": "string"
          },
          "paused": {
            "type": "boolean"
          },
          "time_format": {
            "type": "string"
          },
          "date_text": {
            "type": "string"
          },
          "last_run_status": {
            "type": "string"
          },
          "last_run_at": {
            "type": [
              "string",
              "null"
            ]
          },
          "next_run_at": {
            "type": [
              "string",
              "null"
            ]
          },
          "is_deleted": {
            "type": "boolean"
          },
          "deleted_at": {
            "type": [
              "string",
              "null"
            ]
          },
          "created_at": {}
        },
        "required": [
          "id",
          "parent_id"
        ]
      },
      "ListAutomationsResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Automation"
            }
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "AutomationHistoryResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            }
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateAutomationResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "automation_id": {
                "type": "string"
              }
            },
            "required": [
              "automation_id"
            ]
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "CreateAutomationRequest": {
        "type": "object",
        "properties": {
          "parent_id": {
            "type": "string",
            "minLength": 1,
            "description": "Project ID this automation belongs to"
          },
          "name": {
            "type": "string"
          },
          "frequency": {
            "type": "string",
            "enum": [
              "daily",
              "weekly",
              "monthly"
            ],
            "example": "weekly"
          },
          "day": {
            "type": "string",
            "example": "monday"
          },
          "hours": {
            "type": "string",
            "example": "9"
          },
          "minutes": {
            "type": "string",
            "example": "00"
          },
          "timezone": {
            "type": "string",
            "example": "America/New_York"
          },
          "time_format": {
            "type": "string"
          },
          "recipients": {
            "type": "array",
            "items": {
              "type": "string",
              "format": "email"
            },
            "minItems": 1
          },
          "subject": {
            "type": "string",
            "minLength": 1
          },
          "sender_email": {
            "type": "string"
          },
          "sender_name": {
            "type": "string"
          },
          "message": {
            "type": "string"
          },
          "date_text": {
            "type": "string"
          }
        },
        "required": [
          "parent_id",
          "name",
          "frequency",
          "hours",
          "minutes",
          "timezone",
          "time_format",
          "recipients",
          "subject",
          "sender_email",
          "sender_name",
          "message",
          "date_text"
        ]
      },
      "UpdateAutomationRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "frequency": {
            "type": "string",
            "enum": [
              "daily",
              "weekly",
              "monthly"
            ]
          },
          "hours": {
            "type": "string"
          },
          "minutes": {
            "type": "string"
          },
          "timezone": {
            "type": "string"
          },
          "time_format": {
            "type": "string"
          },
          "recipients": {
            "type": "array",
            "items": {
              "type": "string",
              "format": "email"
            }
          },
          "subject": {
            "type": "string"
          },
          "sender_email": {
            "type": "string"
          },
          "sender_name": {
            "type": "string"
          },
          "message": {
            "type": "string"
          },
          "date_text": {
            "type": "string"
          },
          "day": {
            "type": "string"
          }
        }
      },
      "TestAutomationResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "enum": [
              true
            ]
          },
          "data": {
            "type": "object",
            "additionalProperties": {}
          }
        },
        "required": [
          "success",
          "data"
        ]
      },
      "TestAutomationRequest": {
        "type": "object",
        "properties": {
          "recipients": {
            "type": "array",
            "items": {
              "type": "string",
              "format": "email"
            },
            "minItems": 1,
            "example": [
              "test@example.com"
            ]
          }
        },
        "required": [
          "recipients"
        ]
      },
      "ArchiveBulkBody": {
        "type": "object",
        "properties": {
          "ids": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "minItems": 1
          },
          "type": {
            "type": "string",
            "enum": [
              "clients",
              "projects",
              "media",
              "automations"
            ]
          }
        },
        "required": [
          "ids",
          "type"
        ]
      }
    },
    "parameters": {}
  },
  "paths": {
    "/v1/health": {
      "get": {
        "tags": [
          "Health"
        ],
        "summary": "Health Check",
        "security": [],
        "responses": {
          "200": {
            "description": "Service is healthy or degraded",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "status": {
                      "type": "string",
                      "enum": [
                        "healthy",
                        "degraded",
                        "unhealthy"
                      ]
                    },
                    "timestamp": {
                      "type": "string"
                    },
                    "uptime": {
                      "type": "number"
                    },
                    "version": {
                      "type": "string"
                    },
                    "checks": {
                      "type": "object",
                      "properties": {
                        "supabase": {
                          "type": "boolean"
                        }
                      },
                      "required": [
                        "supabase"
                      ]
                    }
                  },
                  "required": [
                    "status",
                    "timestamp",
                    "uptime",
                    "version",
                    "checks"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/users/me": {
      "get": {
        "tags": [
          "Users"
        ],
        "summary": "Get User",
        "description": "Get the currently authenticated user profile.",
        "responses": {
          "200": {
            "description": "Current user profile",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MeResponse"
                }
              }
            }
          },
          "404": {
            "description": "User not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/users/me/profile": {
      "put": {
        "tags": [
          "Users"
        ],
        "summary": "Update Profile",
        "description": "Update the current user profile name, language, and theme.",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UpdateProfileRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Profile updated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/users/me/avatar": {
      "put": {
        "tags": [
          "Users"
        ],
        "summary": "Update Avatar",
        "description": "Update the current user profile picture.",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UpdateAvatarRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Avatar updated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/users/me/email": {
      "put": {
        "tags": [
          "Users"
        ],
        "summary": "Change Email",
        "description": "Change the current user email address.",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ChangeEmailRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Email address updated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "409": {
            "description": "Email already in use",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/users": {
      "get": {
        "tags": [
          "Users"
        ],
        "summary": "List Users",
        "description": "List all team members for the authenticated account.",
        "parameters": [
          {
            "schema": {
              "type": [
                "integer",
                "null"
              ],
              "minimum": 0,
              "default": 0,
              "example": 0
            },
            "required": false,
            "name": "page",
            "in": "query"
          },
          {
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100,
              "default": 20,
              "example": 20
            },
            "required": false,
            "name": "limit",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "Paginated list of team members",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListUsersResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/users/invite": {
      "post": {
        "tags": [
          "Users"
        ],
        "summary": "Invite User",
        "description": "Invite a new user to the account.",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/InviteUserRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "User invited",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/InviteUserResponse"
                }
              }
            }
          },
          "409": {
            "description": "User already exists",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/users/:id": {
      "put": {
        "tags": [
          "Users"
        ],
        "summary": "Update User",
        "description": "Edit a team member (role, allowed projects, name).",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/EditUserRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "User updated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "403": {
            "description": "Cannot edit a user from a different account",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          },
          "404": {
            "description": "User not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "Users"
        ],
        "summary": "Delete User",
        "description": "Remove a team member from the account.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "User removed",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "403": {
            "description": "Cannot remove owner or user from a different account",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          },
          "404": {
            "description": "User not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/account": {
      "get": {
        "tags": [
          "Account"
        ],
        "summary": "Get Account",
        "description": "Get the accounts row for the current account",
        "responses": {
          "200": {
            "description": "Account document",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/AccountResponse"
                }
              }
            }
          },
          "404": {
            "description": "Account not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "Account"
        ],
        "summary": "Delete Account",
        "description": "Irreversible. Cancels the active Stripe subscription, deletes all data across every table for this account, removes all team members from the users table, purges all S3 media files, and deletes all Supabase Auth users. Requires the account owner's current password as a confirmation gate.",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/DeleteAccountRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Account deleted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DeleteAccountResponse"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized or wrong password",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          },
          "404": {
            "description": "Account or user not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/account/usage": {
      "get": {
        "tags": [
          "Account"
        ],
        "summary": "Get Account Usage",
        "description": "Get account usage statistics vs plan limits",
        "responses": {
          "200": {
            "description": "Usage data",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/AccountUsageResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/company": {
      "get": {
        "tags": [
          "Company"
        ],
        "summary": "Get Company",
        "description": "Get company settings for the current account",
        "responses": {
          "200": {
            "description": "Company settings document",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CompanyResponse"
                }
              }
            }
          },
          "404": {
            "description": "Company settings not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "put": {
        "tags": [
          "Company"
        ],
        "summary": "Update Company",
        "description": "Update company settings",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UpdateCompanyRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Company settings updated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/white-label/domains": {
      "get": {
        "tags": [
          "White Label"
        ],
        "summary": "List Domains",
        "description": "List custom domains for the current account.",
        "responses": {
          "200": {
            "description": "Domain list",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DomainsListResponse"
                }
              }
            }
          }
        }
      },
      "post": {
        "tags": [
          "White Label"
        ],
        "summary": "Add Domain",
        "description": "Add a custom domain. Detects the DNS provider and registers the domain on Vercel.",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/AddDomainRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Domain added",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DomainResponse"
                }
              }
            }
          },
          "409": {
            "description": "Domain already exists",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/white-label/domains/:domain_id": {
      "delete": {
        "tags": [
          "White Label"
        ],
        "summary": "Delete Domain",
        "description": "Remove a custom domain.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "domain_id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Domain removed",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/WhiteLabelSuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Domain not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/white-label/domains/:domain_id/status": {
      "get": {
        "tags": [
          "White Label"
        ],
        "summary": "Check Domain Status",
        "description": "Check domain verification status via Vercel.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "domain_id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Domain status",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DomainResponse"
                }
              }
            }
          },
          "404": {
            "description": "Domain not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/branding": {
      "get": {
        "tags": [
          "Branding"
        ],
        "summary": "Get Branding",
        "description": "Get branding settings",
        "responses": {
          "200": {
            "description": "Branding data",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean",
                      "enum": [
                        true
                      ]
                    },
                    "data": {
                      "type": "object",
                      "additionalProperties": {}
                    }
                  },
                  "required": [
                    "success",
                    "data"
                  ]
                }
              }
            }
          }
        }
      },
      "put": {
        "tags": [
          "Branding"
        ],
        "summary": "Update Branding",
        "description": "Update branding settings",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UpdateBrandingRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Updated",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean",
                      "enum": [
                        true
                      ]
                    }
                  },
                  "required": [
                    "success"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/clients": {
      "get": {
        "tags": [
          "Clients"
        ],
        "summary": "List Clients",
        "description": "List clients for the current account",
        "parameters": [
          {
            "schema": {
              "type": [
                "integer",
                "null"
              ],
              "minimum": 0,
              "default": 0,
              "example": 0
            },
            "required": false,
            "name": "page",
            "in": "query"
          },
          {
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100,
              "default": 20,
              "example": 20
            },
            "required": false,
            "name": "limit",
            "in": "query"
          },
          {
            "schema": {
              "type": "string",
              "example": "acme"
            },
            "required": false,
            "name": "search",
            "in": "query"
          },
          {
            "schema": {
              "type": "string",
              "example": "folderXyz"
            },
            "required": false,
            "name": "folder_id",
            "in": "query"
          },
          {
            "schema": {
              "type": "string",
              "default": "updated_at",
              "example": "updated_at"
            },
            "required": false,
            "name": "sort_by",
            "in": "query"
          },
          {
            "schema": {
              "type": "string",
              "enum": [
                "asc",
                "desc"
              ],
              "default": "desc",
              "example": "desc"
            },
            "required": false,
            "name": "order",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "Paginated client list",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListClientsResponse"
                }
              }
            }
          }
        }
      },
      "post": {
        "tags": [
          "Clients"
        ],
        "summary": "Create Client",
        "description": "Create a new client",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateClientRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Client created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateClientResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/clients/count": {
      "get": {
        "tags": [
          "Clients"
        ],
        "summary": "Count Clients",
        "description": "Count total clients for the current account",
        "responses": {
          "200": {
            "description": "Client count",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ClientCountResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/clients/all": {
      "get": {
        "tags": [
          "Clients"
        ],
        "summary": "List All Clients",
        "description": "List all clients with optional field selection",
        "parameters": [
          {
            "schema": {
              "type": "string",
              "example": "id,name,client_integrations"
            },
            "required": false,
            "name": "fields",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "All clients",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean",
                      "enum": [
                        true
                      ]
                    },
                    "data": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "additionalProperties": {}
                      }
                    }
                  },
                  "required": [
                    "success",
                    "data"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/clients/bulk": {
      "delete": {
        "tags": [
          "Clients"
        ],
        "summary": "Bulk Delete Clients",
        "description": "Delete multiple clients by ID",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/BulkDeleteClientsRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Clients deleted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/clients/:id": {
      "get": {
        "tags": [
          "Clients"
        ],
        "summary": "Get Client",
        "description": "Get a single client by ID",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Client document",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ClientResponse"
                }
              }
            }
          },
          "404": {
            "description": "Client not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "put": {
        "tags": [
          "Clients"
        ],
        "summary": "Update Client",
        "description": "Update a client",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UpdateClientRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Client updated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Client not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "Clients"
        ],
        "summary": "Delete Client",
        "description": "Delete a client and all its associated projects and widgets",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Client deleted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Client not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/clients/:id/screenshot/refresh": {
      "post": {
        "tags": [
          "Clients"
        ],
        "summary": "Refresh Screenshot",
        "description": "Re-fetches the screenshot synchronously using the client's stored website and returns the new URL. Use this for user-triggered refresh on the dashboard card.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Screenshot refreshed",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RefreshScreenshotResponse"
                }
              }
            }
          },
          "400": {
            "description": "Client has no website configured",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          },
          "404": {
            "description": "Client not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/clients/:id/folder": {
      "put": {
        "tags": [
          "Clients"
        ],
        "summary": "Move Client Folder",
        "description": "Move a client to one or more folders",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/MoveClientToFolderRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Client folder updated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Client not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/clients/:id/integrations": {
      "get": {
        "tags": [
          "Clients"
        ],
        "summary": "List Client Integrations",
        "description": "List integrations connected to a client",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Client integrations list",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean",
                      "enum": [
                        true
                      ]
                    },
                    "data": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "success",
                    "data"
                  ]
                }
              }
            }
          },
          "404": {
            "description": "Client not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/folders/clients": {
      "get": {
        "tags": [
          "Folders"
        ],
        "summary": "List Folders",
        "description": "List all client folders for the current account",
        "responses": {
          "200": {
            "description": "Client folder list",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListFoldersResponse"
                }
              }
            }
          }
        }
      },
      "post": {
        "tags": [
          "Folders"
        ],
        "summary": "Create Folder",
        "description": "Create a new client folder",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateFolderRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Folder created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateFolderResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/folders/clients/{id}": {
      "put": {
        "tags": [
          "Folders"
        ],
        "summary": "Update Folder",
        "description": "Rename a client folder",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UpdateFolderRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Folder renamed",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Folder not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "Folders"
        ],
        "summary": "Delete Folder",
        "description": "Delete a client folder and unassign all clients from it",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Folder deleted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Folder not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/projects": {
      "get": {
        "tags": [
          "Projects"
        ],
        "summary": "List Projects",
        "description": "List projects for the current account (optionally filtered by client).",
        "parameters": [
          {
            "schema": {
              "type": "string",
              "example": "cliAbc123"
            },
            "required": false,
            "name": "client_id",
            "in": "query"
          },
          {
            "schema": {
              "type": "string",
              "example": "AGENCY"
            },
            "required": false,
            "name": "template",
            "in": "query"
          },
          {
            "schema": {
              "type": [
                "integer",
                "null"
              ],
              "minimum": 0,
              "default": 0,
              "example": 0
            },
            "required": false,
            "name": "page",
            "in": "query"
          },
          {
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 200,
              "default": 50,
              "example": 50
            },
            "required": false,
            "name": "limit",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "Paginated project list",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListProjectsResponse"
                }
              }
            }
          }
        }
      },
      "post": {
        "tags": [
          "Projects"
        ],
        "summary": "Create Project",
        "description": "Create a new project.",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateProjectRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Project created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateProjectResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/projects/all": {
      "get": {
        "tags": [
          "Projects"
        ],
        "summary": "List All Projects",
        "description": "List all projects (id + name only) for dropdown selectors.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": false,
            "name": "client_id",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "All projects",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean",
                      "enum": [
                        true
                      ]
                    },
                    "data": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string"
                          },
                          "name": {
                            "type": "string"
                          }
                        },
                        "required": [
                          "id",
                          "name"
                        ]
                      }
                    }
                  },
                  "required": [
                    "success",
                    "data"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/projects/bulk": {
      "delete": {
        "tags": [
          "Projects"
        ],
        "summary": "Bulk Delete Projects",
        "description": "Delete multiple projects by ID.",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/BulkDeleteProjectsRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Projects deleted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "403": {
            "description": "One or more projects do not belong to this account",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/projects/{id}": {
      "get": {
        "tags": [
          "Projects"
        ],
        "summary": "Get Project",
        "description": "Get a single project by ID.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Project document",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ProjectResponse"
                }
              }
            }
          },
          "404": {
            "description": "Project not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "put": {
        "tags": [
          "Projects"
        ],
        "summary": "Update Project",
        "description": "Update a project.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UpdateProjectRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Project updated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Project not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "Projects"
        ],
        "summary": "Delete Project",
        "description": "Delete a project and all its widgets.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Project deleted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Project not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/projects/{id}/duplicate": {
      "post": {
        "tags": [
          "Projects"
        ],
        "summary": "Duplicate Project",
        "description": "Duplicate a project — deep copy of pages, widgets, and settings.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/DuplicateProjectRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Duplicate project created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateProjectResponse"
                }
              }
            }
          },
          "404": {
            "description": "Source project not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/projects/{id}/pdf": {
      "delete": {
        "tags": [
          "Projects"
        ],
        "summary": "Delete PDF Notification",
        "description": "Remove a PDF notification entry from a project.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "notification_id": {
                    "type": "string",
                    "example": "notif123"
                  }
                },
                "required": [
                  "notification_id"
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "PDF notification removed",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Project not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/pages": {
      "get": {
        "tags": [
          "Pages"
        ],
        "summary": "List Pages",
        "description": "List pages for a project or template.",
        "parameters": [
          {
            "schema": {
              "type": "string",
              "example": "proj123"
            },
            "required": true,
            "name": "source_id",
            "in": "query"
          },
          {
            "schema": {
              "type": "string",
              "enum": [
                "project",
                "template"
              ],
              "example": "project"
            },
            "required": false,
            "name": "source_type",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "Pages list",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListPagesResponse"
                }
              }
            }
          },
          "404": {
            "description": "Source not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "post": {
        "tags": [
          "Pages"
        ],
        "summary": "Create Page",
        "description": "Create a page on a project or template.",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreatePageRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Page created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreatePageResponse"
                }
              }
            }
          },
          "404": {
            "description": "Source not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/pages/{page_id}": {
      "put": {
        "tags": [
          "Pages"
        ],
        "summary": "Update Page",
        "description": "Update a page.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "page_id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UpdatePageRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Page updated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Page not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "Pages"
        ],
        "summary": "Delete Page",
        "description": "Delete a page.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "page_id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Page deleted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Page not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/search": {
      "get": {
        "tags": [
          "Search"
        ],
        "summary": "Search",
        "description": "Search clients and projects by name (powers the command palette).",
        "parameters": [
          {
            "schema": {
              "type": "string",
              "minLength": 1,
              "example": "acme"
            },
            "required": true,
            "name": "q",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "Search results across clients and projects",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SearchResponse"
                }
              }
            }
          },
          "400": {
            "description": "Query too short",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/widgets/ids": {
      "get": {
        "tags": [
          "Widgets"
        ],
        "summary": "List Widget IDs",
        "description": "Get widget IDs for a source.",
        "parameters": [
          {
            "schema": {
              "type": "string",
              "example": "proj123"
            },
            "required": true,
            "name": "source_id",
            "in": "query"
          },
          {
            "schema": {
              "type": "string",
              "example": "page123"
            },
            "required": false,
            "name": "page_id",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "Array of widget IDs",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListWidgetIDsResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/widgets": {
      "get": {
        "tags": [
          "Widgets"
        ],
        "summary": "List Widgets",
        "description": "List widgets for a source.",
        "parameters": [
          {
            "schema": {
              "type": "string",
              "example": "project"
            },
            "required": false,
            "name": "source_type",
            "in": "query"
          },
          {
            "schema": {
              "type": "string",
              "example": "proj123"
            },
            "required": true,
            "name": "source_id",
            "in": "query"
          },
          {
            "schema": {
              "type": "string",
              "example": "page123"
            },
            "required": false,
            "name": "page_id",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "Widget list",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListWidgetsResponse"
                }
              }
            }
          }
        }
      },
      "post": {
        "tags": [
          "Widgets"
        ],
        "summary": "Create Widgets",
        "description": "Batch create widgets via upsert.",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateWidgetsRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Widgets created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateWidgetsResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/widgets/{id}": {
      "get": {
        "tags": [
          "Widgets"
        ],
        "summary": "Get Widget",
        "description": "Get a single widget by ID.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Widget",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/WidgetResponse"
                }
              }
            }
          },
          "404": {
            "description": "Not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "put": {
        "tags": [
          "Widgets"
        ],
        "summary": "Update Widget",
        "description": "Update a single widget (partial update).",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UpdateWidgetRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Updated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "Widgets"
        ],
        "summary": "Delete Widget",
        "description": "Delete a single widget by ID.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Widget deleted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/widgets/bulk": {
      "delete": {
        "tags": [
          "Widgets"
        ],
        "summary": "Bulk Delete Widgets",
        "description": "Delete multiple widgets by ID.",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/BulkDeleteWidgetsRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Widgets deleted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/data/query": {
      "post": {
        "tags": [
          "Data"
        ],
        "summary": "Query Data",
        "description": "Proxy an integration data query to api.oviond.com",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/DataQueryRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Query result from upstream API",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DataProxyResponse"
                }
              }
            }
          },
          "502": {
            "description": "Upstream API error",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/data/test": {
      "post": {
        "tags": [
          "Data"
        ],
        "summary": "Test Connection",
        "description": "Proxy an integration connection test to api.oviond.com",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/DataTestRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Test result from upstream API",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DataProxyResponse"
                }
              }
            }
          },
          "502": {
            "description": "Upstream API error",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/data/accounts": {
      "post": {
        "tags": [
          "Data"
        ],
        "summary": "List Integration Accounts",
        "description": "Proxy an integration accounts listing to api.oviond.com",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/DataAccountsRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Accounts from upstream API",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DataProxyResponse"
                }
              }
            }
          },
          "502": {
            "description": "Upstream API error",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/data/resource": {
      "post": {
        "tags": [
          "Data"
        ],
        "summary": "Fetch Resource Data",
        "description": "Proxy a resource data fetch (campaigns, videos, etc.) to api.oviond.com",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/DataResourceRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Resource data from upstream API",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DataProxyResponse"
                }
              }
            }
          },
          "502": {
            "description": "Upstream API error",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/calculated-metrics": {
      "get": {
        "tags": [
          "Calculated Metrics"
        ],
        "summary": "List Calculated Metrics",
        "description": "List all calculated metrics for the current account",
        "responses": {
          "200": {
            "description": "Calculated metrics list",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListCalculatedMetricsResponse"
                }
              }
            }
          }
        }
      },
      "post": {
        "tags": [
          "Calculated Metrics"
        ],
        "summary": "Create Calculated Metric",
        "description": "Create a new calculated metric",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateCalculatedMetricRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Metric created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateCalculatedMetricResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/calculated-metrics/{id}": {
      "put": {
        "tags": [
          "Calculated Metrics"
        ],
        "summary": "Update Calculated Metric",
        "description": "Update a calculated metric",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UpdateCalculatedMetricRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Metric updated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Metric not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "Calculated Metrics"
        ],
        "summary": "Delete Calculated Metric",
        "description": "Delete a calculated metric",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Metric deleted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Metric not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/calculated-metrics/{id}/duplicate": {
      "post": {
        "tags": [
          "Calculated Metrics"
        ],
        "summary": "Duplicate Calculated Metric",
        "description": "Duplicate a calculated metric",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/DuplicateCalculatedMetricRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Duplicate metric created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateCalculatedMetricResponse"
                }
              }
            }
          },
          "404": {
            "description": "Source metric not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/saved-metrics": {
      "get": {
        "tags": [
          "Saved Metrics"
        ],
        "summary": "List Saved Metrics",
        "description": "List all saved metrics for the current account.",
        "responses": {
          "200": {
            "description": "Saved metrics list",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListSavedMetricsResponse"
                }
              }
            }
          }
        }
      },
      "post": {
        "tags": [
          "Saved Metrics"
        ],
        "summary": "Create Saved Metric",
        "description": "Create a new saved metric.",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateSavedMetricRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Saved metric created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateSavedMetricResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/saved-metrics/{id}": {
      "put": {
        "tags": [
          "Saved Metrics"
        ],
        "summary": "Update Saved Metric",
        "description": "Update a saved metric.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UpdateSavedMetricRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Saved metric updated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Saved metric not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "Saved Metrics"
        ],
        "summary": "Delete Saved Metric",
        "description": "Delete a saved metric.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Saved metric deleted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Saved metric not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/saved-metrics/{id}/duplicate": {
      "post": {
        "tags": [
          "Saved Metrics"
        ],
        "summary": "Duplicate Saved Metric",
        "description": "Clone a saved metric.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/DuplicateSavedMetricRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Duplicate saved metric created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateSavedMetricResponse"
                }
              }
            }
          },
          "404": {
            "description": "Source saved metric not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/custom-data": {
      "get": {
        "tags": [
          "Custom Data"
        ],
        "summary": "List Custom Data",
        "description": "List custom datasets for the current account (no raw_data)",
        "responses": {
          "200": {
            "description": "Custom data list",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListCustomDataResponse"
                }
              }
            }
          }
        }
      },
      "post": {
        "tags": [
          "Custom Data"
        ],
        "summary": "Create Custom Data",
        "description": "Create a new custom dataset (max 10,000 rows)",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateCustomDataRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Dataset created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateCustomDataResponse"
                }
              }
            }
          },
          "400": {
            "description": "Validation error (e.g. row limit exceeded)",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/custom-data/{id}": {
      "get": {
        "tags": [
          "Custom Data"
        ],
        "summary": "Get Custom Data",
        "description": "Get a single custom dataset by ID (includes raw_data)",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Full custom data document",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CustomDataResponse"
                }
              }
            }
          },
          "404": {
            "description": "Custom dataset not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "put": {
        "tags": [
          "Custom Data"
        ],
        "summary": "Update Custom Data",
        "description": "Update a custom dataset",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UpdateCustomDataRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Dataset updated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "400": {
            "description": "Validation error",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          },
          "404": {
            "description": "Custom dataset not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "Custom Data"
        ],
        "summary": "Delete Custom Data",
        "description": "Delete a custom dataset",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Dataset deleted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Custom dataset not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/custom-data/{id}/duplicate": {
      "post": {
        "tags": [
          "Custom Data"
        ],
        "summary": "Duplicate Custom Data",
        "description": "Duplicate a custom dataset",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/DuplicateCustomDataRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Duplicate dataset created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DuplicateCustomDataResponse"
                }
              }
            }
          },
          "404": {
            "description": "Source dataset not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/billing/plans": {
      "get": {
        "tags": [
          "Billing"
        ],
        "summary": "List Plans",
        "description": "List available subscription plans from Stripe",
        "responses": {
          "200": {
            "description": "Plan list",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListPlansResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/billing/invoices": {
      "get": {
        "tags": [
          "Billing"
        ],
        "summary": "List Invoices",
        "description": "List Stripe invoices for a customer",
        "responses": {
          "200": {
            "description": "Invoice list",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/InvoicesResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/integrations/auths": {
      "get": {
        "tags": [
          "Integrations"
        ],
        "summary": "List Integrations",
        "description": "List all OAuth integrations stored for the current account",
        "responses": {
          "200": {
            "description": "Auth list",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListAuthsResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/integrations/auths/:id/name": {
      "put": {
        "tags": [
          "Integrations"
        ],
        "summary": "Rename Integration",
        "description": "Rename an integration auth entry",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/RenameAuthRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Auth renamed",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Auth not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/integrations/auths/:id": {
      "delete": {
        "tags": [
          "Integrations"
        ],
        "summary": "Delete Integration",
        "description": "Delete an integration auth entry",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Auth deleted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Auth not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/integrations/:client_id": {
      "put": {
        "tags": [
          "Integrations"
        ],
        "summary": "Update Client Integrations",
        "description": "Replace the integration rows for a client in client_integrations",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "client_id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UpdateClientIntegrationRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Integration config updated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Client not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/integrations/:client_id/link": {
      "post": {
        "tags": [
          "Integrations"
        ],
        "summary": "Link Datasource",
        "description": "Link a datasource to a client",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "client_id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "integration_id": {
                    "type": "string"
                  },
                  "account_name": {
                    "type": "string"
                  },
                  "profile": {}
                },
                "required": [
                  "integration_id",
                  "account_name"
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Datasource linked",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Client not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/integrations/:client_id/unlink": {
      "post": {
        "tags": [
          "Integrations"
        ],
        "summary": "Unlink Datasource",
        "description": "Unlink a datasource from a client",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "client_id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "integration_id": {
                    "type": "string"
                  }
                },
                "required": [
                  "integration_id"
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Datasource unlinked",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/integrations/test": {
      "post": {
        "tags": [
          "Integrations"
        ],
        "summary": "Test Auth Connection",
        "description": "Test whether a stored auth connection is valid",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/TestAuthRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Connection test result",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/TestAuthResponse"
                }
              }
            }
          },
          "404": {
            "description": "Auth not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/integrations/profiles": {
      "get": {
        "tags": [
          "Integrations"
        ],
        "summary": "List All Profiles",
        "description": "List all auth profiles for every integration",
        "responses": {
          "200": {
            "description": "Profiles grouped by integration ID",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean",
                      "enum": [
                        true
                      ]
                    },
                    "data": {
                      "type": "object",
                      "additionalProperties": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "additionalProperties": {}
                        }
                      }
                    }
                  },
                  "required": [
                    "success",
                    "data"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/integrations/:integrationID/profiles": {
      "get": {
        "tags": [
          "Integrations"
        ],
        "summary": "List Integration Profiles",
        "description": "List auth profiles for a specific integration",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "integrationID",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Profile list",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean",
                      "enum": [
                        true
                      ]
                    },
                    "data": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "additionalProperties": {}
                      }
                    }
                  },
                  "required": [
                    "success",
                    "data"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/integrations/:integrationID/profiles/:profileName/rename": {
      "put": {
        "tags": [
          "Integrations"
        ],
        "summary": "Rename Profile",
        "description": "Rename an auth connection",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "integrationID",
            "in": "path"
          },
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "profileName",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "new_name": {
                    "type": "string"
                  }
                },
                "required": [
                  "new_name"
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Profile renamed",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Profile not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/integrations/:integrationID/profiles/:profileName": {
      "delete": {
        "tags": [
          "Integrations"
        ],
        "summary": "Delete Profile",
        "description": "Delete an auth connection",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "integrationID",
            "in": "path"
          },
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "profileName",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Profile deleted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/email/setup": {
      "get": {
        "tags": [
          "Email"
        ],
        "summary": "Get Email Setup",
        "description": "Get email setup configuration for the current account",
        "responses": {
          "200": {
            "description": "Email setup document",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/EmailSetupResponse"
                }
              }
            }
          }
        }
      },
      "put": {
        "tags": [
          "Email"
        ],
        "summary": "Update Email Setup",
        "description": "Update email setup configuration",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "additionalProperties": {}
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Email setup updated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          }
        }
      },
      "post": {
        "tags": [
          "Email"
        ],
        "summary": "Add Email Sender",
        "description": "Add a sender to the email setup configuration",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateSenderRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Sender added",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/email/smtp": {
      "put": {
        "tags": [
          "Email"
        ],
        "summary": "Update SMTP Config",
        "description": "Store SMTP configuration for the account",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/SmtpConfigRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "SMTP config saved",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "Email"
        ],
        "summary": "Delete SMTP Config",
        "description": "Remove SMTP configuration from the account",
        "responses": {
          "200": {
            "description": "SMTP config removed",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/email/smtp/test": {
      "post": {
        "tags": [
          "Email"
        ],
        "summary": "Test SMTP",
        "description": "Send a test email using the account SMTP configuration",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/TestSmtpRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Test email sent",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "422": {
            "description": "SMTP not configured",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/email/send": {
      "post": {
        "tags": [
          "Email"
        ],
        "summary": "Send Email",
        "description": "Send a transactional email via Resend",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/SendEmailRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Email sent",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SendEmailResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/email/domains": {
      "post": {
        "tags": [
          "Email"
        ],
        "summary": "Add Email Domain",
        "description": "Add and register a sending domain with Resend",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/AddDomainRequest"
                  },
                  {
                    "properties": {
                      "domain": {
                        "type": "string",
                        "minLength": 1,
                        "example": "mail.acme.com"
                      }
                    }
                  }
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Domain registered",
            "content": {
              "application/json": {
                "schema": {
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/DomainResponse"
                    },
                    {
                      "properties": {
                        "success": {
                          "type": "boolean",
                          "enum": [
                            true
                          ]
                        },
                        "data": {
                          "type": "object",
                          "additionalProperties": {}
                        }
                      }
                    }
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/email/domains/:id": {
      "delete": {
        "tags": [
          "Email"
        ],
        "summary": "Delete Email Domain",
        "description": "Remove a sending domain from Resend and the account config",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Domain removed",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/email/domains/:id/verify": {
      "post": {
        "tags": [
          "Email"
        ],
        "summary": "Verify Email Domain",
        "description": "Trigger domain DNS verification check with Resend",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Verification triggered; updated domain status returned",
            "content": {
              "application/json": {
                "schema": {
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/DomainResponse"
                    },
                    {
                      "properties": {
                        "success": {
                          "type": "boolean",
                          "enum": [
                            true
                          ]
                        },
                        "data": {
                          "type": "object",
                          "additionalProperties": {}
                        }
                      }
                    }
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/email/queue": {
      "post": {
        "tags": [
          "Email"
        ],
        "summary": "Queue Emails",
        "description": "Enqueue a batch of emails to SQS for async delivery, falling back to direct Resend when SQS is not configured",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/QueueEmailRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Emails queued or sent",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/QueueEmailResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/email/logs": {
      "get": {
        "tags": [
          "Email"
        ],
        "summary": "List Email Logs",
        "description": "Get email logs",
        "parameters": [
          {
            "schema": {
              "type": [
                "number",
                "null"
              ],
              "default": 1
            },
            "required": false,
            "name": "page",
            "in": "query"
          },
          {
            "schema": {
              "type": [
                "number",
                "null"
              ],
              "default": 20
            },
            "required": false,
            "name": "limit",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "Email logs",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean"
                    },
                    "data": {
                      "type": "array",
                      "items": {}
                    },
                    "meta": {}
                  },
                  "required": [
                    "success",
                    "data"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/media": {
      "get": {
        "tags": [
          "Media"
        ],
        "summary": "List Media",
        "description": "List media assets for the current account (paginated)",
        "parameters": [
          {
            "schema": {
              "type": [
                "integer",
                "null"
              ],
              "minimum": 0,
              "default": 0,
              "example": 0
            },
            "required": false,
            "name": "page",
            "in": "query"
          },
          {
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100,
              "default": 20,
              "example": 20
            },
            "required": false,
            "name": "limit",
            "in": "query"
          },
          {
            "schema": {
              "type": "string",
              "example": "logo"
            },
            "required": false,
            "name": "search",
            "in": "query"
          },
          {
            "schema": {
              "type": "string",
              "example": "folderAbc"
            },
            "required": false,
            "name": "folder_id",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "Media list",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListMediaResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/media/group": {
      "put": {
        "tags": [
          "Media"
        ],
        "summary": "Group Media",
        "description": "Move multiple media items to a folder",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/GroupMediaRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Media grouped",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/media/:id": {
      "put": {
        "tags": [
          "Media"
        ],
        "summary": "Update Media",
        "description": "Update media metadata (e.g. rename).",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UpdateMediaRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Media updated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Media not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "Media"
        ],
        "summary": "Delete Media",
        "description": "Soft-delete a media item. The underlying file is retained in S3 for potential restore.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Media deleted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Media not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/media/bulk": {
      "delete": {
        "tags": [
          "Media"
        ],
        "summary": "Bulk Delete Media",
        "description": "Soft-delete multiple media items.",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "ids": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "minItems": 1
                  }
                },
                "required": [
                  "ids"
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Media deleted",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean",
                      "enum": [
                        true
                      ]
                    }
                  },
                  "required": [
                    "success"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/media/folders": {
      "get": {
        "tags": [
          "Media"
        ],
        "summary": "List Media Folders",
        "description": "List media folders for the current account.",
        "responses": {
          "200": {
            "description": "Folder list",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListMediaFoldersResponse"
                }
              }
            }
          }
        }
      },
      "post": {
        "tags": [
          "Media"
        ],
        "summary": "Create Media Folder",
        "description": "Create a new media folder.",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateMediaFolderRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Folder created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateMediaFolderResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/media/folders/:id": {
      "put": {
        "tags": [
          "Media"
        ],
        "summary": "Rename Media Folder",
        "description": "Rename a media folder.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/RenameMediaFolderRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Folder renamed",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Folder not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "Media"
        ],
        "summary": "Delete Media Folder",
        "description": "Delete a media folder. Media items in the folder are not deleted.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Folder deleted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Folder not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/assets/tags": {
      "get": {
        "tags": [
          "Assets"
        ],
        "summary": "List Asset Tags",
        "description": "List all unique tags across assets for the current account",
        "responses": {
          "200": {
            "description": "Tag list",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/AssetTagsResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/assets": {
      "get": {
        "tags": [
          "Assets"
        ],
        "summary": "List Assets",
        "description": "List assets for the current account",
        "parameters": [
          {
            "schema": {
              "type": [
                "integer",
                "null"
              ],
              "minimum": 0,
              "default": 0,
              "example": 0
            },
            "required": false,
            "name": "page",
            "in": "query"
          },
          {
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100,
              "default": 20,
              "example": 20
            },
            "required": false,
            "name": "limit",
            "in": "query"
          },
          {
            "schema": {
              "type": "string"
            },
            "required": false,
            "name": "search",
            "in": "query"
          },
          {
            "schema": {
              "type": "string",
              "example": "chart"
            },
            "required": false,
            "name": "type",
            "in": "query"
          },
          {
            "schema": {
              "type": "string"
            },
            "required": false,
            "name": "tag",
            "in": "query"
          },
          {
            "schema": {
              "type": "string",
              "description": "Comma-separated category names to filter by"
            },
            "required": false,
            "name": "datasources",
            "in": "query"
          },
          {
            "schema": {
              "type": "string",
              "enum": [
                "all",
                "mine",
                "standard"
              ],
              "default": "all"
            },
            "required": false,
            "name": "source",
            "in": "query"
          },
          {
            "schema": {
              "type": "string",
              "default": "created_at"
            },
            "required": false,
            "name": "sort_by",
            "in": "query"
          },
          {
            "schema": {
              "type": [
                "number",
                "null"
              ],
              "default": -1
            },
            "required": false,
            "name": "sort_order",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "Asset list",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListAssetsResponse"
                }
              }
            }
          }
        }
      },
      "post": {
        "tags": [
          "Assets"
        ],
        "summary": "Create Asset",
        "description": "Create a new asset",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateAssetRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Asset created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateAssetResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/assets/:id/duplicate": {
      "post": {
        "tags": [
          "Assets"
        ],
        "summary": "Duplicate Asset",
        "description": "Duplicate an asset with a new name",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/DuplicateAssetRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Asset duplicated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DuplicateAssetResponse"
                }
              }
            }
          },
          "404": {
            "description": "Source asset not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/assets/:id/widgets": {
      "get": {
        "tags": [
          "Assets"
        ],
        "summary": "List Asset Widgets",
        "description": "List the widgets that belong to an asset",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Asset widgets",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListAssetWidgetsResponse"
                }
              }
            }
          },
          "404": {
            "description": "Asset not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/assets/:id": {
      "get": {
        "tags": [
          "Assets"
        ],
        "summary": "Get Asset",
        "description": "Get a single asset by ID",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Asset",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GetAssetResponse"
                }
              }
            }
          },
          "404": {
            "description": "Asset not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "put": {
        "tags": [
          "Assets"
        ],
        "summary": "Update Asset",
        "description": "Update an asset",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UpdateAssetRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Asset updated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Asset not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "Assets"
        ],
        "summary": "Delete Asset",
        "description": "Delete an asset",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Asset deleted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Asset not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/pdf/generate": {
      "post": {
        "tags": [
          "PDF"
        ],
        "summary": "Generate PDF",
        "description": "Enqueue a PDF generation job for a report.",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/GeneratePdfRequest"
              }
            }
          }
        },
        "responses": {
          "202": {
            "description": "PDF generation queued",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GeneratePdfResponse"
                }
              }
            }
          },
          "503": {
            "description": "S3 not configured",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/pdf/status/:job_id": {
      "get": {
        "tags": [
          "PDF"
        ],
        "summary": "Get PDF Status",
        "description": "Poll the status of a PDF generation job.",
        "parameters": [
          {
            "schema": {
              "type": "string",
              "minLength": 1
            },
            "required": true,
            "name": "job_id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Job status",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PdfStatusResponse"
                }
              }
            }
          },
          "404": {
            "description": "Job not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/templates": {
      "get": {
        "tags": [
          "Templates"
        ],
        "summary": "List Templates",
        "description": "List templates for the current account.",
        "parameters": [
          {
            "schema": {
              "type": [
                "integer",
                "null"
              ],
              "minimum": 0,
              "default": 0,
              "example": 0
            },
            "required": false,
            "name": "page",
            "in": "query"
          },
          {
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100,
              "default": 20,
              "example": 20
            },
            "required": false,
            "name": "limit",
            "in": "query"
          },
          {
            "schema": {
              "type": "string"
            },
            "required": false,
            "name": "search",
            "in": "query"
          },
          {
            "schema": {
              "type": "string",
              "enum": [
                "ranking",
                "created_at",
                "name"
              ],
              "default": "ranking",
              "example": "ranking"
            },
            "required": false,
            "name": "sort_by",
            "in": "query"
          },
          {
            "schema": {
              "anyOf": [
                {
                  "type": "string",
                  "enum": [
                    "asc",
                    "desc"
                  ]
                },
                {
                  "type": [
                    "integer",
                    "null"
                  ],
                  "minimum": -1,
                  "maximum": 1
                },
                {
                  "type": "null"
                }
              ],
              "default": "desc",
              "example": "desc"
            },
            "required": false,
            "name": "sort_order",
            "in": "query"
          },
          {
            "schema": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                }
              ],
              "description": "Filter by integration IDs"
            },
            "required": false,
            "name": "datasources",
            "in": "query"
          },
          {
            "schema": {
              "type": "string",
              "enum": [
                "standard",
                "mine"
              ],
              "default": "standard",
              "description": "standard = Oviond templates, mine = user templates"
            },
            "required": false,
            "name": "source",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "Template list",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListTemplatesResponse"
                }
              }
            }
          }
        }
      },
      "post": {
        "tags": [
          "Templates"
        ],
        "summary": "Create Template",
        "description": "Create a new template, optionally copying pages and widgets from a project.",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateTemplateRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Template created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateTemplateResponse"
                }
              }
            }
          },
          "404": {
            "description": "Source project not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/templates/:id": {
      "get": {
        "tags": [
          "Templates"
        ],
        "summary": "Get Template",
        "description": "Get a single template by ID.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Template document",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/TemplateResponse"
                }
              }
            }
          },
          "404": {
            "description": "Template not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "put": {
        "tags": [
          "Templates"
        ],
        "summary": "Update Template",
        "description": "Update a template.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UpdateTemplateRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Template updated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Template not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "Templates"
        ],
        "summary": "Delete Template",
        "description": "Delete a template.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Template deleted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Template not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/themes": {
      "get": {
        "tags": [
          "Themes"
        ],
        "summary": "List Themes",
        "description": "List themes for the current account.",
        "responses": {
          "200": {
            "description": "Theme list",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListThemesResponse"
                }
              }
            }
          }
        }
      },
      "post": {
        "tags": [
          "Themes"
        ],
        "summary": "Create Theme",
        "description": "Create a new theme.",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateThemeRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Theme created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateThemeResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/themes/:id": {
      "get": {
        "tags": [
          "Themes"
        ],
        "summary": "Get Theme",
        "description": "Get a single theme by ID.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Theme document",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ThemeResponse"
                }
              }
            }
          },
          "404": {
            "description": "Theme not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "put": {
        "tags": [
          "Themes"
        ],
        "summary": "Update Theme",
        "description": "Update a theme.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UpdateThemeRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Theme updated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Theme not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "Themes"
        ],
        "summary": "Delete Theme",
        "description": "Delete a theme.",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Theme deleted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Theme not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/automations": {
      "get": {
        "tags": [
          "Automations"
        ],
        "summary": "List Automations",
        "description": "List automations across all projects for the current account",
        "parameters": [
          {
            "schema": {
              "type": "string",
              "description": "Filter by project ID"
            },
            "required": false,
            "name": "project_id",
            "in": "query"
          },
          {
            "schema": {
              "type": "string",
              "description": "Filter by client ID"
            },
            "required": false,
            "name": "client_id",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "Automation list",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListAutomationsResponse"
                }
              }
            }
          }
        }
      },
      "post": {
        "tags": [
          "Automations"
        ],
        "summary": "Create Automation",
        "description": "Create a new automation for a project",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateAutomationRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Automation created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateAutomationResponse"
                }
              }
            }
          },
          "404": {
            "description": "Parent project not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/automations/:id/history": {
      "get": {
        "tags": [
          "Automations"
        ],
        "summary": "Get Automation History",
        "description": "Get execution history for an automation",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          },
          {
            "schema": {
              "type": [
                "integer",
                "null"
              ],
              "minimum": 0,
              "default": 0
            },
            "required": false,
            "name": "page",
            "in": "query"
          },
          {
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 50,
              "default": 5
            },
            "required": false,
            "name": "limit",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "Execution history",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/AutomationHistoryResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/automations/:id": {
      "put": {
        "tags": [
          "Automations"
        ],
        "summary": "Update Automation",
        "description": "Update automation schedule and notification settings",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UpdateAutomationRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Automation updated",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Automation or project not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "Automations"
        ],
        "summary": "Delete Automation",
        "description": "Soft-delete an automation and remove it from the cron scheduler",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "parent_id": {
                    "type": "string",
                    "minLength": 1
                  }
                },
                "required": [
                  "parent_id"
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Automation deleted",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Automation not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/automations/bulk": {
      "delete": {
        "tags": [
          "Automations"
        ],
        "summary": "Bulk Delete Automations",
        "description": "Soft-delete multiple automations and remove them from the cron scheduler",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "ids": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "minItems": 1
                  }
                },
                "required": [
                  "ids"
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Automations deleted",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean",
                      "enum": [
                        true
                      ]
                    }
                  },
                  "required": [
                    "success"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/automations/:id/pause": {
      "put": {
        "tags": [
          "Automations"
        ],
        "summary": "Pause Automation",
        "description": "Pause an automation (removes the cron job but retains the config)",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "parent_id": {
                    "type": "string",
                    "minLength": 1
                  }
                },
                "required": [
                  "parent_id"
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Automation paused",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Automation not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/automations/:id/unpause": {
      "put": {
        "tags": [
          "Automations"
        ],
        "summary": "Unpause Automation",
        "description": "Resume a paused automation (re-registers the cron job)",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "parent_id": {
                    "type": "string",
                    "minLength": 1
                  }
                },
                "required": [
                  "parent_id"
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Automation resumed",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuccessResponse"
                }
              }
            }
          },
          "404": {
            "description": "Automation not found",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "error"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/automations/:id/test": {
      "post": {
        "tags": [
          "Automations"
        ],
        "summary": "Test Automation",
        "description": "Trigger a test execution of an automation",
        "parameters": [
          {
            "schema": {
              "type": "string"
            },
            "required": true,
            "name": "id",
            "in": "path"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/TestAutomationRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Test triggered",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/TestAutomationResponse"
                }
              }
            }
          }
        }
      }
    },
    "/v1/archive": {
      "get": {
        "tags": [
          "Archive"
        ],
        "summary": "List Archive",
        "description": "List archived items (paginated)",
        "parameters": [
          {
            "schema": {
              "type": [
                "integer",
                "null"
              ],
              "minimum": 0,
              "default": 0
            },
            "required": false,
            "name": "page",
            "in": "query"
          },
          {
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100,
              "default": 20
            },
            "required": false,
            "name": "limit",
            "in": "query"
          },
          {
            "schema": {
              "type": "string"
            },
            "required": false,
            "name": "search",
            "in": "query"
          },
          {
            "schema": {
              "type": "string"
            },
            "required": false,
            "name": "types",
            "in": "query"
          },
          {
            "schema": {
              "type": "string",
              "enum": [
                "name",
                "deleted_at"
              ],
              "default": "deleted_at"
            },
            "required": false,
            "name": "sort_by",
            "in": "query"
          },
          {
            "schema": {
              "type": "string",
              "enum": [
                "asc",
                "desc"
              ],
              "default": "desc"
            },
            "required": false,
            "name": "order",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "Paginated archived items",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean",
                      "enum": [
                        true
                      ]
                    },
                    "data": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string"
                          },
                          "name": {
                            "type": "string"
                          },
                          "deleted_at": {
                            "type": [
                              "string",
                              "null"
                            ]
                          },
                          "type": {
                            "type": "string",
                            "enum": [
                              "clients",
                              "projects",
                              "media",
                              "automations"
                            ]
                          }
                        },
                        "required": [
                          "id",
                          "name",
                          "deleted_at",
                          "type"
                        ]
                      }
                    },
                    "meta": {
                      "type": "object",
                      "properties": {
                        "page": {
                          "type": "number"
                        },
                        "limit": {
                          "type": "number"
                        },
                        "total": {
                          "type": "number"
                        }
                      },
                      "required": [
                        "page",
                        "limit",
                        "total"
                      ]
                    }
                  },
                  "required": [
                    "success",
                    "data",
                    "meta"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/archive/counts": {
      "get": {
        "tags": [
          "Archive"
        ],
        "summary": "Get Archive Counts",
        "description": "Archived item counts per type",
        "responses": {
          "200": {
            "description": "Archived counts per type",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean",
                      "enum": [
                        true
                      ]
                    },
                    "data": {
                      "type": "object",
                      "properties": {
                        "clients": {
                          "type": "number"
                        },
                        "projects": {
                          "type": "number"
                        },
                        "media": {
                          "type": "number"
                        },
                        "automations": {
                          "type": "number"
                        },
                        "total": {
                          "type": "number"
                        }
                      },
                      "required": [
                        "clients",
                        "projects",
                        "media",
                        "automations",
                        "total"
                      ]
                    }
                  },
                  "required": [
                    "success",
                    "data"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/archive/restore": {
      "put": {
        "tags": [
          "Archive"
        ],
        "summary": "Restore Items",
        "description": "Restore soft-deleted items",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ArchiveBulkBody"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Items restored",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean",
                      "enum": [
                        true
                      ]
                    },
                    "message": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "success",
                    "message"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/archive/permanent": {
      "delete": {
        "tags": [
          "Archive"
        ],
        "summary": "Delete Permanently",
        "description": "Permanently delete archived items",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ArchiveBulkBody"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Items permanently deleted",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean",
                      "enum": [
                        true
                      ]
                    },
                    "message": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "success",
                    "message"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "/v1/activity": {
      "get": {
        "tags": [
          "Activity"
        ],
        "summary": "List Activity",
        "description": "List activity logs for the current account",
        "parameters": [
          {
            "schema": {
              "type": [
                "integer",
                "null"
              ],
              "minimum": 0,
              "default": 0,
              "example": 0
            },
            "required": false,
            "name": "page",
            "in": "query"
          },
          {
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100,
              "default": 20,
              "example": 20
            },
            "required": false,
            "name": "limit",
            "in": "query"
          },
          {
            "schema": {
              "type": "string",
              "example": "client"
            },
            "required": false,
            "name": "resource_type",
            "in": "query"
          },
          {
            "schema": {
              "type": "string",
              "example": "acme"
            },
            "required": false,
            "name": "search",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "Paginated activity log",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean",
                      "enum": [
                        true
                      ]
                    },
                    "data": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "additionalProperties": {}
                      }
                    },
                    "meta": {
                      "type": "object",
                      "properties": {
                        "page": {
                          "type": "number"
                        },
                        "limit": {
                          "type": "number"
                        },
                        "total": {
                          "type": "number"
                        }
                      },
                      "required": [
                        "page",
                        "limit",
                        "total"
                      ]
                    }
                  },
                  "required": [
                    "success",
                    "data",
                    "meta"
                  ]
                }
              }
            }
          }
        }
      }
    }
  },
  "webhooks": {}
}