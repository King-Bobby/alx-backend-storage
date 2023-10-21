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


def call_history(method: Callable) -> Callable:
    """ store the history of inputs and outputs for a particular function"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Get the qualified name of the method"""
        method_name = method.__qualname__

        # Create keys for inputs and outputs
        inputs_key = f"{method_name}:inputs"
        outputs_key = f"{method_name}:outputs"

        # Store input parameters as a string in Redis
        self._redis.rpush(inputs_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, output)
        return output


def replay(func: Callable):
    """ display the history of calls of a particular function."""
    method_name = func.__qualname__
    inputs_key = f"{method_name}:inputs"
    outputs_key = f"{method_name}:outputs"
    redis_instance = func.__self__._redis
    inputs = [
            eval(args_str)
            for args_str in self._redis.lrange(inputs_key, 0, -1)]
    outputs = self._redis.lrange(outputs_key, 0, -1)
    num_calls = len(inputs)

    print(f"{method_name} was called {num_calls} times:")
    for input_args, output in zip(inputs, outputs):
        print(f"{method_name}{input_args} -> {output}")


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
