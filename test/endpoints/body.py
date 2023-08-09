from typing import Optional, Literal, List
from openapi_bridge import endpoint
from decimal import Decimal
from datetime import date, datetime
from pydantic import BaseModel

# TODO: test lists in path

class MyRequestBody(BaseModel):
    my_str: str
    my_user: Optional[str] = "bob"

class MyResponseBody(BaseModel):
    my_int: int
    my_request: Optional[MyRequestBody]


@endpoint("/body")
def body(
    *,
    body: MyRequestBody,
) -> MyRequestBody:
    """
    other description
    @param body my request body description
    """
    pass
