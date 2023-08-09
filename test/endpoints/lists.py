from typing import Optional, Literal, List
from openapi_bridge import endpoint
from decimal import Decimal
from datetime import date, datetime
import pydantic

# TODO: test lists in path

if pydantic.__version__[0] == "1":
    from pydantic import constr, conint, conlist

    @endpoint("/lists")
    def lists(
        *,
        my_int_list: List[int],
        my_str_list: conlist(str, min_items=1, max_items=100),
    ) -> bool:
        """
        other description
        @param my_int_list my int_list description
        @param my_str_list my str_list description
        @response 200 {"description": "was the operation a success?"}
        """
        pass

else:
    from typing_extensions import Annotated
    from pydantic import StringConstraints, Field

    @endpoint("/lists")
    def lists(
        *,
        my_int_list: List[int],
        # my_str_list: Annotated[List[str], Field(min_items=1, max_items=100)],
        my_str_list: Annotated[List[str], Field(min_items=1, max_items=100)],
    ) -> bool:
        """
        other description
        @param my_int_list my int_list description
        @param my_str_list my str_list description
        @response 200 {"description": "was the operation a success?"}
        """
        pass
