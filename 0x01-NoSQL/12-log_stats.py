#!/usr/bin/python3
"""
    12-log_stas.py
    Python script that provides some stats about Nginx logs stored in MongoDB
"""
import pymongo

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
db = mongo_client.logs
collection = db.nginx

total_logs = collection.count_documents({})

print(f"{total_logs} logs")

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
print("Methods:")
for method in methods:
    count = collection.count_documents({"method": method})
    print(f"\tmethod {method}: {count}")

specific_log_count = collection.count_documents(
    {"method": "GET", "path": "/status"})
print(f"{specific_log_count} status check")
