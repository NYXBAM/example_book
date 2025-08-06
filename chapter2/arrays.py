from array import array
from random import random
import copy

floats = array('d', (random() for i in range(10**7)))
# print(floats[-1])  # Access the last element

# fp = open('float.bin', 'wb')
# floats.tofile(fp)  # Write the array to a binary file
# fp.close

# floats2 = array('d')
# fp = open('float.bin', 'rb')
# floats2.fromfile(fp, 10**7)  # Read the array from the binary file
# fp.close()

# print(floats2 == floats)  # Check if the two arrays are equal

floats3 = array('d', floats) 
# OR better 

floats4 = copy.copy(floats3)  # Create a shallow copy of the array

print(type(floats)) 
print(floats3[-1])  # Access the last element of the copied array



# some interesting code to find occurrences of a random float in a large array
# while True:
#     target = round(random(), 6)  
#     print(f"Searching for occurrences of {target}...")
#     floats_round = array('d', (round(random(), 6) for _ in range(10**7)))
#     co = floats_round.count(target)
#     if co > 0:
#         print(f"Occurrences of {target}: {co}")
#         break


# ------------------------------------------------------------------------- # 
numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(memv)
print(len(memv))
print(memv[0])

memv_oct = memv.cast('B')  # Cast to a memoryview of bytes
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)  # Output: array('h', [-2, -1, 1024, 1, 2])

# ------------------------------------------------------------------------- # 

# Numpy example

import numpy as np

a = np.arange(12)
print(a)  # Output: [ 0  1  2  3  4  5  6  7  8  9 10 11]
print(type(a))
print(a.shape)

a.shape = (3, 4)
print(a.shape)
print(a)
print(a[0]) 
print(a[2, 1])
print(a[:, 1])
print(a.transpose())  # Transpose the array

# ------------------------------------------------------------------------- # 

# collections deque
import collections
from collections import Counter

dq = collections.deque(range(10), maxlen=10)
print(dq)  # Output: deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
dq.rotate(3)  # Rotate the deque by 3 positions
print(dq)  # Output: deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
dq.appendleft(11)  # Append 11 to the right
print(dq)  # Output: deque([8, 9, 0, 1, 2, 3, 4, 5, 6, 11], maxlen=10)
dq.extend([12, 13, 14])  # Extend the deque with multiple elements
print(dq)  # Output: deque([9, 0, 1, 2, 3, 4, 5, 6, 11, 12], maxlen=10)
dq.extendleft([15, 16, 17])  # Extend the deque with multiple elements from the left


dq.clear()
print(dq)  # Output: deque([], maxlen=10)
# dq.append(1) # appen takes only one argument
# extend can take multiple arguments
dq.extend([1, 2, 3])
print(dq)  # Output: deque([1, 2, 3], maxlen=10)
dq.rotate(-1) 
print(dq)  # Output: deque([2, 3, 1], maxlen=10)

print(len(dq))

# ------------------------------------------------------------------------- # 

l = [28, 22, '32', '234', 443, 44423, 34234]

sorted_l = sorted(l, key=int)
print(sorted_l) # [22, 28, '32', '234', 443, 34234, 44423]
sorted_l = sorted(l, key=str) 
print(sorted_l) # [22, '234', 28, '32', 34234, 443, 44423]