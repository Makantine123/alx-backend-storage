#!/usr/bin/env python3
"""
Module contains insert_school
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert function
    """
    return mongo_collection.insert(kwargs)
