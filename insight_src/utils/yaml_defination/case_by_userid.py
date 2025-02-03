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

# Update the existing YAML file
with open('cisco_support_case_api_v3.yaml', 'w') as file:
    yaml.dump(openapi_definition, file, sort_keys=False)

