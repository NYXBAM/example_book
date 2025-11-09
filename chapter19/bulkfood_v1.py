

class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
        
    def subtotal(self):
        return self.weight * self.price
    
raisins = LineItem('Golden raisins', 10, 6.95)
print(raisins.subtotal()) # 69.5
