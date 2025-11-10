# in classic syntax we used <weight = property(get_weight, set_weight, 
#                                               doc="Weight in kilograms")

class Foo:
    @property
    def bar(self):
        "The bar attribute"
        return self.__dict__['bar']
    
    @bar.setter
    def bar(self, value):
        self.__dict__['bar'] = value