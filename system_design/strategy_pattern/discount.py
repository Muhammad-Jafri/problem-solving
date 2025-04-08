from abc import ABC, abstractmethod

# Strategy Interface
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total):
        pass

# Concrete Strategies
class NoDiscount(DiscountStrategy):
    def apply_discount(self, total):
        return total

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage
        
    def apply_discount(self, total):
        return total - (total * self.percentage / 100)

class FixedDiscount(DiscountStrategy):
    def __init__(self, amount):
        self.amount = amount
        
    def apply_discount(self, total):
        return max(0, total - self.amount)

# Context
class ShoppingCart: # Other classes are used as a variable here
    def __init__(self, discount_strategy=NoDiscount()):
        self.items = []
        self.discount_strategy = discount_strategy
    
    def add_item(self, item, price):
        self.items.append((item, price))
    
    def calculate_total(self):
        total = sum(price for _, price in self.items)
        return self.discount_strategy.apply_discount(total)
    
    def set_discount_strategy(self, discount_strategy):
        self.discount_strategy = discount_strategy


# Create a shopping cart with no discount
cart = ShoppingCart()
cart.add_item("Book", 10)
cart.add_item("Pen", 5)
print(f"Total with no discount: ${cart.calculate_total()}")

# Change to percentage discount
cart.set_discount_strategy(PercentageDiscount(10))
print(f"Total with 10% discount: ${cart.calculate_total()}")

# Change to fixed discount
cart.set_discount_strategy(FixedDiscount(7))
print(f"Total with $7 fixed discount: ${cart.calculate_total()}")