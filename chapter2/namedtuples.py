from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

print(tokyo.name)  # Output: Tokyo
print(tokyo.country)  # Output: JP
print(tokyo.population)  # Output: 36.933
print(tokyo.coordinates)  # Output: (35.689722, 139.691667)

print(City._fields)  # Output: ('name', 'country', 'population', 'coordinates')


LatLong = namedtuple('LatLong', 'lat long')
delphi_data = ('Delhi NCR', 'IN', 26.072, LatLong(28.613889, 77.209444))
delphi = City._make(delphi_data)
print(delphi)  # Output: City(name='Delhi NCR', country='IN', population=26.072, coordinates=LatLong(lat=28.613889, long=77.209444))
print(delphi._asdict())  # Output: {'name': 'Delhi NCR', 'country': 'IN', 'population': 26.072, 'coordinates': LatLong(lat=28.613889, long=77.209444)}

for key, value in delphi._asdict().items():
    print(f"{key}: {value}")