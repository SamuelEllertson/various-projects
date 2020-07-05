#!/usr/bin/env python3

class cached:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        self.instance = instance
        return self

    def __call__(self, *args, **kwargs):
        cache = self.instance._cache

        if self.func not in cache:
            cache[self.func] = self.func(self.instance, *args, **kwargs)

        return cache[self.func]

    def __set_name__(self, owner, name):

        def clear_cache(instance):
            instance._cache.clear()

        owner._cache = getattr(owner, "_cache", {})

        owner.clear_cache = clear_cache

class Foo:
    def __init__(self, x):
        self.x = x

    @cached
    def length(self):
        print("called length")
        return self.x


