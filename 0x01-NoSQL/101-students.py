#!/usr/bin/env python3
"""
Module contains top_students function
"""


def top_students(mongo_collection):
    """
    Top students function
    """
    pipeline = [
        {
            '$unwind': '$topics'
        },
        {
            'group': {
                '_id': '$_id',
                'name': {'$first': '$name'},
                'averageScore': {'$avg': '$topics.score'}
            }
        },
        {
            '$sort': {'averageScore': -1}
        }
    ]

    result = list(mongo_collection.aggregate(pipeline))
    return result
