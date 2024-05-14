#!/usr/bin/env python3
"""
this module list all documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """list all documents in a collection"""
    return list(mongo_collection.find())
