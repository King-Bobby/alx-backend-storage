#!/usr/bin/env python3
"""
Module contains def schools_by_topic(mongo_collection, topic)
"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    query = {"topics": {"$elemMatch": {"$eq": topic}}}
    return [doc for doc in mongo_collection.find(query)]
