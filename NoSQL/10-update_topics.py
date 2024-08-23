#!/usr/bin/env python3
"""
This update all topics
and return nothing
"""

import pymongo


def update_topics(mongo_collection, name, topics):
    """
    This function takes a collection,
    a name(string) and a list of topics(string)
    to update
    """
    query_result = mongo_collection.update_many(
        {"name": name}, {"$set": {"topics": topics}}
        )
    return query_result
