#!/usr/bin/env python3
"""
function that accept an Iterable Value of Sequence
and return a tuple of squence and int
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    element_length function
    lst Iterable of Sequences
    return list of tuple(value and length)
    """
    return [(i, len(i)) for i in lst]
