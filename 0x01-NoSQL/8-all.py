#!/usr/bin/env python3
"""
Module contains the function def list_all(mongo_collection)
"""


def list_all(mongo_collection):
    """lists all documents in a collection"""
    if mongo_collection is None:
        return []
    else:
        return [doc for doc in mongo_collection.find()]
