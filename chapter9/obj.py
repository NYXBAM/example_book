

from array import array
import math

class Vector2d:
    typecode = 'd'
    
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)
    @property    
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
    
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + 
                bytes(array(self.typecode, self)))
        
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self)) 
    
    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)
    
    def angle(self):
        return math.atan2(self.y, self.x)
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)
    
    
v1 = Vector2d(3, 4)
print(v1.x, v1.y) # 3.0 4.0
x, y = v1
print(x, y) # 3.0 4.0
print(repr(v1)) # Vector2d(3.0, 4.0)
v1_clone = eval(repr(v1))
print(v1 == v1_clone) # True

octets = bytes(v1)
print(octets) # b'd\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@'
print(abs(v1)) # 5.0 # 
print(bool(v1), bool(Vector2d(0, 0))) # True False

# --------------------- classmethod --------------------- # 
print("*"*40)
print('\n\n@classmethod\n')


class Demo:
    @classmethod
    def klassmeth(*args):
        return args
    @staticmethod
    def statmeth(*args):
        return args
    
    
print(Demo.klassmeth()) # (<class '__main__.Demo'>,)
print(Demo.klassmeth('spam')) # (<class '__main__.Demo'>, 'spam')
print(Demo.statmeth()) # ()
print(Demo.statmeth('spam')) # ('spam',)

# --------------------- format --------------------- # 
# Some examples and small sheets formating showed in format_sheet.py
print("*"*40)
print('\noutput format \n')

brl = 1/2.43 #

print(format(brl, '0.4f')) # 0.4115
print('1 BRT = {rate:0.2f} USD'.format(rate=brl))

v1 = Vector2d(3, 6)
print(format(v1)) # (3.0, 6.0)
print(format(v1, '.2f')) # (3.00, 6.00)
print(format(v1, '.3e')) # (3.000e+00, 6.000e+00)
# using 'p' to switch to polar coordinates
print(format(Vector2d(1, 1), 'p')) # <1.4142135623730951, 0.7853981633974483>
print(format(Vector2d(1, 1), '.3ep')) # <1.414e+00, 7.854e-01>
print(format(Vector2d(1, 1), '0.5fp')) # <1.41421, 0.78540>


v1 = Vector2d(3, 4)
v2 = Vector2d(3.1, 4.2)
print(hash(v1), hash(v2)) #7 384307168202284039



# --------------------- full class --------------------- #
print("*"*40)
print('\nfull class \n')
print('Vector2d_v3.py')

class Vector2d:
    typecode = 'd'
    
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)
    @property    
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
    
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + 
                bytes(array(self.typecode, self)))
        
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self)) 
    
    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)
    
    def angle(self):
        return math.atan2(self.y, self.x)
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)
    
    
v1 = Vector2d(3, 4)
print(v1.x, v1.y) # 3.0 4.0
x, y = v1
print(x, y) # 3.0 4.0
print(v1) # (3.0, 4.0)

v1_clone = eval(repr(v1))

print(v1 == v1_clone) # True
octets = bytes(v1)
print(octets) # b'd\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@'
print(abs(v1)) # 5.0 

print(bool(v1), bool(Vector2d(0, 0))) # True False

# Test of ``.frombytes()`` class method:
v1_clone = Vector2d.frombytes(bytes(v1))
print(v1 == v1_clone) # True

# ---------------------- name mangling ---------------------- # 
print("*"*40)
print('\nname mangling \n')
v1 = Vector2d(3, 4)
print(v1.__dict__) # {'_Vector2d__x': 3.0, '_Vector2d__y': 4.0}

# ---------------------- __slots__ ---------------------- # 
print("*"*40)
print('\n__slots__ \n')
# u can see how i used slots in practice here: 
# https://github.com/NYXBAM/CryptoWhaleMonitor/blob/master/models/dataclass.py

class Vector2d:
    __slots__ = ('__x', '__y')
    typecode = 'd'
    # other methods are the same as above
    
    
# if u need to add some dynamic attribute use this:
class Vector2d:
    __slots__ = ('__x', '__y', '__dict__', '__weakref__') # __weakref__ and  __dict__ 
    typecode = 'd'
    # other methods are the same as above


class Vector2d:
    typecode = 'd'
    
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)
    @property    
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
    
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + 
                bytes(array(self.typecode, self)))
        
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self)) 
    
    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)
    
    def angle(self):
        return math.atan2(self.y, self.x)
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)
   
   
v1 = Vector2d(1.1, 2.2)
dumpd = bytes(v1)
print(dumpd)  # b'd\x9a\x99\x99\x99\x99\x99\xf1?\x9a\x99\x99\x99\x99\x99\x01@'
v1.typecode = 'f' # change typecode for this instance only
dumpf = bytes(v1)
print(dumpf) # b'f\xcd\xcc\x8c?\xcd\xcc\x0c@'
print(len(dumpd), len(dumpf)) # 17 9
print(Vector2d.typecode) # d

class ShortVector2d(Vector2d):
    typecode = 'f'
    
sv = ShortVector2d(1/11, 1/27)
print(sv) # (0.09090909090909091, 0.037037037037037035)
print(len(bytes(sv))) # 9 
