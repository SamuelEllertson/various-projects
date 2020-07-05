#!/usr/bin/env python3
import builtins
import itertools as it
from functools import reduce

class Chainer:

    modules_to_search = [builtins, it]
    cache = {"reduce": reduce}

    params_first = {map, filter, reduce, it.dropwhile, it.filterfalse, it.starmap, it.takewhile}
    only_params = {range,input, it.count}

    def __init__(self, value=None):
        self._value = value

        self._opr = None
        self.is_method = False
        self.called = False

    def __getattr__(self, attr):

        self.ensure_called()

        if attr.startswith("_"):
            self.is_method = True
            self.opr = getattr(self.value, attr[1:])
            return self
        else:
            self.is_method = False

        if attr in self.cache:
            self.opr = self.cache[attr]
            return self

        for module in self.modules_to_search:
            if hasattr(module, attr):
                self.opr = getattr(module, attr)
                self.cache[attr] = self.opr
                break
        else:
            raise AttributeError(f"Could not resolve attribute '{attr}'")

        return self

    def __call__(self, *args, **kwargs):
        self.called = True

        if self.opr in self.params_first:
            self.value = self.opr(*args, self.value, **kwargs)
        elif self.opr in self.only_params or self.is_method:
            self.value = self.opr(*args, **kwargs)
        else:
            self.value = self.opr(self.value, *args, **kwargs)
        
        return self

    def __iter__(self):
        return iter(self.value)

    def apply(self, func):
        self.opr = func
        return self

    @property
    def value(self):
        self.ensure_called()

        return self._value

    @value.setter
    def value(self, val):
        self.ensure_called()

        self._value = val

    @property
    def opr(self):
        return self._opr

    @opr.setter
    def opr(self, value):
        self.ensure_called()

        self._opr = value
        self.called = False
    
    def ensure_called(self):
        if self._opr is not None and not self.called:
            self()

    @classmethod
    def register_module(cls, module):
        cls.modules_to_search.append(module)

    @classmethod
    def register_function(cls, function, params_first=False, only_params=False):
        cls.cache[function.__name__] = function

        if params_first:
            cls.params_first.add(function)
        elif only_params:
            cls.only_params.add(function)

import random

Chainer.register_module(random)


a = Chainer().range(5,1,-1).set.sorted.map(lambda x: x ** 2).enumerate.dict
#a = Chainer().range(1,10).choices(k=3)
#a = Chainer("abc")._upper.map(ord).list.choices(k=4).set.sorted.enumerate.dict
print(a.value)
