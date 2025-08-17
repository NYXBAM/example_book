# ---- Strategy Pattern ----
from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order: # abstract base class
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        """Return the total for this order."""
        if not hasattr(self, '_total'):
            self._total = sum(item.total() for item in self.cart)
        return self._total


    def due(self):
        """Return the total minus any applicable discount."""
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total:{:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        """Return discount as a positive dollar amount."""

class FidelityPromo(Promotion):
    """5% discount for orders over $1000."""
    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0

class BulkItemPromo(Promotion):
    """10% discount on each LineItem with quantity >= 20."""
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount

class LargeOrderPromo(Promotion):
    """7% discount for orders with 10 or more distinct items."""
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.07
        return 0


# Example usage
customer1 = Customer('John Doe', 1200)
print(customer1)  # Customer(name='John Doe', fidelity=1200)
order1 = Order(customer1, [LineItem('item1', 1, 100), LineItem('item2', 2, 50)], FidelityPromo())
print(order1)  # <Order total:200.00 due:190.00>
# Example usage with different promotions
customer2 = Customer('Jane Smith', 800)
order2 = Order(customer2, [LineItem('item1', 20, 10), LineItem('item2', 5, 20)], BulkItemPromo())
print(order2)  # <Order total:150.00 due:135.00>


# --------------------- # 
# --- functional programming --- #

from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
    
    def total(self):
        if not hasattr(self, '_total'):
            self._total = sum(item.total() for item in self.cart)
        return self._total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount
    
    def __repr__(self):
        fmt = '<Order total:{:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):
    """5% discount for orders over $1000."""
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0

def bulk_item_promo(order):
    """10% discount on each LineItem with quantity >= 20."""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount

def large_order_promo(order):
    """7% discount for orders with 10 or more distinct items."""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0


# Example usage
customer1 = Customer('John Doe', 1200)
cart = [LineItem('item1', 1, 100), LineItem('item2', 2, 50), 
          LineItem('item3', 3, 30), LineItem('item4', 4, 20)]

order1 = Order(customer1, cart, fidelity_promo)
print(order1)  # <Order total:200.00 due:190.00>

    