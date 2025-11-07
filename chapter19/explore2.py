# pseudo 

# def object_maker(the_class, some_args):
#     new_object = the_class.__new__(some_args)
#     if isinstance(new_object, the_class):
#         the_class._init_(new_object, some_args)
    
#     return new_object


from collections import abc
import keyword

class FrozenJSON:
    
    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg
        
    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value
            
    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else: 
            return FrozenJSON(self.__data[name])
        
        

