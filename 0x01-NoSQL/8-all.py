#!/usr/bin/env python3
""".8-all"""


def list_all(mongo_collection):
    """List all documents in the MongoDB collection."""
    documents = list(mongo_collection.find({}))
    return documents
