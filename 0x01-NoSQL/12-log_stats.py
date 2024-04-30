#!/usr/bin/env python3
""" provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


def log_stats():
    """ Count number of logs with method=GET and path=/status"""

    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Count total number of logs
    total_logs = collection.count_documents({})
    print("{} logs".format(total_logs))

    # Count number of logs for each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    # Count number of logs with method=GET and path=/status
    status_check_count = collection.count_documents(
            {"method": "GET", "path": "/status"})
    print("{} status check".format(status_check_count))


if __name__ == "__main__":
    log_stats()
