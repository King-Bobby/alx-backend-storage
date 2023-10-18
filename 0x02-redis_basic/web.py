#!/usr/bin/env python3
"""
Module for task 5
"""


import requests
import redis
from typing import Dict


def get_page(url: str) -> str:
    """Initialize the Redis client"""
    redis_client = redis.Redis()

    # Key for tracking URL access count
    count_key = f"count:{url}"

    # Check if the count key exists in Redis
    if redis_client.exists(count_key):
        # If it exists, increment the count and get the current count
        count = redis_client.incr(count_key)
    else:
        # If it doesn't exist, create the count key and set it to 1
        redis_client.set(count_key, 1)
        count = 1

    # Check if the URL content is cached
    cached_content = redis_client.get(url)

    if cached_content is not None:
        # If cached content exists, return it
        return cached_content.decode("utf-8")

    # If the URL content is not cached, fetch it
    response = requests.get(url)

    if response.status_code == 200:
        # Cache the content with a 10-second expiration time
        redis_client.setex(url, 10, response.text)
        return response.text

    # If the request was unsuccessful, return an error message
    return f"Failed to retrieve content for URL: {url}"
