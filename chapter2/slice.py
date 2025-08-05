invoice = """
0.....6.....12.............18........24.........................50..........

1909   Pimoroni PiBrella                        $17.50              3   $52.50  
1510   SparkFun RedBot Mainboard                $49.00              1   $49.00
1511   SparkFun RedBot Chassis Kit              $89.00              2   $178.00
"""

SKU = slice(0, 6) 
DESCRIPTION = slice(6, 35)
UNIT_PRICE = slice(32, 60) 
line_items = invoice.split('\n')[3:] 
for item in line_items:
    print(item[SKU], item[DESCRIPTION], item[UNIT_PRICE])



#################

l = list(range(10))
print(l)
l[2:5] = [20, 30]
print(l)  # Output: [0, 1, 20, 30, 5, 6, 7, 8, 9]
del l[5:7]
print(l)
l[3::2] = [11, 12]
print(l)

# ----------------# 

l = [1,2,3]
print(l*5)

# ----------------#

board = [['_'] * 3 for _ in range(3)]  # Create a 3x3 board
print(board)  # Output: [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
board[1][1] = 'X'  # Place an 'X' in the center
print(board)  # Output: [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]


board = []
for i in range(3):
    row = ['_'] * 3 
    board.append(row)  # Create a new row for each iteration


# interesting, but another way to create a board

weird_board = [['_'] * 3] * 3  # Create a 3x3 board with references to the same list
weird_board[2][2] = 'O'  # Place an 'O' in the center
print(weird_board)  # Output: [['_', '_', '_'], ['_', 'O', '_'], ['_', 'O', '_']]
# look detail, all rows are the same
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)

print(board)


#---------------> 

l = [1, 2, 3]
print(id(l))
l *= 2
print(l)  # Output: [1, 2, 3, 1, 2, 3]
print(id(l))

t = (1, 2, 3)
print(id(t))
t *= 2
print(t)  # Output: (1, 2, 3, 1, 2, 3)
print(id(t))  # We see how to id is changed, because tuples are immutable and a new tuple is created



#---------------> BISECT <----------- #

import bisect
import sys 

HAYSTACK = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
NEEDLES = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
ROW_FMT = '{0:>2d} @ {1:>2d} {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * ' |'
        print(ROW_FMT.format(needle, position, offset))

if __name__ == '__main__':
    print('DEMO bisect_left:')
    demo(bisect.bisect_left)
    print('\nDEMO bisect_right:')
    demo(bisect.bisect_right)


# # Example of using bisect to find the closest record in a sorted list
index = [(100, 'addr1'), (200, 'addr2'), (300, 'addr3')]
key = 250
pos = bisect.bisect_left(index, (key,))
# # If pos is not at the end, we can get the closest record
record = index[pos-1][1] if pos > 0 else None
print(f"Closest record to {key}: {record}")

# More examples: 

def grade(score, breakpoints=[60,70,80,90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

print(grade(70))  # Output: 'C'
print([grade(score) for score in [33, 99, 77, 70, 90, 100]])


####### bisect.insort() example

import bisect
import random

SIZE = 7

random.seed(1729)

my_list = []
for i in range(SIZE):
    value = random.randrange(SIZE*2)
    bisect.insort(my_list, value)
    print(f'Inserted {value} into {my_list}')

