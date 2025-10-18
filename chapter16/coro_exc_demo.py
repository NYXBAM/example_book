class DemoException(Exception):
    """An exception type for the demo."""
    
    
def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
                print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run.')

exc_coro = demo_exc_handling()
next(exc_coro) 
# -> coroutine started
exc_coro.send(11)
# -> coroutine received: 11
exc_coro.send(22)
# -> coroutine received: 22
exc_coro.close()
from inspect import getgeneratorstate
print(getgeneratorstate(exc_coro))
# 'GEN_CLOSED'

exc_coro = demo_exc_handling()
next(exc_coro) 
# -> coroutine started
exc_coro.send(11)
# -> coroutine received: 11
exc_coro.send(22)
# -> coroutine received: 22
exc_coro.throw(DemoException) 
# *** DemoException handled. Continuing...
from inspect import getgeneratorstate
print(getgeneratorstate(exc_coro))  # GEN_SUSPENDED

exc_coro = demo_exc_handling()
next(exc_coro) 
# -> coroutine started
exc_coro.send(11)
# -> coroutine received: 11
exc_coro.send(22)
# -> coroutine received: 22
exc_coro.throw(ZeroDivisionError) 

from inspect import getgeneratorstate
print(getgeneratorstate(exc_coro))  # GEN_CLOSED

def demo_finally():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled. Continuing...')
            else:
                print('-> coroutine received: {!r}'.format(x))
    finally:
        print('-> coroutine ending')