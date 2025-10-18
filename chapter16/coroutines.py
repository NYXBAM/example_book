def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:', x)
    
# my_coro = simple_coroutine()
# print(my_coro) # <generator object simple_coroutine at 0x10cff9bd0>
# print(next(my_coro)) # -> coroutine started
# print(my_coro.send(42)) # -> coroutine received: 42
#   print(my_coro.send(42))
#   StopIteration

def simple_coro2(a):
    print('-> Strted: a =', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)
    
my_coro2 = simple_coro2(14)
from inspect import getgeneratorstate
print(getgeneratorstate(my_coro2)) # 'GEN_CREATED'

print(next(my_coro2)) # -> Strted: a = 14
print(getgeneratorstate(my_coro2)) # 'GEN_SUSPENDED'
print(my_coro2.send(28)) # -> Received: b = 28
# print(my_coro2.send(99)) # -> Received: c = 99
# print(getgeneratorstate(my_coro2)) # 'GEN_CLOSED'

from coroutil import coroutine

@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count
        
# coro_avg = averager()
# print(next(coro_avg)) # None
# print(coro_avg.send(10)) # 10.0
# print(coro_avg.send(30)) # 20.0
# print(coro_avg.send(5))  # 15.0


coro_avg = averager()
from inspect import getgeneratorstate
print(getgeneratorstate(coro_avg)) # 'GEN_SUSPENDED'
print(coro_avg.send(10)) # 10.0
print(coro_avg.send(30)) # 20.0
print(coro_avg.send(5)) # 15.0

coro_avg = averager() 
print(coro_avg.send(40)) # 40.0
print(coro_avg.send(50)) # 45.0
# print(coro_avg.send('spam')) # TypeError: unsupported operand type(s) for +=: 'float' and 'str'
# print(coro_avg.send(50)) # StopIteration