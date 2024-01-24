#!/usr/bin/env python3
""".11-schools_by_topic.py"""


def schools_by_topic(mongo_collection, topics):
    """find in a document in the MongoDB collection."""
    result = mongo_collection.find({"topics": topics})
    return result
