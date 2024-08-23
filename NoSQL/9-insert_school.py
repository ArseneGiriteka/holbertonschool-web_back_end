#!/usr/bin/env python3
"""
this is a script to insert doc
"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    this function insert a doc in
    a given collection
    """
    querry_result = mongo_collection.insert_one(kwargs)
    return str(querry_result.inserted_id)
