from array import array
import reprlib
import math

class Vector:
    typecode = 'd'
    
    def __init__(self, components):
        self._components = array(self.typecode, components)
        
    def __iter__(self):
        return iter(self._components)
    
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
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))
    
    def __bool__(self):
        return bool(abs(self))
    
    def __len__(self):
        return len(self._components)
    
    def __getitem__(self, index):
        return self._components[index]
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
        
    
v1 = Vector([3, 4, 5])
print(len(v1)) # 3
print(v1[0], v1[-1]) # 3.0 5.0
v7 = Vector(range(7))
print(v7[1:4]) # array('d', [1.0, 2.0, 3.0])


# ------------------- itter ------------------- # 
print('*'*60)
print('\nItter:\n')
class MySeq:
    def __getitem__(self, index):
        return index
    
s = MySeq()
print(s[1], s[2], s[3]) # 1 2 3
print(s[1:4]) # slice(1, 4, None)
print(s[1:4:2]) # slice(1, 4, 2)
print(s[1:4:2, 9]) # (slice(1, 4, 2), 9)
print(s[1:4:2, 7:9]) # (slice(1, 4, 2), slice(7, 9, None))

# ------------------- slices  ------------------- # 

print('*'*60)
print('\slices:\n')



# class Vector:
#     # pass other code
#     def __len__(self):
#         return len(self._components)
    
#     def __getitem__(self, index):
#         return self._components[index]
    
v1 = Vector([3, 4, 5])
print(len(v1)) # 3 

v7 = Vector(range(7))
print(v7[1:4]) # array('d', [1.0, 2.0, 3.0])

class MySeq:
    def __getitem__(self, index):
        return index
    
s = MySeq()
print(s[1], s[2], s[3]) # 1 2 3
print(s[1:4]) # slice(1, 4, None)
print(s[1:4:2]) # slice(1, 4, 2)
print(s[1:4:2, 9]) # (slice(1, 4, 2), 9)
print(s[1:4:2, 7:9]) # (slice(1, 4, 2), slice(7, 9, None))
print(dir(slice))   # ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'indices', 'start', 'step', 'stop']
sl = slice(1, 4, 2)
print(sl.indices(1)) # (1, 4, 2)

print(slice(None, 10, 2).indices(5)) # (0, 5, 2)
print(slice(-3, None, None).indices(5)) # (2, 5, 1)

# ------------------- __getitem__ ------------------- #
print('*'*60)
print('\n__getitem__:\n')

import numbers
class Vector:
    typecode = 'd'
    
    def __init__(self, components):
        self._components = array(self.typecode, components)
        
    def __iter__(self):
        return iter(self._components)
    
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
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))
    
    def __bool__(self):
        return bool(abs(self))
    
    def __len__(self):
        return len(self._components)
    # new method with slices
    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = f'{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
        
v7 = Vector(range(7))
print(v7[-1]) # 6.0
print(v7[1:4]) # (1.0, 2.0, 3.0)
print(v7[-1:]) # (6.0,)
# print(v7[1,2]) # TypeError: Vector indices must be integers

# ------------- Vectors and dynamic attributes ------------- #
print('*'*60)
print('\nVectors and dynamic attributes:\n')

class Vector:
    typecode = 'd'
    shortcut_names = 'xyzt'
    
    def __init__(self, components):
        self._components = array(self.typecode, components)
        
    def __iter__(self):
        return iter(self._components)
    
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
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))
    
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
    
    # add new method to get attributes
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
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
    
    
    
v = Vector(range(10))

print(v.z) # 2.0
v.x = 10
print(v.x) # 10 
print(v) # (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0)