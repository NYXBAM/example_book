
with open('mirror.py') as fp:
    src = fp.read()
    
print(len(src)) # 106
print(fp) # <_io.TextIOWrapper name='mirror.py' mode='r' encoding='UTF-8'>
print(fp.closed) # True
print(fp.encoding) # UTF-8


from mirror import LookingGlass
with LookingGlass() as what:
    print('Alice, Kitty and Snowdrop')
    print(what)

# pordwonS dna yttiK ,ecilA
print(what) # JABBERWOCKY

manager = LookingGlass()
print(manager) # <mirror.LookingGlass object at 0x10c22f310>

monster = manager.__enter__()
print(monster) # YKCOWREBBAJ
print(monster == 'JABBERWOCKY') # eurT
print(manager) # >0137c7401x0 ta tcejbo ssalGgnikooL.rorrim<

# Using @contextmanager

from mirror_gen import looking_glass
with looking_glass() as what:
    print('Alice, Kitty and Snowdrop')
    print(what)
# pordwonS dna yttiK ,ecilA
print(what) # YKCOWREBBAJ