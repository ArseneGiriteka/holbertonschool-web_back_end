#!/usr/bin/env python3
"""
This script defines a function to insert a document
into a MongoDB collection.
"""

import pymongo
from pymongo.collection import Collection


def insert_school(mongo_collection: Collection, **kwargs) -> str:
    """
    Insert a document into the specified MongoDB collection.

    Args:
        mongo_collection (Collection): The pymongo collection
        object where the document will be inserted.
        **kwargs: Keyword arguments representing the fields and
        values of the document to be inserted.

    Returns:
        str: The _id of the newly inserted document as a string.
    """

    query_result = mongo_collection.insert_one(kwargs)

    return str(query_result.inserted_id)
