#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple
"""
this module contains a simple helper function
that returns a tuple of size two containing a start index
"""


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        this method initiate the class
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
        this method return the page wanted by using the correct index range
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        dataset = self.dataset()

        if page * page_size > len(dataset):
            return []

        start_index, end_index = index_range(page, page_size)
        return dataset[start_index:end_index]


def index_range(page, page_size) -> Tuple[int, int]:
    """
    returns a tuple of size two containing a start index
    and an end index
    """
    return ((page - 1) * page_size, page * page_size)
