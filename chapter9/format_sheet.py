# This is a quick reference sheet for Python's str.format() method.




"{} {}".format("Hello", "World")          # "Hello World"
"{1} {0}".format("World", "Hello")        # "Hello World"  
"{name} {age}".format(name="John", age=25) # "John 25"


# Numbers 

"{:.2f}".format(3.14159)      # "3.14" 
"{:+.2f}".format(3.14)        # "+3.14" 
"{:,.2f}".format(12345.67)    # "12,345.67"

"{:d}".format(42)             # "42" # decimal
"{:b}".format(42)             # "101010" # binary
"{:x}".format(255)            # "ff" # hexadecimal
"{:o}".format(64)             # "100" # octal


"{:.1%}".format(0.8567)       # "85.7%"  # percentage


# Text
"{:>10}".format("test")       # "      test" - right
"{:<10}".format("test")       # "test      " - left  
"{:^10}".format("test")       # "   test   " - center

# Fill characters
"{:*>10}".format("test")      # "******test" - star
"{:_<10}".format("test")      # "test______" - underscore
"{:═^10}".format("test")      # "═══test═══" - box drawing character

# Numbers
"{:>10d}".format(42)          # "        42" - right
"{:010d}".format(42)          # "0000000042" - zero-padded


# Lists
fruits = ["apple", "banana", "orange"]
"{0[0]} і {0[2]}".format(fruits)          # "apple and orange"

# Dict  
person = {"name": "Petro", "age": 35}
"{name} - {age} y.o".format(**person)   # "Petro - 35 y.o"

# Attributes
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
user = User("Mariya", 28)
"{0.name} - {0.age} y.o".format(user)   # "Mariya - 28 y.o"

# DATE and TIME 

from datetime import datetime
now = datetime.now()

"{:%Y-%m-%d}".format(now)        # "2025-09-07"
"{:%H:%M:%S}".format(now)        # "14:30:25" 
"{:%d.%m.%Y %H:%M}".format(now)  # "07.09.2025 14:30"

# Special symbols

# Braces
"{{}}".format()                  # "{}"
"{{{}}}".format("test")          # "{test}"

# Special conversions
"{!r}".format("hello")           # "'hello'" - repr()
"{!s}".format("hello")           # "hello" - str()  
"{!a}".format("Привет")          # '\u041f\u0440\u0438\u0432\u0435\u0442' - ascii()

