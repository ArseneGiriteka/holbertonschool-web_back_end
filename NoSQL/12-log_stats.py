#!/usr/bin/env python3
""" Provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print(f"{logs_collection.count_documents({})} logs")

    print("Methods:")
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check_count = logs_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")
