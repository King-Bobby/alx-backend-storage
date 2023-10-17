#!/usr/bin/env python3
"""
Module contains the function def insert_school(mongo_collection, **kwargs)
"""


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection based on kwargs"""
    new_document = kwargs
    document = mongo_collection.insert_one(new_document)
    return document.inserted_id
