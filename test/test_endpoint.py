import pytest
from openapi_bridge import get_pydantic_schemata, PATHS
from . import pydantic_no_models
from pprint import pprint


def test_no_params():
    from .endpoints import no_params

    specs = get_pydantic_schemata(pydantic_no_models)
    assert specs == {
        "components": {
            "schemas": {
                "Klasse0": {"type": "object", "properties": {}},
            }
        }
    }
    pprint(PATHS)
    assert PATHS["default"]["/no-params"] == {
        "get": {
            "parameters": [],
            "summary": "no_params description",
            "description": "",
            "tags": [],
            "operationId": "test.endpoints.no_params.no_params",
            "responses": {
                200: {"description": "was the operation a success?"},
                400: {
                    "description": "Client error",
                    "content": {
                        "application/problem+json": {
                            "schema": {"$ref": "#/components/schemas/Problem"}
                        }
                    },
                },
            },
            "security": [{"basic": []}],
        }
    }


def test_standard_query():
    from .endpoints import standard_query

    specs = get_pydantic_schemata(pydantic_no_models)
    assert specs == {
        "components": {
            "schemas": {
                "Klasse0": {"type": "object", "properties": {}},
            }
        }
    }
    pprint(PATHS)
    assert PATHS["default"]["/standard-query"] == {
        "get": {
            "description": "",
            "operationId": "test.endpoints.standard_query.standard_query",
            "parameters": [
                {
                    "description": "my " "int " "description",
                    "in": "query",
                    "name": "my_int",
                    "required": True,
                    "schema": {"type": "integer"},
                },
                {
                    "description": "my " "str " "description",
                    "in": "query",
                    "name": "my_str",
                    "required": True,
                    "schema": {"type": "string"},
                },
                {
                    "description": "my " "float " "description",
                    "in": "query",
                    "name": "my_float",
                    "required": True,
                    "schema": {"type": "number"},
                },
                {
                    "description": "my " "bool " "description",
                    "in": "query",
                    "name": "my_bool",
                    "required": True,
                    "schema": {"type": "boolean"},
                },
                {
                    "description": "my " "decimal " "description",
                    "in": "query",
                    "name": "my_decimal",
                    "required": True,
                    "schema": {"format": "decimal", "type": "number"},
                },
                {
                    "description": "my " "datetime " "description",
                    "in": "query",
                    "name": "my_datetime",
                    "required": True,
                    "schema": {"format": "date-time", "type": "string"},
                },
                {
                    "description": "my " "date " "description",
                    "in": "query",
                    "name": "my_date",
                    "required": True,
                    "schema": {"format": "date", "type": "string"},
                },
                {
                    "description": "my " "bytes " "description",
                    "in": "query",
                    "name": "my_bytes",
                    "required": True,
                    "schema": {"format": "binary", "type": "string"},
                },
            ],
            "responses": {
                200: {"description": "my " "response"},
                400: {
                    "content": {
                        "application/problem+json": {
                            "schema": {"$ref": "#/components/schemas/Problem"}
                        }
                    },
                    "description": "Client " "error",
                },
            },
            "security": [{"basic": []}],
            "summary": "standard_query " "description",
            "tags": [],
        }
    }


def test_constraints():
    from .endpoints import constraints

    specs = get_pydantic_schemata(pydantic_no_models)
    assert specs == {
        "components": {
            "schemas": {
                "Klasse0": {"type": "object", "properties": {}},
            }
        }
    }
    pprint(PATHS)
    assert PATHS["default"]["/constraints"] == {
        "get": {
            "description": "",
            "operationId": "test.endpoints.constraints.constraints",
            "parameters": [
                {
                    "description": "my " "str " "description",
                    "in": "query",
                    "name": "my_str",
                    "required": True,
                    "schema": {
                        "pattern": "^[a-zA-Z0-9_#]$",
                        "type": "string",
                    },
                },
                {
                    "description": "my int " "description",
                    "in": "query",
                    "name": "my_int",
                    "required": True,
                    "schema": {"maximum": 100, "minimum": 1, "type": "integer"},
                },
            ],
            "responses": {
                200: {"description": "my " "response"},
                400: {
                    "content": {
                        "application/problem+json": {
                            "schema": {"$ref": "#/components/schemas/Problem"}
                        }
                    },
                    "description": "Client " "error",
                },
            },
            "security": [{"basic": []}],
            "summary": "standard_query " "description",
            "tags": [],
        }
    }


def test_lists():
    from .endpoints import lists

    specs = get_pydantic_schemata(pydantic_no_models)
    assert specs == {
        "components": {
            "schemas": {
                "Klasse0": {"type": "object", "properties": {}},
            }
        }
    }
    pprint(PATHS)
    assert PATHS["default"]["/lists"] == {
        "get": {
            "description": "",
            "operationId": "test.endpoints.lists.lists",
            "parameters": [
                {
                    "description": "my int_list description",
                    "in": "query",
                    "name": "my_int_list",
                    "required": True,
                    "schema": {"items": {"type": "integer"}, "type": "array"},
                },
                {
                    "description": "my str_list description",
                    "in": "query",
                    "name": "my_str_list",
                    "required": True,
                    "schema": {
                        "items": {"type": "string"},
                        "maxItems": 100,
                        "minItems": 1,
                        "type": "array",
                    },
                },
            ],
            "responses": {
                200: {"description": "was the operation a success?"},
                400: {
                    "content": {
                        "application/problem+json": {
                            "schema": {"$ref": "#/components/schemas/Problem"}
                        }
                    },
                    "description": "Client " "error",
                },
            },
            "security": [{"basic": []}],
            "summary": "other description",
            "tags": [],
        }
    }


def test_other():
    from .endpoints import other

    specs = get_pydantic_schemata(pydantic_no_models)
    assert specs == {
        "components": {
            "schemas": {
                "Klasse0": {"type": "object", "properties": {}},
            }
        }
    }
    pprint(PATHS)
    assert PATHS["default"]["/other"] == {
        "get": {
            "description": "",
            "operationId": "test.endpoints.other.other",
            "parameters": [
                {
                    "description": "my literal " "description",
                    "in": "query",
                    "name": "my_literal",
                    "required": True,
                    "schema": {"enum": ["ausu", "coredata"], "type": "string"},
                },
                {
                    "description": "my optional " "description",
                    "in": "query",
                    "name": "my_optional",
                    "required": False,
                    "schema": {"default": "solute", "type": "string"},
                },
            ],
            "responses": {
                200: {"description": "was the operation a success?"},
                400: {
                    "content": {
                        "application/problem+json": {
                            "schema": {"$ref": "#/components/schemas/Problem"}
                        }
                    },
                    "description": "Client " "error",
                },
            },
            "security": [{"basic": []}],
            "summary": "other description",
            "tags": ["MySection"],
        }
    }


def test_body():
    from .endpoints import body

    specs = get_pydantic_schemata(pydantic_no_models)
    assert specs == {
        "components": {
            "schemas": {
                "Klasse0": {"type": "object", "properties": {}},
            }
        }
    }
    pprint(PATHS)
    assert PATHS["default"]["/body"] == {
        "get": {
            "description": "",
            "operationId": "test.endpoints.body.body",
            "parameters": [
                {
                    "description": "my request body " "description",
                    "explode": True,
                    "in": "query",
                    "name": "body",
                    "required": True,
                    "schema": {
                        "properties": {
                            "my_str": {"type": "string"},
                            "my_user": {"default": "bob", "type": "string"},
                        },
                        "type": "object",
                    },
                    "style": "deepObject",
                }
            ],
            "responses": {
                200: {
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/MyRequestBody"}
                        }
                    },
                    "description": "OK",
                },
                400: {
                    "content": {
                        "application/problem+json": {
                            "schema": {"$ref": "#/components/schemas/Problem"}
                        }
                    },
                    "description": "Client " "error",
                },
            },
            "security": [{"basic": []}],
            "summary": "other description",
            "tags": [],
        }
    }
