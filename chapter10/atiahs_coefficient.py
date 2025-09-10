# This some example code for using atiah's coefficient
# This not from book example
# It`s myself examples

import math

class Movie:
    def __init__(self, views, rating):
        self.views = views    
        self.rating = rating 
    
    def otiah_normalize(self):
        k = 1 / math.sqrt(2)
        return Movie(self.views * k, self.rating * k)
    
    def __repr__(self):
        return f"Movie(views={self.views:.1f}k, rating={self.rating:.1f})"

# Some films with different views and ratings
movie1 = Movie(1000, 8.5)  
movie2 = Movie(100, 9.8)  
movie3 = Movie(500, 7.2)  

print("Original films:")
print(movie1)  # Movie(views=1000.0k, rating=8.5)
print(movie2)  # Movie(views=100.0k, rating=9.8)  
print(movie3)  # Movie(views=500.0k, rating=7.2)


norm1 = movie1.otiah_normalize()
norm2 = movie2.otiah_normalize()
norm3 = movie3.otiah_normalize()

print("\nNormalized films:")
print(norm1)  # Movie(views=707.1k, rating=6.0)
print(norm2)  # Movie(views=70.7k, rating=6.9)
print(norm3)  # Movie(views=353.6k, rating=5.1)

### Phones 

class Product:
    def __init__(self, price, rating):
        self.price = price   
        self.rating = rating 
    
    def otiah_normalize(self):
        k = 1 / math.sqrt(2)
        return Product(self.price * k, self.rating * k)
    
    def value_score(self):
        return self.rating / self.price if self.price > 0 else 0


iphone = Product(1000, 4.8)    
budget_phone = Product(200, 4.2)
cheap_phone = Product(50, 2.5)  

norm_iphone = iphone.otiah_normalize()
norm_budget = budget_phone.otiah_normalize()  
norm_cheap = cheap_phone.otiah_normalize()


print(f"iPhone: {norm_iphone.value_score():.4f}") # 0.0048 
print(f"Norm: {norm_budget.value_score():.4f}")  # 0.0210
print(f"Cheap: {norm_cheap.value_score():.4f}") # 0.0500