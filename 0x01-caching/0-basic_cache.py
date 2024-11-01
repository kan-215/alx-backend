#!/usr/bin/python3
"""Basic Cache implementation Class
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    the clss implements a basic cache 

    Attributes:
        MAX_ITEMS: total items that can be stored in the cache
    """
    def put(self, key, item):
        """ Adds an item into the cache
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """ Gets an item by key
        """
        return self.cache_data.get(key, None)
