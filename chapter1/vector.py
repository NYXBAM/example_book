from math import hypot

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y  

    def __repr__ (self):
        return f"Vector(%r, %r)" % (self.x, self.y)
    
    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))

    # or u can use simpless method 
    # def __bool_(self):
        # return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)



v1 = Vector(2, 4)
v2 = Vector(2, 1)
result = v1 + v2
print(result)  # Output: Vector(4, 5)

v3 = Vector(6, 8)

res = abs(v3)
print(res)  # Output: 10.0