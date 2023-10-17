#!/usr/bin/env python3
"""
Module contains script that gives some stats about Nginx logs stored in MongoDB
"""


import pymongo


def log_stats(mongo_collection):
    """provides some stats about Nginx logs stored in MongoDB"""
    total_logs = mongo_collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_stats = {
            method: mongo_collection.count_documents({"method": method})
            for method in methods}
    specific_log_count = mongo_collection.count_documents(
            {"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_stats[method]}")
    print(f"{specific_log_count} status check")


if __name__ == "__main__":
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    collection = db['nginx']
    log_stats(collection)
