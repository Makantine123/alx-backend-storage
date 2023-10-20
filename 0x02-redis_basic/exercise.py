#!/usr/bin/env python3
"""
Module contains Cache class
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class, stores an instance of the Redis client
    """

    def __init__(self) -> None:
        """Initialisation of class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store method"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key