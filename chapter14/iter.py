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