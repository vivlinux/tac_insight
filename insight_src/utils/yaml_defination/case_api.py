import yaml

openapi_definition = {
    "openapi": "3.0.0",
    "info": {
        "title": "Cisco Support Case API v3",
        "description": "API for interacting with the Cisco Support Case Manager tool",
        "version": "3.0.0"
    },
    "servers": [
        {
            "url": "https://apix.cisco.com/case/v3"
        }
    ],
    "paths": {
        "/cases/case_ids/{case_ids}": {
            "get": {
                "summary": "Get Case Summary",
                "description": "Returns brief information for the specified case or cases",
                "parameters": [
                    {
                        "name": "case_ids",
                        "in": "path",
                        "required": True,
                        "schema": {
                            "type": "string"
                        },
                        "description": "Comma-separated list of case IDs (max 30)"
                    },
                    {
                        "name": "sort_by",
                        "in": "query",
                        "required": False,
                        "schema": {
                            "type": "string",
                            "enum": ["STATUS", "SEVERITY", "CREATED_DATE", "UPDATED_DATE"]
                        },
                        "description": "Order in which the results should be sorted"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/CaseSummaryResponse"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/cases/details/case_id/{case_id}": {
            "get": {
                "summary": "Get Case Details",
                "description": "Returns detailed information for the specified case",
                "parameters": [
                    {
                        "name": "case_id",
                        "in": "path",
                        "required": True,
                        "schema": {
                            "type": "string"
                        },
                        "description": "Identifier of the case"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/CaseDetailResponse"
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "components": {
        "schemas": {
            "CaseSummaryResponse": {
                "type": "object",
                "properties": {
                    "count": {
                        "type": "integer"
                    },
                    "cases": {
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/CaseSummary"
                        }
                    }
                }
            },
            "CaseSummary": {
                "type": "object",
                "properties": {
                    "item_entry_id": {"type": "integer"},
                    "user_id": {"type": "string"},
                    "case_id": {"type": "string"},
                    "title": {"type": "string"},
                    "severity": {"type": "integer"},
                    "contact_name": {"type": "string"},
                    "status_flag": {"type": "string"},
                    "status": {"type": "string"},
                    "creation_date": {"type": "string", "format": "date-time"},
                    "updated_date": {"type": "string", "format": "date-time"},
                    "serial_number": {"type": "string"},
                    "contract_id": {"type": "string"},
                    "technology_name": {"type": "string"},
                    "sub_technology_name": {"type": "string"},
                    "rmas": {"type": "array", "items": {"type": "string"}},
                    "bugs": {"type": "array", "items": {"type": "string"}}
                }
            },
            "CaseDetailResponse": {
                "type": "object",
                "properties": {
                    "caseDetail": {
                        "$ref": "#/components/schemas/CaseDetail"
                    }
                }
            },
            "CaseDetail": {
                "type": "object",
                "properties": {
                    "user_id": {"type": "string"},
                    "case_id": {"type": "string"},
                    "title": {"type": "string"},
                    "severity": {"type": "string"},
                    "status": {"type": "string"},
                    "creation_date": {"type": "string", "format": "date-time"},
                    "updated_date": {"type": "string", "format": "date-time"},
                    "serial_number": {"type": "string"},
                    "contract_id": {"type": "string"},
                    "contact_user_id": {"type": "string"},
                    "contact_name": {"type": "string"},
                    "preferred_contact_method": {"type": "string"},
                    "contact_email_ids": {"type": "array", "items": {"type": "string"}},
                    "contact_business_phone_numbers": {"type": "array", "items": {"type": "string"}},
                    "contact_mobile_phone_numbers": {"type": "array", "items": {"type": "string"}},
                    "owner_name": {"type": "string"},
                    "owner_email": {"type": "string"},
                    "close_date": {"type": "string", "format": "date-time"},
                    "technology_name": {"type": "string"},
                    "sub_technology_name": {"type": "string"},
                    "tracking_number": {"type": "string"},
                    "problem_code_name": {"type": "string"},
                    "request_type": {"type": "string"},
                    "rmas": {"type": "array", "items": {"type": "string"}},
                    "bugs": {"type": "array", "items": {"type": "string"}},
                    "notes": {"type": "array", "items": {"$ref": "#/components/schemas/Note"}}
                }
            },
            "Note": {
                "type": "object",
                "properties": {
                    "note": {"type": "string"},
                    "note_detail": {"type": "string"},
                    "created_by": {"type": "string"},
                    "creation_date": {"type": "string", "format": "date-time"}
                }
            }
        }
    }
}

# Add the n
openapi_definition["paths"]["/cases/users/user_ids/{user_ids}"] = {
    "get": {
        "summary": "Get Cases by User ID",
        "description": "Returns summary information for cases associated with the specified user or users",
        "parameters": [
            {
                "name": "user_ids",
                "in": "path",
                "required": True,
                "schema": {
                    "type": "string"
                },
                "description": "Identifier of the user or users for which to return results (comma-separated, max 10)"
            },
            {
                "name": "date_created_from",
                "in": "query",
                "required": False,
                "schema": {
                    "type": "string",
                    "format": "date-time"
                },
                "description": "Beginning date (in UTC) of the range in which to search"
            },
            {
                "name": "date_created_to",
                "in": "query",
                "required": False,
                "schema": {
                    "type": "string",
                    "format": "date-time"
                },
                "description": "End date (in UTC) of the range in which to search"
            },
            {
                "name": "status_flag",
                "in": "query",
                "required": False,
                "schema": {
                    "type": "string",
                    "enum": ["O", "C"]
                },
                "description": "Return only cases associated with the specified status"
            },
            {
                "name": "sort_by",
                "in": "query",
                "required": False,
                "schema": {
                    "type": "string",
                    "enum": ["STATUS", "SEVERITY", "CREATED_DATE", "UPDATED_DATE"]
                },
                "description": "Order in which the results should be sorted"
            },
            {
                "name": "page_index",
                "in": "query",
                "required": False,
                "schema": {
                    "type": "integer"
                },
                "description": "Index number of the page to return"
            }
        ],
        "responses": {
            "200": {
                "description": "Successful response",
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/CasesByUserIdResponse"
                        }
                    }
                }
            }
        }
    }
}

# Add new schema for the response
openapi_definition["components"]["schemas"]["CasesByUserIdResponse"] = {
    "type": "object",
    "properties": {
        "pagination_response_record": {
            "$ref": "#/components/schemas/PaginationResponseRecord"
        },
        "cases": {
            "type": "array",
            "items": {
                "$ref": "#/components/schemas/CaseSummary"
            }
        }
    }
}

# Add PaginationResponseRecord schema
openapi_definition["components"]["schemas"]["PaginationResponseRecord"] = {
    "type": "object",
    "properties": {
        "last_index": {"type": "integer"},
        "page_index": {"type": "integer"},
        "page_records": {"type": "integer"},
        "self_link": {"type": "string"},
        "title": {"type": "string"},
        "total_records": {"type": "integer"}
    }
}

# Add the new endpoint to the existing 'paths' dictionary
openapi_definition["paths"]["/cases/contracts/contract_ids/{contract_ids}"] = {
    "get": {
        "summary": "Get Cases by Contract ID",
        "description": "Returns summary information for cases associated with the specified contract or contracts",
        "parameters": [
            {
                "name": "contract_ids",
                "in": "path",
                "required": True,
                "schema": {
                    "type": "string"
                },
                "description": "Identifier of the contract or contracts for which to return results (comma-separated, max 10)"
            },
            {
                "name": "date_created_from",
                "in": "query",
                "required": False,
                "schema": {
                    "type": "string",
                    "format": "date-time"
                },
                "description": "Beginning date (in UTC) of the range in which to search"
            },
            {
                "name": "date_created_to",
                "in": "query",
                "required": False,
                "schema": {
                    "type": "string",
                    "format": "date-time"
                },
                "description": "End date (in UTC) of the range in which to search"
            },
            {
                "name": "status_flag",
                "in": "query",
                "required": False,
                "schema": {
                    "type": "string",
                    "enum": ["O", "C"]
                },
                "description": "Return only cases associated with the specified status"
            },
            {
                "name": "sort_by",
                "in": "query",
                "required": False,
                "schema": {
                    "type": "string",
                    "enum": ["STATUS", "SEVERITY", "CREATED_DATE", "UPDATED_DATE"]
                },
                "description": "Order in which the results should be sorted"
            },
            {
                "name": "page_index",
                "in": "query",
                "required": False,
                "schema": {
                    "type": "integer"
                },
                "description": "Index number of the page to return"
            }
        ],
        "responses": {
            "200": {
                "description": "Successful response",
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/CasesByContractIdResponse"
                        }
                    }
                }
            }
        }
    }
}

# Add new schema for the response
openapi_definition["components"]["schemas"]["CasesByContractIdResponse"] = {
    "type": "object",
    "properties": {
        "pagination_response_record": {
            "$ref": "#/components/schemas/PaginationResponseRecord"
        },
        "cases": {
            "type": "array",
            "items": {
                "$ref": "#/components/schemas/CaseSummary"
            }
        }
    }
}



# Write the OpenAPI definition to a YAML file
with open('../api_yaml/cisco_support_case_api_v3.yaml', 'w') as file:
    yaml.dump(openapi_definition, file, sort_keys=False)

print("OpenAPI definition has been written to cisco_support_case_api_v3.yaml")
