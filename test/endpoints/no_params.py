from typing import Optional
from openapi_bridge import endpoint
from decimal import Decimal
from datetime import date, datetime

@endpoint("/no-params")
def no_params() -> bool:
    """
    no_params description
    @response 200 {"description": "was the operation a success?"}
    """
    pass


