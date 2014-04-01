from django.core.cache import cache
from evelink import api
import time


class DjangoCache(api.APICache):

    def __init__(self):
        super(DjangoCache, self).__init__()
        self.cache = cache

    def put(self, key, value, duration):
        expiration = time.time() + duration
        self.cache.set(key, (value, expiration), duration)