#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''

import requests
import redis
import time


def get_page(url: str) -> str:
    # Initialize Redis connection
    r = redis.Redis()

    # Track how many times the URL was accessed
    count_key = f"count:{url}"
    r.incr(count_key)

    # Get the HTML content from the URL
    response = requests.get(url)

    # Cache the result with an expiration time of 10 seconds
    cache_key = f"cache:{url}"
    r.setex(cache_key, 10, response.text)

    return response.text
