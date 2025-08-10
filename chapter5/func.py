def factorial(n):
    '''returns n'''
    return 1 if n < 2 else n * factorial(n - 1)

print(factorial(333))
print(factorial.__doc__)

fact = factorial
print(fact(333))

fruits = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi']

print(sorted(fruits, key=len))

def reverce_string(s):
    '''Returns the reversed string'''
    return s[::-1]

print(sorted(fruits, key=reverce_string))
