# This code demonstrates the creation of dictionaries in Python using different methods.

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict([('one', 1), ('two', 2), ('three', 3)])
d = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
e = dict.fromkeys(['one', 'two', 'three'], 0)
print(a == b == c == d)  # True

# dictcomp 
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (7, 'Russia'),
    (81, 'Japan'),
]

country_code = {country: code for code, country in DIAL_CODES}
print(country_code)  # {'China': 86, 'India': 91, 'United States': 1, 'Indonesia': 62, 'Brazil': 55, 'Russia': 7, 'Japan': 81}

# ------------------------------------------- # 

import sys 
import re
import collections

WORK_RE = re.compile(r'\w+')
index = {}

with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORK_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location =  (line_no, column_no)
            occurrences = index.setdefault(word, [])
            occurrences.append(location)
            index[word] = occurrences


for word in sorted(index, key=str.upper):
    locations = index[word]
    print(f"{word:15} {locations!r}")  



# ------------------------------------------- # 

WORK_RE = re.compile(r'\w+')
index = {}
with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORK_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])  

# ------------------------------------------- #
WORK_RE = re.compile(r'\w+')
index = collections.defaultdict(list) # using defaultdict for cleaner code
with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORK_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)
for word in sorted(index, key=str.upper):
    print(word, index[word])


# __missing__ method # 

class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

d  = StrKeyDict0([('2', 'two'), ('4', 'four')])

print(d['2'])  # Output: two
print(d[2])  # Output: tw

print(d.get(4))  # Output: four