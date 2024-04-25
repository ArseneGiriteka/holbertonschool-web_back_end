#!/usr/bin/env python3
"""
making of miltiplier to multiply to n
and return the result as float
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier function
    multiplier float
    return function that multiplies a float by multiplier
    """
    def multiplier_func(n: float) -> float:
        """
        multiplier_func function
        n: float
        return n * multiplietr
        """
        return n * multiplier
    return multiplier_func
