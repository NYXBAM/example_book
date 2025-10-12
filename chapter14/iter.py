from abc import abstractmethod
import re 
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
        
    def __getitem__(self, index):
        return self.words[index]
    
    def __len__(self):
        return len(self.words)
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
s = Sentence('"The time has come," the Walrus said,')
print(s) # Sentence('"The time ha... Walrus said,')

for word in s:
    print(word)

print(list(s)) # ['The', 'time', 'has', 'come', 'the', 'Walrus', 'said']
print(s[0]) # The

class Foo:
    def __iter__(self):
        pass

from collections import abc
print(issubclass(Foo, abc.Iterable)) # True 
f = Foo()
print(isinstance(f, abc.Iterable)) # True 

# Simple example for iter string 
s = 'ABC'
for char in s: 
    print(char)
# A
# B
# C

# Without for, using while True 
s = 'ABC'
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break

class Iterator(abc.Iterable):
    """code from Lib/_collections_abc.py"""
    __slots_ = ()
    
    @abstractmethod
    def __next__(self):
        raise StopIteration
    
    def __iter__(self):
        return self
    
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterator:
            if (any("__next__" in B.__dict__ for B in C.__mro__) and any("__iter__" in B.__dict__ for B in C.__mro__)):
                return True
        return NotImplemented
    
    
s3 = Sentence('Pig and Pepper')
it = iter(s3)
print(it) # <iterator object at 0x101a799f0>
print(next(it)) # Pig
print(next(it)) # and
print(next(it)) # Pepper 
# print(next(it))   # StopIteration
print(list(it)) # []


RE_WORD = re.compile('\w+')

class Sentence2:
    
    def __init__(self, text):
        self.text = text 
        self.words = RE_WORD.findall(text)
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        return SentenceIterator(self.words)
    
class SentenceIterator:
    
    def __init__(self, words):
        self.words = words
        self.index = 0
        
    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word
    
    def __iter__(self):
        return self
    
    
    # Class sentence num 3 
    
    RE_WORD = re.compile('\w+')
    
class Sentence3:  
     def __init__(self, text):
         self.text = text 
         self.words = RE_WORD.findall(text)
         
     def __repr__(self):
         return 'Sentence(%s)' % reprlib.repr(self.text)
     
     def __iter__(self):
         for word in self.words:
             yield word
         return
        
# generators 

def gen_123():
    yield 1
    yield 2
    yield 3
    
print(gen_123) # <function gen_123 at 0x101a7a0d0>

for i in gen_123():
    print(i) # 1 2 3 
    
g = gen_123()
print(next(g)) # 1
print(next(g)) # 2
print(next(g)) # 3 
# print(next(g)) # StopIteration

def gen_AB():
    print('start')
    yield "A"
    print('continue')
    yield "B"
    print('end')
    
for c in gen_AB():
    print('->', c)
    # start
    # -> A
    # continue
    # -> B
    # end

    
# Lazy version of Sentence class 
# Sentence4

import re 
import reprlib

RE_WORD = re.compile('\w+')

class Sentence4:
    
    def __init__(self, text):
        self.text = text
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()
            
            
# Trying number 5 using generator expression
# Sentence5


def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')
    
res1 = [x*3 for x in gen_AB()]
print(res1)
for i in res1:
    print('-->', i)
    
res2 = (x*3 for x in gen_AB())
print(res2) # <generator object <genexpr> at 0x1104d5f20>

# Then we can create Sentence5 with generator expression

import re 
import reprlib

RE_WORD = re.compile('\w+')

class Sentence5: 
        def __init__(self, text):
            self.text = text
        
        def __repr__(self):
            return 'Sentence(%s)' % reprlib.repr(self.text)
        
        def __iter__(self):
            """Here we use generator expression"""
            return (match.group() for match in RE_WORD.finditer(self.text))
        
# Arithmetic progression iterator

class ArithmeticProgression:
    
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end
        
    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None 
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index



ap = ArithmeticProgression(0, 1, 3)
print(list(ap)) # [0, 1, 2]

ap = ArithmeticProgression(1, .5, 3)
print(list(ap)) # [1.0, 1.5, 2.0, 2.5]

ap = ArithmeticProgression(0, 1/3, 1)
print(list(ap)) # [0.0, 0.3333333333333333, 0.6666666666666666]

from fractions import Fraction
ap = ArithmeticProgression(0, Fraction(1, 3), 1)
print(list(ap)) #  [Fraction(0, 1), Fraction(1, 3), Fraction(2, 3)]

from decimal import Decimal
ap = ArithmeticProgression(0, Decimal('.1'), .3)
print(list(ap)) # [Decimal('0'), Decimal('0.1'), Decimal('0.2')]


# generator function aritprog_gen

def aritprog_gen(begin, step, end=None):
    result = type(begin + step) (begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index


# Using itertools
import itertools

gen = itertools.count(1, .5)

print(next(gen)) # 1
print(next(gen)) # 1.5
print(next(gen)) # 2.0
print(next(gen)) # 2.5

gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
print(list(gen)) # [1, 1.5, 2.0, 2.5]

# then using takewhile, we create new 
# function aritprog_gen

def aritropgen_gen(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    
    return ap_gen



def vowel(c):
    return c.lower() in "aeiou"

print(list(filter(vowel, "Aardvark"))) # ['A', 'a', 'a']
# itertools func 
import itertools
print(list(itertools.filterfalse(vowel, "Aardvark"))) # ['r', 'd', 'v', 'r', 'k']
print(list(itertools.dropwhile(vowel, "Aardvark"))) # ['r', 'd', 'v', 'r', 'k']
print(list(itertools.takewhile(vowel, "Aardvark"))) # ['A', 'a']
print(list(itertools.compress("Aardvark", (1,0,1,1,0,1)))) # ['A', 'r', 'd', 'a']
print(list(itertools.islice("Aardvark", 4))) # ['A', 'a', 'r', 'd']
print(list(itertools.islice("Aardvark", 4, 7))) # ['v', 'a', 'r']
print(list(itertools.islice("Aardvark", 1, 7, 2))) # ['a', 'd', 'a']



sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]

import itertools
print(list(itertools.accumulate(sample))) # 5, 9, 11, 19, 26, 32, 35, 35, 44, 45]
print(list(itertools.accumulate(sample, min))) # [5, 4, 2, 2, 2, 2, 2, 0, 0, 0]
print(list(itertools.accumulate(sample, max))) # [5, 5, 5, 8, 8, 8, 8, 8, 9, 9]
import operator
print(list(itertools.accumulate(sample, operator.mul))) # [5, 20, 40, 320, 2240, 13440, 40320, 0, 0, 0]
print(list(itertools.accumulate(range(1, 15), operator.mul))) # [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200] !FACTORIAL! 
print(list(enumerate('albatroz', 1))) # [(1, 'a'), (2, 'l'), (3, 'b'), (4, 'a'), (5, 't'), (6, 'r'), (7, 'o'), (8, 'z')]

import operator
print(list(map(operator.mul, range(11), range(11)))) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(list(map(operator.mul, range(11), [2,4,8])))  # [0, 4, 16]
print(list(map(lambda a, b: (a, b), range(11), [2,4,8]))) # [(0, 2), (1, 4), (2, 8)]
print(list(itertools.starmap(operator.mul, enumerate('albatroz', 1)))) # ['a', 'll', 'bbb', 'aaaa', 'ttttt', 'rrrrrr', 'ooooooo', 'zzzzzzzz']
sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
print(list(itertools.starmap(lambda a, b: b/a, 
                             enumerate(itertools.accumulate(sample), 1)))) # [5.0, 4.5, 3.6666666666666665, 4.75, 5.2, 5.333333333333333, 5.0, 4.375, 4.888888888888889, 4.5]

print(list(itertools.chain('ABC', range(2)))) # ['A', 'B', 'C', 0, 1]
print(list(itertools.chain(enumerate('ABC'))))  # [(0, 'A'), (1, 'B'), (2, 'C')]
print(list(itertools.chain.from_iterable(enumerate('ABC')))) # [0, 'A', 1, 'B', 2, 'C']
print(list(zip('ABC', range(5)))) # [('A', 0), ('B', 1), ('C', 2)]
print(list(zip('ABC', range(5), [10, 20, 30, 40]))) # [('A', 0, 10), ('B', 1, 20), ('C', 2, 30)]
print(list(itertools.zip_longest('ABC', range(5), fillvalue='?')))

# itertools product 

print(list(itertools.product('ABC', range(2)))) # [('A', 0), ('A', 1), ('B', 0), ('B', 1), ('C', 0), ('C', 1)]

suits = 'spades hearts diamonds clubs'.split()
print(list(itertools.product('AK', suits))) # [('A', 'spades'), ('A', 'hearts'), ('A', 'diamonds'), ('A', 'clubs'), ('K', 'spades'), ('K', 'hearts'), ('K', 'diamonds'), ('K', 'clubs')]
print(list(itertools.product('ABC', repeat=2))) #[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

print(list(itertools.product(range(2), repeat=3))) # [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
rows = itertools.product('AB', range(2), repeat=2)
for row in rows: print(row)
"""
    ('A', 0, 'A', 0)
    ('A', 0, 'A', 1)
    ('A', 0, 'B', 0)
    ('A', 0, 'B', 1)
    ('A', 1, 'A', 0)
    ('A', 1, 'A', 1)
    ('A', 1, 'B', 0)
    ('A', 1, 'B', 1)
    ('B', 0, 'A', 0)
    ('B', 0, 'A', 1)
    ('B', 0, 'B', 0)
    ('B', 0, 'B', 1)
    ('B', 1, 'A', 0)
    ('B', 1, 'A', 1)
    ('B', 1, 'B', 0)
    ('B', 1, 'B', 1)
"""

 # combinations
 # combinations_with_replacement
 # count 
 # cycle 
 # permutations
 # repeat

ct = itertools.count()
print(next(ct)) # 0
print(next(ct)) # 1

print(list(itertools.islice(itertools.count(1, .3), 3))) # [1, 1.3, 1.6]
cy = itertools.cycle('ABC')
print(next(cy)) # A

print(list(itertools.islice(cy, 7))) # ['B', 'C', 'A', 'B', 'C', 'A', 'B']
rp = itertools.repeat(7)
print(next(rp)) # 7
print(next(rp)) # 7
print(list(itertools.repeat(8, 4))) # [8, 8, 8, 8]

print(list(map(operator.mul, range(11), itertools.repeat(5)))) # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# Combinations generator

print(list(itertools.combinations('ABC', 2))) # [('A', 'B'), ('A', 'C'), ('B', 'C')]
print(list(itertools.combinations_with_replacement('ABC', 2))) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
print(list(itertools.permutations('ABC', 2))) # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
print(list(itertools.product('ABC', repeat=2))) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

 
# groupby 
# reverserd
# tee

print(list(itertools.groupby('LLLLAAGGG'))) # [('L', <itertools._grouper object at 0x10c6c93c0>), ('A', <itertools._grouper object at 0x10c6c9510>), ('G', <itertools._grouper object at 0x10c6cabc0>)]
for char, group in itertools.groupby('LLLLAAGGG'):
    print(char, '->', list(group))
'''
        L -> ['L', 'L', 'L', 'L']
        A -> ['A', 'A']
        G -> ['G', 'G', 'G']
'''

animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear',
           'bat', 'dolphin', 'shark', 'lion']
animals.sort(key=len)
print(animals) # ['rat', 'bat', 'duck', 'bear', 'lion', 'eagle', 'shark', 'giraffe', 'dolphin']

for length, group in itertools.groupby(animals, len):
    print(length, '->', list(group))

'''
3 -> ['rat', 'bat']
4 -> ['duck', 'bear', 'lion']
5 -> ['eagle', 'shark']
7 -> ['giraffe', 'dolphin']
'''
for length, group in itertools.groupby(reversed(animals), len):
    print(length, '->', list(group))
    
'''
7 -> ['dolphin', 'giraffe']
5 -> ['shark', 'eagle']
4 -> ['lion', 'bear', 'duck']
3 -> ['bat', 'rat']
'''


# itertools.tee

print(list(itertools.tee('ABC'))) # [<itertools._tee object at 0x103a66b00>, <itertools._tee object at 0x103aed080>]
g1, g2 = itertools.tee('ABC')

print(next(g1)) # A
print(next(g2)) # A
print(list(g1)) # ['B', 'C']
print(list(zip(*itertools.tee('ABC')))) # [('A', 'A'), ('B', 'B'), ('C', 'C')]

# yield 

def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i
            
s = 'ABC'
t = tuple(range(3))
print(list(chain(s, t))) # ['A', 'B', 'C', 0, 1, 2]

def chain(*iterables):
    for i in iterables:
        yield from i

print(list(chain(s, t))) # ['A', 'B', 'C', 0, 1, 2]


# all and any

print(all([1, 2, 3])) # True
print(all([1, 0, 3])) # False 
print(all([])) # True 
# any 
print(any([1, 2, 3])) # True
print(any([1, 0, 3])) # True 
print(any([0, 0, 0])) # False
print(any([])) # False


g = (n for n in [0, 0.0, 7, 8])
print(any(g)) # True
print(next(g)) # 8 # because 0 and 0.0 are false, then drop 7, and generator return next 8




from random import randint

def d6():
    return randint(1, 6)

d6_iter = iter(d6, 1)
print(d6_iter) # <callable_iterator object at 0x101a7a070>
for roll in d6_iter:
    print(roll)
    
    
def f(): 
    def do_yield(n):
        yield n
    x = 0
    while True:
        x += 1
        yield from do_yield(x) # use yield from to yield values from subgenerator
        
print(f()) # <generator object f at 0x10b63e8f0>


class Fibonacci:
    
    def __iter__(self):
        return FibonacciGenerator()
    
class FibonacciGenerator:
    
    def __init__(self):
        self.a = 0
        self.b = 1
        
    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result
    
    def __iter__(self):
        return self
    

# fib = Fibonacci()
# fib_gen = iter(fib)
# for _ in range(10):
#     print(next(fib_gen))

def fibonacci():
    a, b = 0, 1
    while True:
        yield a 
        a, b = b, a + b