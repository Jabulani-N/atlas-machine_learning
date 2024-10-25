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
    for document in mongo_collection:
        listy.append(document)
    return listy
