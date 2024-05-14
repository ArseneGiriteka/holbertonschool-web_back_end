#!/usr/bin/env python3
"""
find schools
"""


def schools_by_topic(mongo_collection, topic):
    """find schools by theirs topics"""
    return list(mongo_collection.find({"topics": {"$in": [topic]}}))
