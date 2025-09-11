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