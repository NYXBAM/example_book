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
print(my_coro2.send(99)) # -> Received: c = 99
print(getgeneratorstate(my_coro2)) # 'GEN_CLOSED'