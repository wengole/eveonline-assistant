import hashlib
import time
from functools import wraps

from django.core.cache import cache
from django.db import models
from evelink import api


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


def cacheable(cache_key, timeout=3600):
    def paramed_decorator(func):
        @wraps(func)
        def decorated(self, *args, **kwargs):
            format_kwargs = kwargs.copy()
            format_kwargs.update(self.__dict__)
            md5 = hashlib.md5()
            md5.update(cache_key.format(**format_kwargs).encode('utf-8'))
            key = md5.hexdigest()
            res = cache.get(key)
            if res is None:
                res = func(self, *args, **kwargs)
                cache.set(key, res, timeout)
            return res
        decorated.__doc__ = func.__doc__
        decorated.__dict__ = func.__dict__
        return decorated
    return paramed_decorator