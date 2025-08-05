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
while True:
    target = round(random(), 6)  
    print(f"Searching for occurrences of {target}...")
    floats_round = array('d', (round(random(), 6) for _ in range(10**7)))
    co = floats_round.count(target)
    if co > 0:
        print(f"Occurrences of {target}: {co}")
        break

