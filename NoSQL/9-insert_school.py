#!/usr/bin/env python3
"""
this is a script to insert doc
and return result
"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    query_result = mongo_collection.insert_one(kwargs)
    return str(query_result.inserted_id)