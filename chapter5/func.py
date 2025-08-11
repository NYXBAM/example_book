def factorial(n):
    '''returns n'''
    return 1 if n < 2 else n * factorial(n - 1)

print(factorial(333))
print(factorial.__doc__)

fact = factorial
print(fact(333))

fruits = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi']

print(sorted(fruits, key=len))

def reverce_string(s):
    '''Returns the reversed string'''
    return s[::-1]

print(sorted(fruits, key=reverce_string))

lmda = sorted(fruits, key=lambda s: s[::-1])
print(lmda)

# --------------- map -------------------- #

print(list(map(fact, range(10))))

examp = [fact(n) for n in range(10)]
print(examp)

print(list[map(fact, filter(lambda n: n % 2, range(10)))])

examp2 = [fact(n) for n in range(10) if n % 2]
print(examp2)

# --------------- reduce -------------------- # 
from functools import reduce
from operator import add

r = (reduce(add, range(1000)))
print(r)

# ---------------- class -------------------- #

import random 

class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)
    
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


bing = BingoCage(range(33235))
print(bing.pick())
print(callable(bing)) # it`s True

# -------------*params **params--------- #

def test_func(**par):
    print(par)

test_func(z=1, k=2, h=3, s=4, q=5)