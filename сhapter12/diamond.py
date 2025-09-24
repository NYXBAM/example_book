class A:
    def ping(self):
        print('ping:', self)
        
class B(A):
    def pong(self):
        print('pong:', self)
        
class C(A):
    def pong(self):
        print('PONG', self)

class D(B, C):
    def ping(self):
        super().ping()
        print('post-ping:', self)
        
    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)
        
        
d = D()
print(D.__mro__) # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
print(d.pong()) # pong: <__main__.D object at 0x106baea50>
print(C.pong(d)) # PONG <__main__.D object at 0x106baea50>

print(d.ping()) # ping: <__main__.D object at 0x108e0aa50> # post-ping: <__main__.D object at 0x108e0aa50>

print(d.pingpong())
print(d.pingpong())
# ping: <__main__.D object at 0x10316aa50> # self.ping()
# ping: <__main__.D object at 0x10316aa50> # super().ping()
# pong: <__main__.D object at 0x10316aa50> # self.pong()
# pong: <__main__.D object at 0x10316aa50> # super().pong()
# PONG <__main__.D object at 0x10316aa50> # C.pong(self)

# __mro__ inspection 
print(bool.__mro__) # (<class 'bool'>, <class 'int'>, <class 'object'>)

import tkinter

print(tkinter.Text.__mro__) # (<class 'tkinter.Text'>, <class 'tkinter.Widget'>, <class 'tkinter.BaseWidget'>, <class 'tkinter.Misc'>, <class 'tkinter.Pack'>, <class 'tkinter.Place'>, <class 'tkinter.Grid'>, <class 'tkinter.XView'>, <class 'tkinter.YView'>, <class 'object'>)
