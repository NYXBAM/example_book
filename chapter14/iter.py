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
