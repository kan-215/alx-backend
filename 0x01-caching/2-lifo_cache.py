#!/usr/bin/python3
"""LIFO caching
"""
from threading import RLock

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO cache implementation(Last in first out)

    Attributes:
        __keys (list): Stores cache keys according to entry using `.append`
        __rlock (RLock): Locks accessed resources to prevent race condition
    """
    def __init__(self):
        """ instance method
        """
        super().__init__()
        self.__keys = []
        self.__rlock = RLock()

    def put(self, key, item):
        """ Adds an item in the cache
        """
        if key is not None and item is not None:
            keyOut = self._balance(key)
            with self.__rlock:
                self.cache_data.update({key: item})
            if keyOut is not None:
                print('DISCARD: {}'.format(keyOut))

    def get(self, key):
        """ Gets an item by key
        """
        with self.__rlock:
            return self.cache_data.get(key, None)

    def _balance(self, keyIn):
        """ Removes the earliest item from the cache at MAX size
        """
        keyOut = None
        with self.__rlock:
            keysLength = len(self.__keys)
            if keyIn not in self.__keys:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    keyOut = self.__keys.pop(keysLength - 1)
                    self.cache_data.pop(keyOut)
            else:
                self.__keys.remove(keyIn)
            self.__keys.insert(keysLength, keyIn)
        return keyOut
