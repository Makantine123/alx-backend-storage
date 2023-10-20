#!/usr/bin/env python3
"""
Module contains update_topics function
"""


def update_topics(mongo_collection, name, topics):
    """
    Update function
    """
    query = {'name': name}
    new_value = {'$set': {'topics': topics}}
    mongo_collection.update_many(query, new_value)
