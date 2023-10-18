#!/usr/bin/env python3
"""
Module contains class Cache
"""


import redis
import uuid
from typing import Union


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
