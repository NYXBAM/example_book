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