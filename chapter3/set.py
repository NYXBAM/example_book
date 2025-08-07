# --------------> SET <--------------- #

l = ['spam', 'spam', 'eggs', 'spam', 'chlen']
j = ['not spam', 'eggs', 'ham', 'spam', 'chlen']

print(set(l))
found = set(l) & set(j)
print(found)  # Output: {'eggs', 'spam'}

s = {1}
print(type(s))
s.pop()
print(s)  # Output: set()

s = {1, 2, 3, 4, 5, 6, 7}

print(len(s))
s.remove(2) # Raises KeyError if the element is not found
print(s)  # Output: {1, 3, 4, 5, 6, 7}
s.discard(444) # No error if the element is not found
print(s)  # Output: {1, 4, 5, 6, 7}


#####  Some speed tests  #####
# import time
# import numpy as np

# numbers = np.random.rand(10_000_000)
# needles = np.random.rand(1)
# start = time.perf_counter()
# found = set(numbers) & set(needles)
# end = time.perf_counter()
# print(f"Set intersection took {end - start:.6f} seconds")

# ----------------------------------------------------- # 
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (7, 'Russia'),
    (81, 'Japan'),
    (49, 'Germany'),
    (33, 'France'),
    (39, 'Italy'),
    (34, 'Spain'),
    (44, 'United Kingdom'),
    (61, 'Australia'),
    (27, 'South Africa'),
    (82, 'South Korea'),
]

d1 = dict(DIAL_CODES)
print('d1:', d1.keys())

d2 = dict(sorted(DIAL_CODES))
print('d2:', d2.keys())

d3 = dict(sorted(DIAL_CODES, key=lambda x: x[1]))
print('d3:', d3.values())



# ----------------------------------------------------- # 