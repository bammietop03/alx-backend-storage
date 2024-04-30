#!/usr/bin/env python3
""" provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


if __name__ == "__main__":
    """ Count number of logs with method=GET and path=/status"""

    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Count total number of logs
    total_logs = collection.count_documents({})
    print(f'{total_logs} logs')

    # Count number of logs for each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    # Count number of logs with method=GET and path=/status
    status_check_count = collection.count_documents(
            {"method": "GET", "path": "/status"})

    print(f'{status_check} status check')
