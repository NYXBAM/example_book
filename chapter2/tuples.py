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