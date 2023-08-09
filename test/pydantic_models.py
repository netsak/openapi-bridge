from __future__ import annotations

import pydantic
import datetime
import decimal
import typing

class Klasse0(pydantic.BaseModel):
    ...

class Klasse1(pydantic.BaseModel):
    id: int
    name: str
    admin: bool
    age: float
    date: datetime.date
    datetime: datetime.datetime
    # differend handling here
    # 1: "decimal": {"type": "number"},
    # 2: 'decimal': {'anyOf': [{'type': 'number'}, {'type': 'string'}]},
    # decimal: decimal.Decimal


class CategoryBase(pydantic.BaseModel):
    id: int = pydantic.Field(..., description="the ID of the category")
    parent_id: typing.Optional[int] = pydantic.Field(
        None, description="the ID of the category's parent"
    )


class CategoryTreeItem(CategoryBase):
    children: typing.List[CategoryTreeItem] = pydantic.Field(
        ...,
        description="a array of categories (as `CategoryTreeItem`) containing all child categories of this category",
    )
