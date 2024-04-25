#!/usr/bin/env python3
"""
function that takes a list of mixed integer and floats
and return the sum as float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    function sum_mixed_list
    arguments mxd_lst
    retun a float
    """
    return sum(mxd_lst)
