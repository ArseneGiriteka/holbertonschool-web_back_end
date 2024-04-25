#!/usr/bin/env python3
"""
function that calculate the sum of float stored in
a list and return that sum as a float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    function sum_list
    argument input_list
    return float
    """
    return float(sum(input_list))
