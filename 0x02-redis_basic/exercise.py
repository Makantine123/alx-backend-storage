#!/usr/bin/env python3
"""
Module contains Cache class
"""
import functools
import redis
import uuid
from typing import Callable, Union


def increment_call_count(self, method_name: str):
    if method_name in self.method_calls:
        self.method_calls[method_name] += 1
    else:
        self.method_calls[method_name] = 1


def count_calls(self, method: Callable) -> Callable:
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        method_name = method.__qualname__
        self.increment_call_count(method_name)
        return method(self, *args, **kwargs)
    return wrapper


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
        """"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, bytes]:
        """"""
        return self.get(key, fn=int)
