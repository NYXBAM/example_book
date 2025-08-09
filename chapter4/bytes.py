def println(a):
    print(a)

s = 'café'
println(len(s))

b = s.encode('utf-8')
println(b)
println(len(b))

c = b.decode('utf-8')
println(c)

cafe = bytes('café', encoding='utf_8')
println(cafe)
println(cafe[0])
cafe_arr = bytearray(cafe)
println(cafe_arr)
println(cafe_arr[-1:])

print(bytes.fromhex('31 4B CE A9'))

import array 
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
print(octets)

for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Nino'.encode(codec), sep='\t')


city = "São Paulo"
print(city.encode('utf-8'))
print(city.encode('latin-1', errors='replace')) # replaces characters that can't be encoded ????
print(city.encode('utf_16')) 
print(city.encode('iso8859_1'))
print(city.encode('cp437', errors='xmlcharrefreplace')) # replaces characters that can't be encoded with XML character references

u16 = 'São Paulo'.encode('utf-16')
print(list(u16))

### UNICODE NORMALIZATION

from unicodedata import normalize, name

s1 = 'café'
s2 = 'cafe\u0301'

print(s1 == s2)  # False


print(normalize('NFC', s1) == normalize('NFC', s2))  # ✅ True

print(list(normalize('NFD', s1)))  # ['c', 'a', 'f', 'e', '́']

ohm = '\u2126'
# ohm = 'Й'
print(name(ohm))
ohm_c = normalize('NFC', ohm)
print(ohm_c)
print(name(ohm_c))  # GREEK CAPITAL LETTER OMEGA


def nfc_equal(s1, s2):
    return normalize('NFC', s1) == normalize('NFC', s2)


print(nfc_equal(s1, s2))  # True


### --- UNICODE NORMALIZATION --- ###

import unicodedata
import string

def shave_marks(txt):
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt
                     if unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)


order = '<>><><>><Hello ĉ, ĝ, ĥ, ĵ,sdkas Hersssr Voß: # § ⸹ ¶ ⸿ (capitulum) № ⌘ ჻ ፨ ※ ℹ ⅈ '



shaved_order = shave_marks(order)
print(shaved_order) 
