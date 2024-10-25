#!/usr/bin/env python3
"""
lists all document in provided mongo collection
"""

import pymongo


def list_all(mongo_collection):
    """
    mongo_collection = mongo collection

    lists all documents
    """
    listy = []
    documents = mongo_collection.find()
    for document in documents:
        listy.append(document)
    return listy
