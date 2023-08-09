from typing import Optional
from openapi_bridge import endpoint
from decimal import Decimal
from datetime import date, datetime
from typing_extensions import Annotated
import pydantic


if pydantic.__version__[0] == "2":
    from pydantic import StringConstraints, Field

    @endpoint("/constraints")
    def constraints(
        *,
        my_str: Annotated[str, StringConstraints(pattern=r"^[a-zA-Z0-9_#]$")],
        my_int: Annotated[int, Field(ge=1, le=100)],
    ) -> str:
        """
        standard_query description
        @param my_str my str description
        @param my_int my int description
        @response 200 {"description": "my response"}
        """

else:
    from pydantic import constr, conint

    @endpoint("/constraints")
    def constraints(
        *,
        my_str: constr(regex=r"^[a-zA-Z0-9_#]$"),
        my_int: conint(ge=1, le=100),
        # TODO: add confloat
    ) -> str:
        """
        standard_query description
        @param my_str my str description
        @param my_int my int description
        @response 200 {"description": "my response"}
        """
