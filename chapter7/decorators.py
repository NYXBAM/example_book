# This code not from book. 
# it`s my own examples 
#
# examples from book here:
# /example_book/chapter7/book-decorators.py



import time 

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end  = time.time()
        print(f"{func.__name__} took {end - start:.4f} sec")
        return result
    return wrapper




def logger_decorator(func):
    def wrapper():
        print(f"Init func: {func.__name__}")
        func()  
        print(f"Func: {func.__name__} finished")
    return wrapper

@timing
@logger_decorator
def say_hello():
    print("Hello, world!")

say_hello()

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Init {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)  
        print(f"func {func.__name__} return {result}")
        return result
    return wrapper

@logger_decorator
def add(a, b):
    return a + b

print(add(3, 5))

# decorator with params
@timing
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)  # Repeat func 3 times
def say_hello():
    print("hi!")

say_hello()


####### Example auth

def check_access(func):
    def wrapper(*args):
        if args[0] == "admin" and args[1] == "password":
            print('hello admin')
            return func(*args)
        
        else:
            return "Access denied"
    
    return wrapper
        #

@check_access
def login(user, password): 
    # print(f"Hello {user}")
    return f"Welcome {user}"

print(login('admin', 'password'))
print(login('admin', '1234'))


# ------------------------------------ # 


# @timing
# def slow():
#     time.sleep(1)

# slow()

# @timing
# def start_count():
#     total = 0
#     while total < 999990:
#         total += 1
#         print(total)


# start_count()


# ------------------- # 

def cache(func):
    saved = {}
    def wrapper(x):
        if x in saved:
            print(f"Take from cache: {x}")
            return saved[x]
        result = func(x)
        saved[x] = result
        return result
    return wrapper


@timing
@cache
def slow_square(x):
    print(f"Sqrt {x}...")
    return x * x

print(slow_square(4))

print(slow_square(4))

print(slow_square(4)) 
print(slow_square(4)) 

# --------------- closure --------------- # 
def outer_func(x):
    def inner_func(y):
        return x + y  
    return inner_func

closure = outer_func(10)  
print(closure(5))  # 15
print(closure(20)) # 30



# --------------------- singledispatch --------------------- # 

from functools import singledispatch

@singledispatch
def process(value):
    print(f"Unknown {type(value)} -> {value}")

@process.register(int)
def _(value):
    print(f"This is integer: {value}")

@process.register(str)
def _(value):
    print(f"This is string: '{value}'")

@process.register(list)
def _(value):
    print(f"This is list with {len(value)} elements")

lst = [1,2,3,4,5,6,7,8]
process(lst)  # This is list with 8 elements