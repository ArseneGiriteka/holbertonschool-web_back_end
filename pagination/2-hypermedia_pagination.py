#!/usr/bin/env python3
"""
this module contains the class Server
and return the dataset and get the page wanted
"""

import csv
from math import ceil
from typing import List, Tuple, Optional, Dict, Any


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        this methods accepts same arguments as get_page and return
        a diction of binded data
        """
        dictionary: Dict = {}
        page_dataset = self.get_page(page, page_size)
        start_index, end_index = index_range(page, page_size)
        if page_dataset is not None:
            dictionary.update({"page_size": len(page_dataset)})
            dictionary.update({"page": page})
            dictionary.update({"data": page_dataset})
            if end_index > len(self.dataset()):
                dictionary.update({"next_page": None})
            else:
                dictionary.update({"next_page": page + 1})
            if start_index <= 0:
                dictionary.update({"prev_page": None})
            else:
                dictionary.update({"prev_page": page - 1})
            dictionary.update(
                {"total_pages": ceil(len(self.dataset()) / page_size)})
        return dictionary


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    returns a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    """
    return ((page - 1) * page_size, page * page_size)
