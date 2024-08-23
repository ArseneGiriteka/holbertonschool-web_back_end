#!/usr/bin/env python3
"""
this is a script to insert doc
and return result
"""

from typing import List, Dict
from pymongo.collection import Collection


def insert_school(mongo_collection: Collection, **kwargs: List[Dict]) -> str:
    """
    this function insert a doc in
    a given collection
    """
    query_result = mongo_collection.insert_one(kwargs)
    return str(query_result.inserted_id)
