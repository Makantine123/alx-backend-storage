#!/usr/bin/env python3
"""
Module contains schools_by_topic function
"""


def schools_by_topic(mongo_collection, topics):
    """
    School function
    """
    return mongo_collection.find({'topics': topics})
