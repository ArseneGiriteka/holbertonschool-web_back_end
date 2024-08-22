#!/usr/bin/env python3
"""
this module contains a simple helper function
that returns a tuple of size two containing a start index
and an end index
"""
from typing import Tuple


def index_range(page, page_size) -> Tuple[int, int]:
    """
    returns a tuple of size two containing a start index
    and an end index
    """
    return ((page - 1) * page_size, page * page_size)
