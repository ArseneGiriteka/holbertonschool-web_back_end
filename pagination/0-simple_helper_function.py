#!/usr/bin/env python3
"""
implementation of function that returns strat and end index
based of the position of the page
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    function index_range take start page and the size of each page
    return the start index and the end index in a tuple
    """
    return ((page - 1) * page_size, page * page_size)
