#!/usr/bin/env python3
"""
Inserting new documents in a collection
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    function to insert a new document in mongo_collection
    """
    document = mongo_collection.insert_one(kwargs)
    return document.inserted_id
