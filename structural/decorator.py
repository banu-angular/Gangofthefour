# An e-commerce coffee shop system uses the Decorator pattern to calculate prices for customized drinks dynamically without creating dozens of complex subclasses like EspressoWithMilkAndCaramel. The system starts with a simple core object, a Plain Coffee, which has a base price of ₹100. When a customer adds toppings like milk or caramel, each ingredient acts as a visual wrapper around the original coffee object. At checkout, the outermost wrapper calculates the total cost by requesting the price from the inner coffee object and adding its own ingredient fee to the total. This allows customers to mix, match, or double up on any combination of extras at runtime while keeping the core software architecture lightweight, clean, and easily maintainable.
# Component Interface
class Coffee:
    def get_cost(self):
        pass
# Concrete Component
class PlainCoffee(Coffee):
    def get_cost(self):
        return 100
# Decorator Base Class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee
    def get_cost(self):
        return self.coffee.get_cost()
# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def get_cost(self):
        return super().get_cost() + 20
class CaramelDecorator(CoffeeDecorator):
    def get_cost(self):
        return super().get_cost() + 30
# Usage Example
# Start with a plain coffee
coffee = PlainCoffee()
print(f"Cost of Plain Coffee: ₹{coffee.get_cost()}")
# Add milk
coffee_with_milk = MilkDecorator(coffee)
print(f"Cost of Coffee with Milk: ₹{coffee_with_milk.get_cost()}")
# Add caramel on top of milk
coffee_with_milk_and_caramel = CaramelDecorator(coffee_with_milk)
print(f"Cost of Coffee with Milk and Caramel: ₹{coffee_with_milk_and_caramel.get_cost()}")
# Output:
# Cost of Plain Coffee: ₹100
# Cost of Coffee with Milk: ₹120
# Cost of Coffee with Milk and Caramel: ₹150
