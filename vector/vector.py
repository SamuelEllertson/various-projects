#!/usr/bin/env python3

from collections.abc import MutableSequence
import operator
from reprlib import recursive_repr
import math
from itertools import repeat

def is_iterable(obj):
    try:
        iter(obj)
    except TypeError:
        return False
    else:
        return True

def make_iterable(obj):
    '''Objects which are not iterable will be made to be an iterable of itself'''

    if is_iterable(obj):
        return obj
    return repeat(obj)

class Vector(MutableSequence):

    __slots__ = ["values", "cache"]

    swizzles = {
        "x": 0,
        "y": 1,
        "z": 2,
        "w": 3,
        "r": 0,
        "g": 1,
        "b": 2,
        "a": 3
    }

    def __init__(self, *args):
        self.values = list(args)
        self.cache = {}

    @classmethod
    def from_iterable(cls, iterable):
        """Returns a new vector constructed from iterable

        >> Vector.from_iterable(range(5))
        Vector(0, 1, 2, 3, 4)
        >>> Vector.from_iterable([1,1,2,2])
        Vector(1, 1, 2, 2)
        """

        return cls(*iterable)

    @property
    def length(self):
        key = "length"
        if key in self.cache:
            return self.cache[key]

        self.cache[key] = math.hypot(*self)
    
        return self.cache[key]

    def dot(self, other):
        other = make_iterable(other)

        return sum(x * y for x, y in zip(self, other))

    def normalize(self):
        self /= self.length
        return self

    def get_normalized(self):
        return self / self.length

    def insert(self, *args, **kwargs):
        self.cache.clear()
        self.values.insert(*args, **kwargs)

    def apply_operator(self, other, opr, right=False, inplace=False):
        '''Takes an arbitrary object 'other' and an binary operator, applying the operator to components of self and 
        the object. If other is iterable, it is treated as a vector, otherwise it is coerced to be an iterable of itself.
        The operation can optionally be made act inplace, or for the operands to be reversed with the 'right' param'''

        other = make_iterable(other)

        opr_params = zip(other, self) if right else zip(self, other)

        new_values = (opr(x,y) for x,y in opr_params)

        if inplace:
            self.values = list(new_values)
            self.cache.clear()
            return self
        else:
            return self.from_iterable(new_values)

    def valid_swizzle(self, string):
        return all(char in self.swizzles for char in string)

    def __getattr__(self, attr):
        '''Provides ability to swizzle. 
        >>> vec = Vector(1,2,3)
        >>> vec.x
        Vector(1)
        >>> vec.xxyyzz
        Vector(1, 1, 2, 2, 3, 3)
        >>> vec.rgrgb
        Vector(1, 2, 1, 2, 3)
        '''

        if not self.valid_swizzle(attr):
            raise AttributeError(attr)
        
        return self.from_iterable(self[self.swizzles[char]] for char in attr)

    def __setattr__(self, attr, value):
        '''Provides ability to set values by swizzling.
        >>> vec = Vector(1,2,3)
        >>> vec.x = 10
        >>> vec
        Vector(10, 2, 3)
        >>> vec.yz = Vector(20,30)
        >>> vec
        Vector(10, 20, 30)
        >>> vec.rg = 100
        >>> vec
        Vector(100, 100, 30)
        >>> vec.gb = [50, 60]
        >>> vec
        Vector(100, 50, 60)
        '''

        #Regular attribute setting
        if not self.valid_swizzle(attr):
            return object.__setattr__(self, attr, value)

        iterable_values = make_iterable(value)

        for swiz_char, val in zip(attr, iterable_values):
            index = self.swizzles[swiz_char]
            self[index] = val

    def __delattr__(self, attr):
        '''Provides ability to delete by swizzle'''

        #Regular attribute deletion
        if not self.valid_swizzle(attr):
            return object.__delattr__(self, attr)

        for index in sorted(set(self.swizzles[swiz_char] for swiz_char in attr), reverse=True):
            del self[index]

    @recursive_repr()
    def __repr__(self):
        """Returns a string representation of the vector

        >>> repr(Vector(1,2,3))
        'Vector(1, 2, 3)'
        >>> repr(Vector())
        'Vector()'
        """

        return f"{self.__class__.__name__}({', '.join(repr(value) for value in self.values)})"

    def __getitem__(self, index):
        """Provides access to elements or slices of a vector

        >>> vec = Vector(1,2,3)
        >>> vec[0]
        1
        >>> vec[:2]
        Vector(1, 2)
        >>> vec[::-1]
        Vector(3, 2, 1)
        >>> vec[5]
        Traceback (most recent call last):
        IndexError: list index out of range
        """

        if isinstance(index, int):
            return self.values[index]

        return self.from_iterable(self.values[index])

    def __setitem__(self, index, value):
        """Sets elements or slices of a vector

        >>> vec = Vector(1,2,3)
        >>> vec[0] = 9
        >>> vec
        Vector(9, 2, 3)
        >>> vec[1:2] = [1,1,1,1,1]
        >>> vec
        Vector(9, 1, 1, 1, 1, 1, 3)
        >>> vec[:3] = Vector(1,2,3)
        >>> vec
        Vector(1, 2, 3, 1, 1, 1, 3)
        """
        self.cache.clear()

        self.values[index] = value

    def __delitem__(self, index):
        """deletes elements or slices of a vector

        >>> vec = Vector(1,2,3,4,5)
        >>> del vec[1]
        >>> vec
        Vector(1, 3, 4, 5)
        >>> del vec[1:3]
        >>> vec
        Vector(1, 5)
        """
        self.cache.clear()

        del self.values[index]

    def __len__(self):
        """Returns the number of elements in the vector

        >>> len(Vector(1,2,3))
        3
        >>> len(Vector())
        0
        """

        return len(self.values)

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.values == other.values
        return NotImplemented

    def __add__(self, other):
        return self.apply_operator(other, operator.add)

    def __sub__(self, other):
        return self.apply_operator(other, operator.sub)

    def __mul__(self, other):
        return self.apply_operator(other, operator.mul)
    
    def __truediv__(self, other):
        return self.apply_operator(other, operator.truediv)
    
    __radd__ = __add__

    __rmul__ = __mul__

    def __rsub__(self, other):
        return self.apply_operator(other, operator.sub, right=True)

    def __rtruediv__(self, other):
        return self.apply_operator(other, operator.truediv, right=True)

    def __iadd__(self, other):
        return self.apply_operator(other, operator.add, inplace=True)

    def __isub__(self, other):
        return self.apply_operator(other, operator.sub, inplace=True)

    def __imul__(self, other):
        return self.apply_operator(other, operator.mul, inplace=True)

    def __itruediv__(self, other):
        return self.apply_operator(other, operator.truediv, inplace=True)

    __matmul__ = __rmatmul__ = dot 

    def __neg__(self):
        return self.from_iterable(-x for x in self)

    def __pos__(self):
        return self

    def __bool__(self):
        return any(self)

    def __abs__(self):
        return self.length

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

