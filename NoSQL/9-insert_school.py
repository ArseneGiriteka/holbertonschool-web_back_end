#!/usr/bin/env python3
"""
This module provides a function to insert a document
into a MongoDB collection.
"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Insert a document into the specified MongoDB collection.
    and return id inserted
    """
    query_result = mongo_collection.insert_one(kwargs)
    return query_result.inserted_id
