#!/usr/bin/env python3
""" adding the top 10 of the most present IPs in the collection
nginx of the database logs """
from pymongo import MongoClient


def log_stats():
    """ Count number of logs with method=GET and path=/status"""
    # Connect to MongoDB
    client = MongoClient()
    db = client.logscollection = db.nginx

    # Count total number of logs
    total_logs = collection.count_documents({})
    print("{} logs".format(total_logs))

    # Count number of logs for each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    # Count number of logs with method=GET and path=/status
    status_check_count = collection.count_documents(
            {"method": "GET", "path": "/status"})
    print("{} status check".format(status_check_count))

    # Calculate top 10 most present IPs
    top_ips_pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = collection.aggregate(top_ips_pipeline)

    # Print top IPs
    print("IPs:")
    for ip in top_ips:
        print("\t{}: {}".format(ip["_id"], ip["count"]))


if __name__ == "__main__":
    log_stats()
