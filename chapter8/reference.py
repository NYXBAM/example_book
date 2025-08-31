class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))
    
    
x = Gizmo()
print(x) # Gizmo id: 4430965328

'''
y = Gizmo() * 10 # This will raise an error
print(y)


    y = Gizmo() * 10
        ~~~~~~~~^~~~
TypeError: unsupported operand type(s) for *: 'Gizmo' and 'int'

'''

# --------------- ownerships --------------- # 
print('\nOwnerships:')
charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
print(lewis is charles) # True
print(id(lewis), id(charles)) # 4434761920 4434761920
lewis['balance'] = 950
print(charles) # {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}

alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
print(alex is charles) # False
print(alex == charles) # True
print(alex is not charles) # True

# --------------- tuples --------------- # 
print('\nTuples:')  
t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])

print(t1==t2) # True 

print(id(t1[-1])) # 4355770624
t1[-1].append(99)
print(t1) # (1, 2, [30, 40, 99])
print(id(t1[-1])) # 4355770624 
print(t1==t2) # False 


# --------------- default lists copying --------------- # 
print('\nDefault lists copying:')

l1 = [3, [55, 44], (7, 8, 9)]
l2 = list(l1)
print(l2)
print(l2 is l1) # False
print(l2 == l1) # True  


l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)

l1.append(100)
l1[1].remove(55)
print('l1:',l1) # l1: [3, [66, 44], (7, 8, 9), 100]
print('l2:', l2) # l2: [3, [66, 44], (7, 8, 9)]
l2[1] += [33, 22]
l2[2] += (10,11)
print('l1:',l1) # l1: [3, [66, 44, 33, 22], (7, 8, 9), 100]
print('l2:', l2) # l2: [3, [66, 44, 33, 22], (7, 8, 9, 10, 11)]

# --------------- shallow and deep copying --------------- #
print('\nShallow and deep copying:')
import copy

class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
    
    def pick(self, name):
        self.passengers.append(name)
    
    def drop(self, name):
        self.passengers.remove(name)

    
    
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1) # shallow copy
bus3 = copy.deepcopy(bus1) # deep copy  
print(id(bus1), id(bus2), id(bus3)) # 4456953376 4458256400 4458256720
bus1.drop('Bill')
print(bus2.passengers) # ['Alice', 'Claire', 'David']
print(id(bus1), id(bus2), id(bus3)) # 4456953376 4458256400 4458256720
print(bus3.passengers) # ['Alice', 'Bill', 'Claire', 'David']

# --------------- circular references --------------- #
print('\nCircular references:') 
a = [10, 20]
b = [a, 30]
a.append(b)
print(a) # [10, 20, [...], 30]
from copy import deepcopy
c = deepcopy(a)
print(c) # [10, 20, [...], 30]

# --------------- call by sharing muttable / immutable  --------------- # 
print('\nCall by sharing:')

def f(a, b):
    a += b 
    return a 

x = 1 
y = 2 
print(f(x, y))
a = [1, 2]
b = [3, 4]

print(f(a, b)) #  [1, 2, 3, 4]
print(a, b) # [1, 2, 3, 4] [3, 4]

t = (10, 20)
u = (30, 40)
 
print(f(t, u)) # (10, 20, 30, 40)
print(t, u) #  (10, 20) (30, 40)

class HauntedBus:
    def __init__ (self, passengers=[]):
        self.passengers = passengers
        
    def pick(self, name):
        self.passengers.append(name)
        
    def drop(self, name):
        self.passengers.remove(name)
        


bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers) # ['Alice', 'Bill']
bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers) # ['Bill', 'Charlie']

bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers) # ['Carrie']

bus3 = HauntedBus()
print(bus3.passengers) # ['Carrie']
bus3.pick('Dave')
print(bus2.passengers) # ['Carrie', 'Dave']
print(bus2.passengers is bus3.passengers)  # True

print(HauntedBus.__init__.__defaults__[0])  # ['Carrie', 'Dave']

class TwilightBus:
    def __init__ (self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers  # we need to copy this list if we want to avoid side effects
            # self.passengers = list(passengers) # It`s correct and better way
            
    def pick(self, name):
        self.passengers.append(name)
        
    def drop(self, name):
        self.passengers.remove(name)
        
basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_team)
bus.drop('Tina') 
bus.drop('Pat')
print(basketball_team) # ['Sue', 'Maya', 'Diana']


