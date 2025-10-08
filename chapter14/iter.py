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
