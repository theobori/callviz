"""utility module"""

from typing import Any

from copy import deepcopy, Error

def try_get_copy(value: Any) -> Any:
    """Try to get a copy of `value`, if un(deep)copyable,
    it returns the value itself

    Args:
        value (Any): The value you want to copy

    Returns:
        Any: Copied value (or not)
    """

    if value is None:
        return value

    try:
        return deepcopy(value)
    except Error:
        return value
