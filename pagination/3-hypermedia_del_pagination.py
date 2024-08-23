#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from math import ceil
from typing import List, Dict, Tuple, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        This function is get_hyper_index
        and returns a dictionary
        """
        dictionary = {}

        if index == 0:
            index = 1

        assert index >= 0 and index <= ceil(
            len(self.__indexed_dataset) / page_size)

        dictionary.update({"index": index})

        data = []
        i = 0
        size = page_size
        while i in range(size):
            if self.indexed_dataset().get(index + i):
                data.append(self.indexed_dataset().get(index + i))
            else:
                size = size + 1
            i = i + 1

        dictionary.update({"data": data})
        dictionary.update({"page_size": page_size})
        dictionary.update({"next_index": index + size})

        return dictionary
