#!/usr/bin/env python3
"""
Module contains Cache class
"""
import redis
import uuid
from typing import Callable, Union


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

    def get(self,
            key: str,
            fn: Callable = None):
        """Retrieves a value from Redis data storage"""
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> Union[str, bytes]:
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, bytes]:
        return self.get(key, fn=int)
