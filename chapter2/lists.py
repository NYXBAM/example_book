symbols = "!@#$%^&*()"
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
    print(f"Symbol: {symbol} Code: {ord(symbol)}")


# 2 

symbols = "!@#$%^&*()"
codes = [ord(symbol) for symbol in symbols]
print(codes)

# some another examples 

# squares
numbers = [1,2,3,4,5]
squares = [n**2 for n in numbers]
print(squares)

# 2

numbers = [1,2,3,4,5,6,7,8,9,10]
evens = [n for n in numbers if n % 2 ==0]
print(evens)

# 3 temp convertaion
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(9/5)*temp + 32 for temp in celsius]
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]


# # # # book example #########

x = "ABC"
dummy = [ord(x) for x in x]
print(dummy)  # [65, 66, 67]


symbols = "!@#$%^&*()©®"
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)  

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)  


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6, 8, 10]

words = ["apple", "banana", "cat", "dog", "elephant"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(long_words)  # ['banana', 'elephant']



# -----------> decarts <----------- # 
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes] 
print(tshirts)  # [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]
for color in colors: 
    for size in sizes: 
        print((color, size))


tshirts = [(color, size) for size in sizes for color in colors]
print(tshirts)  # [('S', 'black'), ('S', 'white'), ('M', 'black'), ('M', 'white'), ('L', 'black'), ('L', 'white')]





# -----------> decarts <----------- #

symbols = "!@#$%^&*()"
res = tuple(ord(symbol) for symbol in symbols)
print(res)  # (33, 64, 35, 36, 37, 94, 38, 42, 40, 41)

import array

ress = array.array('I', (ord(symbol) for symbol in symbols))
print(ress)


# Descartes out generator

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

# if u wanna new fstring 
# it`s the same as above but with f-string

for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)



