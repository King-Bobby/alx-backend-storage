#!/usr/bin/env python3
"""
Module contains function def update_topics(mongo_collection, name, topics)
"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document based on the name"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
