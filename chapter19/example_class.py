


class Class:
    data = 'the data class attr'
    @property
    def prop(self):
        return 'the prop value'
    
obj = Class()
print(vars(obj)) # {}
print(obj.data) # the data class attr
obj.data = 'bar'
print(vars(obj)) # {'data': 'bar'}
print(obj.data) # bar
print(Class.data) # the data class attr
print(Class.prop) # <property object at 0x106c16840>
print(obj.prop) # the prop value
# obj.prop = 'foo' # AttributeError: can't set attribute 'prop'
obj.__dict__['prop'] = 'foo'
print(vars(obj)) # {'data': 'bar', 'prop': 'foo'}
print(obj.prop) # the prop value
Class.prop = 'baz'
print(obj.prop) # foo
print(obj.data) # bar
print(Class.data) # the data class attr
Class.data = property(lambda self: 'the "data" prop value')
print(obj.data) # the "data" prop value
del Class.data
print(obj.data) # bar
