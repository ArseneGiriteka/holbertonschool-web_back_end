#!/usr/bin/env python3
"""
this module is new
"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    function index_range take start page and the size of each page
    return the start index and the end index in a tuple
    """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        object constuctor that initiate
        a data set attr as none
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        a method to get a page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        self.dataset()

        start_index, end_index = index_range(page, page_size)
        if start_index >= len(self.__dataset):
            return []
        return self.__dataset[start_index:end_index]
