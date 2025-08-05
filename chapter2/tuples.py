# Small chapter about tuples
# Tuples are immutable sequences in Python, often used to store related data.

lax_coordinates = (33.9425, -118.408056)  # Tuple representing latitude and longitude

city, year, pop, chg, area = 'Tokyo', 2003, 32450, 0.66, 8014.0  # Unpacking a tuple
traveler_ids = [("USA", "31195855"), ("BRA", "CE342567"), ("ESP", "XDA205856")]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)  # Output: USA/31195855, BRA/CE342567, ESP/XDA205856
    print(passport)
    # new formating 
    print(f'{passport[0]}/{passport[1]}')  # Output: USA/31195855, BRA/CE342567, ESP/XDA205856

for country, _ in traveler_ids:
    print(country)  # Output: USA, BRA, ESP


# Tuple unpacking 
lax_coordinates = (33.9425, -118.408056)  # Tuple representing latitude and longitude
latitude, longitude = lax_coordinates  # Unpacking the tuple
print(latitude)  # Output: 33.9425
print(longitude)  # Output: -118.408056 


import os

_, filename = os.path.split('/home/username/documents/file.txt')  # Unpacking the result of os.path.split
print(filename)  # Output: file.txt


a, b, *rest = range(5)
print(a)
print(b)
print(rest)


######################################

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 26.072, (28.613889, 77.209444)),
    ('Mexico City', 'MX', 20.142, (19.432778, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.712778, -74.006111)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:^9.4f} | {:^9.4f}'

for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))