# Classic syntax proprty deco

class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
        
    def __repr__(self):
        """Example repr"""
        return f'<weight: {self.weight}>\n<price: {self.price}\ndesk: {self.description}>'
        
    def subtotal(self):
        return self.weight * self.price
    
    def get_weight(self):
        return self._weight

    def set_weight(self, value):
        if value > 0:
            self._weight = value
        else:
            raise ValueError('value must be > 0')
        
    weight = property(get_weight, set_weight)
    

item = LineItem(description='Banana', weight=103, price=15)
