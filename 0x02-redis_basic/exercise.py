#!/usr/bin/env python3
"""
Module contains class Cache
"""


import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Counts how many times a methos is called"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Implements the method after increasing its call count"""
        method_name = method.__qualname__
        count_key = f"count:{method_name}"
        self._redis.incr(count_key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Contains the method store"""
    def __init__(self):
        """Initialize the Redis client and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generate a random key and Store input data in Redis using random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """Check if the key exists in Redis"""
        if self._redis.exists(key):
            data = self._redis.get(key)
            if fn is not None:
                return fn(data)
            return data
        return None

    def get_str(self, key: str) -> Union[str, None]:
        """converts ouput to str"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """Converts output to int"""
        return self.get(key, fn=int)
