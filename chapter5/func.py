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

 # ------------------- sig -------------------- # 

from inspect import signature

sig = signature(reverce_string)
print(sig) # <Signature (s)>

sign = signature(factorial)

my_sig = {3}
bound_args = sig.bind(*my_sig)
print(bound_args)  # BoundArguments(args=(3,), kwargs={})


# ---------------------- annotations -------------------- #

def clip(text: str, max_len: 'int > 0' = 80) -> str:
    '''Return text clipped to a maximum length'''
    if len(text) > max_len:
        return text[:max_len]
    return text

print(clip.__annotations__)  # {'text': <class 'str'>, 'max_len': 'int > 0', 'return': <class 'str'>}

# ---------------------- operator ------------------------- #
from functools import reduce
from operator import mul

def fact(n):
    return reduce(mul, range(1, n+1))

print(fact(5))  # 120

metro_data = [
    ('Tokyo', 'JPN', 36.933, (35.689722, 139.691667)),
    ('Delhi', 'IND', 21.935, (28.613889, 77.208889)),
    ('Mexico-city', 'MEX', 20.142, (19.428056, -99.133333)),
    ('New York', 'USA', 8.336, (40.712778, -74.005833)),
    ('Sao Paulo', 'BRA', 10.992, (-23.547778, -46.635833)),
    ('Mumbai', 'IND', 12.442, (19.076111, 72.877778)),
    ('Shanghai', 'CHN', 24.150, (31.222222, 121.458056)),
]

from operator import itemgetter
for city in sorted(metro_data, key=itemgetter(3)):
    print(city)

cc_name = itemgetter(1, 0)
for city in metro_data:
    print(cc_name(city))  # ('JPN', 'Tokyo'), ('IND', 'Delhi'), ...



# ----------------------------------------------------- #

from collections import namedtuple
LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))
               for name, cc, pop, (lat, long) in metro_data]
print(metro_areas[0])
print(metro_areas[0].coord.lat)  # 36.933

from operator import attrgetter

name_lat = attrgetter('name', 'coord.lat')
for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))  # ('Tokyo', 35.689722), ('Delhi', 28.613889), ...


# ----------------------------------------------------------- #
from operator import methodcaller

s = 'The time has come'
upcase = methodcaller('upper')
print(upcase(s))  # THE TIME HAS COME
print(str.upper(s))  # THE TIME HAS COME
hiphenate = methodcaller('replace', ' ', '-')
print(hiphenate(s))  # The-time-has-come
