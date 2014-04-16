from django.core.cache import cache
from django.db import models
from evelink import api
import time
from functools import wraps


class DjangoCache(api.APICache):

    def __init__(self):
        super(DjangoCache, self).__init__()
        self.cache = cache

    def put(self, key, value, duration):
        expiration = time.time() + duration
        self.cache.set(key, (value, expiration), duration)


class GetOrNoneManager(models.Manager):
    """Adds get_or_none method to objects
    """

    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            # TODO: Sort out logging
            #logger.warn('No %s matching kwargs %s' % (self.model._meta
            # .verbose_name, kwargs))
            return None


def cache_method(cache_key, timeout=300):
    def cache_it(func):
        @wraps(func)
        def with_cache(self, *args, **kwargs):
            cached = cache.get(cache_key)
            if cached is not None:
                return cached
            value = func(*args, **kwargs)
            cache.set(cache_key, value, timeout)
            return value
        return with_cache
    return cache_it