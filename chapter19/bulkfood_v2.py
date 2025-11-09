

class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
        
    def subtotal(self):
        return self.weight * self.price
    
    @property
    def weight(self):
        return self.__weight
        
    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')
    
    
# raisins = LineItem('Walnuts', 0, 6.95)
# print(raisins.subtotal()) # raise ValueError('value must be > 0')
                          # ValueError: value must be > 0

