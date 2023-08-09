from typing import Optional, Literal
from openapi_bridge import endpoint
from decimal import Decimal
from datetime import date, datetime


@endpoint("/other")
def other(
    *,
    my_literal: Literal["ausu", "coredata"],
    my_optional: Optional[str] = "solute",
) -> bool:
    """
    other description
    @section MySection
    @param my_literal my literal description
    @param my_optional my optional description
    @response 200 {"description": "was the operation a success?"}
    """
    pass

# TODO: add section