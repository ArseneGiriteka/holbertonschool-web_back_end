#!/usr/bin/env python3
"""
updating a collection
"""


def update_topics(mongo_collection, name, topics):
    """
    this function will update the mongo_collection
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
