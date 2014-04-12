from django.core.cache import cache
from django.db import models
from evelink import api
import time


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