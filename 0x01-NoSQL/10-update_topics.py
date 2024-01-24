#!/usr/bin/env python3
""".10-update_topics"""


def update_topics(mongo_collection, name, topics):
    """update a document in the MongoDB collection."""
    result = mongo_collection.update_many(
        {"name": name}, {"$set": {"topics": topics}})
    return result.matched_count, result.modified_count
