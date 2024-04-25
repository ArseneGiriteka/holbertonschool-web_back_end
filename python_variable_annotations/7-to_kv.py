#!/usr/bin/env python3
"""
this function built a tuple ok key-value
and accept a int-float value and string value
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    function to_kv
    arguments k(str), v(int or float)
    return Tuple[str, float]
    """
    return k, v**2
