#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''

import requests
import redis
import time


def get_page(url: str) -> str:
    """ Initialize Redis connection"""
    r = redis.Redis()

    # Increment access count for the URL
    count_key = f"count:{url}"
    r.incr(count_key)

    # Get page content from cache if available
    page_key = f"page:{url}"
    cached_page = r.get(page_key)
    if cached_page:
        return cached_page.decode('utf-8')

    # If not cached, fetch page content from the web
    response = requests.get(url)
    page_content = response.text

    # Cache page content with expiration time of 10 seconds
    r.setex(page_key, 10, page_content)

    return page_content
