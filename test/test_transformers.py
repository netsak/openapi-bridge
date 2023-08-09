import pytest

from openapi_bridge import _flatten_single, _replace_const, _remove_null_type


def test_flatten_single():
    schema = {
        "properties": {
            "brands": {
                "anyOf": [
                    {
                        "items": {
                            "type": "integer",
                        },
                        "type": "array",
                    },
                ],
            },
            "availability": {
                "anyOf": [
                    {
                        "items": {
                            "enum": [
                                1,
                                2,
                                3,
                                99,
                            ],
                            "type": "integer",
                        },
                        "type": "array",
                    },
                ],
                "description": "my description",
            },
        },
    }
    _flatten_single(schema, "anyOf")
    from pprint import pprint

    pprint(schema)
    assert schema == {
        "properties": {
            "brands": {
                "items": {
                    "type": "integer",
                },
                "type": "array",
            },
            "availability": {
                "items": {
                    "enum": [
                        1,
                        2,
                        3,
                        99,
                    ],
                    "type": "integer",
                },
                "type": "array",
                "description": "my description",
            },
        },
    }


def test_replace_const():
    schema = {
        "properties": {
            "is_on_sale": {
                "items": {
                    "const": 1,
                },
                "type": "array",
            },
        },
    }
    _replace_const(schema)
    from pprint import pprint

    pprint(schema)
    assert schema == {
        "properties": {
            "is_on_sale": {
                "items": {
                    "enum": [1],
                },
                "type": "array",
            },
        },
    }


def test_flatten_single_anyOf_null_type():
    schema = {
        "properties": {
            "export_type": {
                "anyOf": [
                    {
                        "$ref": "#/components/schemas/ExportType",
                    },
                    {
                        "type": "null",
                    },
                ]
            },
        }
    }
    _remove_null_type(schema)
    assert schema == {
        "properties": {
            "export_type": {
                "anyOf": [
                    {
                        "$ref": "#/components/schemas/ExportType",
                    },
                ]
            },
        }
    }


def test_transform_anyOf_null_type_with_description():
    schema = {
        "properties": {
            "cheapest_offer": {
                "anyOf": [
                    {
                        "$ref": "#/components/schemas/Offer",
                    },
                    {
                        "type": "null",
                    },
                ],
                "description": "Cheapest offer in the baseproduct",
            },
        },
    }
    _remove_null_type(schema)
    assert schema == {
        "properties": {
            "cheapest_offer": {
                "anyOf": [
                    {
                        "$ref": "#/components/schemas/Offer",
                    },
                ],
                "description": "Cheapest offer in the baseproduct",
            },
        }
    }


def test_remove_anyOf_null_type():
    schema = {
        "properties": {
            "min_price": {
                "anyOf": [
                    {
                        "type": "number",
                    },
                    {
                        "type": "string",
                    },
                    {
                        "type": "null",
                    },
                ]
            },
            "shop_prices": {
                "additionalProperties": {
                    "anyOf": [
                        {
                            "type": "number",
                        },
                        {
                            "type": "string",
                        },
                        {
                            "type": "null",
                        },
                    ]
                },
            },
        },
    }
    _remove_null_type(schema)
    assert schema == {
        "properties": {
            "min_price": {
                "anyOf": [
                    {
                        "type": "number",
                    },
                    {
                        "type": "string",
                    },
                ]
            },
            "shop_prices": {
                "additionalProperties": {
                    "anyOf": [
                        {
                            "type": "number",
                        },
                        {
                            "type": "string",
                        },
                    ]
                },
            },
        }
    }
