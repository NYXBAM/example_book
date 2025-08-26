def deco(func):
    def inner():
        print('running inner()')
    return inner
    
@deco
def target():
    print('running target()')

target()
# running inner()

###### registration.py ####### 

registry = []

def register(func):
    print(f'running register{func}')
    registry.append(func)
    return func

@register 
def f1():
    print('running f1()')

@register 
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

if __name__ == '__main__':
    main()

# ------------------------------------- # 
b = 6
def f1(a):
    print(a)
    print(b)

f1(3)

# def f2(a):
#     print(a)
#     print(b)
#     b = 9

# f2(3)


import dis 

# dis.dis(f1)
'''
 47           RESUME                   0

 48           LOAD_GLOBAL              1 (print + NULL)
              LOAD_FAST                0 (a)
              CALL                     1
              POP_TOP

 49           LOAD_GLOBAL              1 (print + NULL)
              LOAD_GLOBAL              2 (b)
              CALL                     1
              POP_TOP
              RETURN_CONST             0 (None)
'''

# --------------------- closure --------------------- # 

class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)

avg = Averager()
print(avg(10)) # 10.0
print(avg(11)) # 10.5

def make_averager():
    '''
    functional realisation
    '''
    series = []
    hueries = []

    def averager(new_value):
        series.append(new_value)
        print(hueries)
        total = sum(series)
        return total/len(series)
    return averager

avg = make_averager()

print(avg(10)) # 10.0
print(avg(11)) # 10.5


print(avg.__code__.co_varnames) # ('new_value', 'total')
print(avg.__code__.co_freevars) # ('series',)

# --------------------- nonlocal --------------------- # 

def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    
    return averager 


# --------------------- functools.lru_cache --------------------- # 

from clockdeco_demo import clock
import functools

@clock
def fibonacci(n):
    if n < 2: 
        return n
    return fibonacci(n-2) + fibonacci(n-1)


if __name__ == '__main__':
    print(fibonacci(6))

@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2: 
        return n
    return fibonacci(n-2) + fibonacci(n-1)


if __name__ == '__main__':
    print(fibonacci(6))


# --------------------- singledispatch --------------------- # 

import html

def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

print(htmlize((1,2,3))) # <pre>(1, 2, 3)</pre>
print(htmlize(abs)) # <pre>&lt;built-in function abs&gt;</pre>
print('Chlen & Co\n- a ch') # Chlen & Co
                            # - a ch



from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0}  (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


data = [1, "Hello World", (2, 3)]
print(htmlize(data))