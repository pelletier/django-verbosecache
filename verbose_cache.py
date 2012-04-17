"Verbose cache backend"

import functools
from pprint import pprint
from django.core.cache.backends.base import BaseCache

def verbose(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print "[CACHE] %s called with:" % f.__name__
        pprint(args)
        pprint(kwargs)
        res = f(*args, **kwargs)
        print "Output: %s" % res
        return res
    return wrapper

class VerboseCache(BaseCache):
    
    @verbose
    def __init__(self, host, *args, **kwargs):
        BaseCache.__init__(self, *args, **kwargs)

    @verbose
    def add(self, key, value, timeout=None, version=None):
        key = self.make_key(key, version=version)
        self.validate_key(key)
        return True

    @verbose
    def get(self, key, default=None, version=None):
        key = self.make_key(key, version=version)
        self.validate_key(key)
        return default

    @verbose
    def set(self, key, value, timeout=None, version=None):
        key = self.make_key(key, version=version)
        self.validate_key(key)

    @verbose
    def delete(self, key, version=None):
        key = self.make_key(key, version=version)
        self.validate_key(key)

    @verbose
    def get_many(self, keys, version=None):
        return {}

    @verbose
    def has_key(self, key, version=None):
        key = self.make_key(key, version=version)
        self.validate_key(key)
        return False

    @verbose
    def set_many(self, data, timeout=0, version=None):
        pass

    @verbose
    def delete_many(self, keys, version=None):
        pass

    @verbose
    def clear(self):
        pass

# For backwards compatibility
class CacheClass(VerboseCache):
    pass
