#!/usr/bin/env python3
"""
this is a script to list all
"""

import pymongo


def list_all(mongo_collection):
    """
    to list every single docs
    none if it doesn't exist
    """
    return list(mongo_collection.find())
