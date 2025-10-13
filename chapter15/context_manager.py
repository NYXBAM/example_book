
with open('mirror.py') as fp:
    src = fp.read()
    
print(len(src)) # 106
print(fp) # <_io.TextIOWrapper name='mirror.py' mode='r' encoding='UTF-8'>
print(fp.closed) # True
print(fp.encoding) # UTF-8
