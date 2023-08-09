import pytest
from typing import Optional
from openapi_bridge import endpoint, get_pydantic_schemata
from . import pydantic_models


def test_models():
    specs = get_pydantic_schemata(pydantic_models)
    print(specs)
    assert specs == {
        "components": {
            "schemas": {
                "Klasse0": {"type": "object", "properties": {}},
                "Klasse1": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"},
                        "admin": {"type": "boolean"},
                        "age": {"type": "number"},
                        "date": {"type": "string", "format": "date"},
                        "datetime": {"type": "string", "format": "date-time"},
                    },
                    "required": ["id", "name", "admin", "age", "date", "datetime"],
                },
                "CategoryBase": {
                    "properties": {
                        "id": {"description": "the ID of the category", "type": "integer"},
                        "parent_id": {
                            "description": "the ID of the category's parent",
                            "type": "integer",
                        },
                    },
                    "required": ["id"],
                    "type": "object",
                },
                "CategoryTreeItem": {
                    "properties": {
                        "children": {
                            "description": "a array of categories (as `CategoryTreeItem`) containing all child categories of this category",
                            "items": {"$ref": "#/components/schemas/CategoryTreeItem"},
                            "type": "array",
                        },
                        "id": {"description": "the ID of the category", "type": "integer"},
                        "parent_id": {
                            "description": "the ID of the category's parent",
                            "type": "integer",
                        },
                    },
                    "required": ["id", "children"],
                    "type": "object",
                },
            }
        }
    }
