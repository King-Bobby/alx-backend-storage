#!/usr/bin/env python3
"""
Module contains def top_students(mongo_collection)
"""


def top_students(mongo_collection):
    """ returns all students sorted by average score"""
    Students = mongo_collection.aggregate(
        [{"$project": {
            "-id": 1,
            "name": 1,
            "averageScore": {
                "$avg": {"$avg": "$topics.score"}},
            "topics": 1
        }},
         {"$sort": {"averageScore": -1}}]
        )
    return Students
