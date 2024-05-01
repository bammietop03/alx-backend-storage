#!/usr/bin/env python3
"""Create a Cache class. In the __init__ method, store an instance of the
Redis client as a private variable named _redis (using redis.Redis()) and
flush the instance using flushdb"""

import redis
import uuid
from typing import Union


class Cache:
    """A cache class"""
    def __init__(self):
        """Create an instance of redis and flush it"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """A store class and generates a key and set it to the argument data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int]:
        """ get a value of a specific key with callable function added """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, bytes]:
        """ Converts btye to str """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """ Convert byte to int """
        return self.get(key, fn=int)
