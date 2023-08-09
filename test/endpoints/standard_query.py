from typing import Optional
from openapi_bridge import endpoint
from decimal import Decimal
from datetime import date, datetime


@endpoint("/standard-query")
def standard_query(
    *,
    my_int: int,
    my_str: str,
    my_float: float,
    my_bool: bool,
    my_decimal: Decimal,
    my_datetime: datetime,
    my_date: date,
    my_bytes: bytes,
) -> str:
    """
    standard_query description
    @param my_int my int description
    @param my_str my str description
    @param my_float my float description
    @param my_bool my bool description
    @param my_decimal my decimal description
    @param my_datetime my datetime description
    @param my_date my date description
    @param my_bytes my bytes description
    @response 200 {"description": "my response"}
    """
