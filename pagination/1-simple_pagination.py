#!/usr/bin/env python3
"""
this module contains a simple helper function
that returns a tuple of size two containing a start index
"""

import csv
import math
from typing import List, Tuple, Optional


class Server:
    """
    Server class to paginate a database of popular baby names.
    and return the dataset and get the page wanted
    and return the dataset
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """
        this method initiate the class
        and return the dataset and get the page wanted
        and return the dataset
        """
        self.__dataset: Optional[List[List[str]]] = None

    def dataset(self) -> List[List[str]]:
        """
        Cached dataset and return the dataset
        and return the dataset
        and return the dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        this method return the page wanted by using the correct index range
        and return the dataset
        and return the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        dataset = self.dataset()

        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    returns a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    """
    return ((page - 1) * page_size, page * page_size)
