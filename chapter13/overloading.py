from array import array
import reprlib
import numbers
import functools
import operator
import math
import itertools
from collections import Counter

# repr unary operators
class Vector:
    typecode = 'd'
    
    def __init__(self, components):
        self._components = array(self.typecode, components)
        
    def __iter__(self):
        return iter(self._components)

    def __add__(self, other):
        pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        return Vector(a + b for a, b in pairs)
     # unary operators
    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))
    
    # unary operators
    def __neg__(self):
        return Vector(-x for x in self)
    
    # unary operators
    def __pos__(self):
        return Vector(self)
    
    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return f'Vector({components})'
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))
    
    def __eq__(self, other):
        return (len(self)) == len(other) and all(a == b for a, b in zip(self, other))
    
    def __bool__(self):
        return bool(abs(self))
    
    def __len__(self):
        return len(self._components)
    
    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = f'{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))
    
    def __hash__(self):
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes, 0)
    
    shortcut_names = 'xyzt'
    
    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
            
        msg = f'{cls.__name__!r} object has no attribute {name!r}'
        raise AttributeError(msg)
    
    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = f'readonly attribute {name!r}'
            elif name.islower():
                error = f"can't set attributes 'a' to 'z' in {cls.__name__!r}"
            else:
                error = ''
            if error:
                raise AttributeError(error)
        super().__setattr__(name, value)
    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n - 1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a
    
    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))
    
    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)],
                                     self.angles())
            outer_fmt = '<()>'
        else:
            coords = self
            outer_fmt = '({})'
        componetns = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(componetns))
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)



# When x != +x 

import decimal 
ctx = decimal.getcontext()
ctx.prec = 40
one_third = decimal.Decimal('1')/ decimal.Decimal('3')
print(one_third)  # 0.3333333333333333333333333333333333333333
print(one_third == +one_third) # True
ctx.prec = 28
print(one_third == +one_third) # False
print(+one_third) # 0.3333333333333333333333333333

ct = Counter('abracadabra')
print(ct) # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
ct['r'] = - 3 
ct['d'] = 0 
print(ct) # Counter({'a': 5, 'b': 2, 'c': 1, 'd': 0, 'r': -3})


# Vector and overloading 
v1 = Vector([3, 4, 5])
v2 = Vector([6, 7, 8])
print(v1 + v2) # (9.0, 11.0, 13.0)
print(v1 + v2 == Vector([3+6, 4+7, 5+8])) # True
v1 = Vector([3, 4, 5, 6])
v3 = Vector([1, 2])
print(v1 + v3) # (4.0, 6.0, 5.0, 6.0)

v1 = Vector([3, 4, 5]) 
print(v1 + (10, 20, 30))  # (13.0, 24.0, 35.0)

