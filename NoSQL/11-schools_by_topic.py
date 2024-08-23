#!/usr/bin/env python3
"""
this module host a function called
def schools_by_topic(mongo_collection, topic):
"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    this function find a list of docs having
    a specific topic and return that list
    """
    schools = mongo_collection.find({"topics": topic})
    return schools
