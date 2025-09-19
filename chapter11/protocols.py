from typing import Any


class Foo:
    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]
        
f = Foo()
print(f[1]) # 10
for i in f: print(i) # 0 10 20

import collections
from random import shuffle

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) 
                       for suit in self.suits 
                       for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
    # this method allows item assignment (shuffling)
    def __setitem__(self, position, card):
        deck._cards[position] = card 

    

# Monkey patching __setitem__ to enable shuffle
# def set_card(deck, position, card):
#     deck._cards[position] = card
    

l = list(range(10))
shuffle(l)
print(l)
# but trying to shuffle a deck
deck = FrenchDeck()
# shuffle(deck) # TypeError: 'FrenchDeck' object does not support item assignment
# so we add __setitem__ method to FrenchDeck
# FrenchDeck.__setitem__ = set_card
shuffle(deck)
print(deck[:5])

# ----------------- ABCs ----------------- # 

class Struggle:
    def __len__(self): return 22
    
from collections import abc

print(isinstance(Struggle(), abc.Sized)) # True

# ---------------- Frenchdeck2.py ---------------- # 

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck2(collections.MutableSequence):
    ranks =[str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) 
                       for suit in self.suits 
                       for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def __setitem__(self, position, value):
        self._cards[position] = value
    
    def __delitem__(self, position):
        del self._cards[position]
    
    def insert(self, position, value):
        self._cards.insert(position, value)    