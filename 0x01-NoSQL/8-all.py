#!/usr/bin/env python3
"""
Module list_all function
"""


def list_all(mongo_collection):
    """
    Function takes in mongo_collection argument which represent
    a pymongo collection object
    """
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents
