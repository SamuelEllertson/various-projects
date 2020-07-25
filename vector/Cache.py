#!/usr/bin/env python3

from functools import wraps

class Cached:

    def clear_cache(self):
        getattr(self, "_Cache", {}).clear()

    @classmethod
    def method(cls, method):
        
        @wraps(method)
        def wrapper(instance, *args, **kwargs):
            #Ensure cache exists
            instance._Cache = getattr(instance, "_Cache", {})

            cache = instance._Cache

            #Ensure value exists
            if method not in cache:
                cache[method] = method(instance, *args, **kwargs)

            return cache[method]

        return wrapper

    @classmethod
    def property(cls, method):
        return property(cls.method(method))

    @classmethod
    def invalidate(cls, method):

        @wraps(method)
        def wrapper(instance, *args, **kwargs):
            instance.clear_cache()
            return method(instance, *args, **kwargs)

        return wrapper
