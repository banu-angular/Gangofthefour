# The Setup: You are developing a Graphics App that can draw different Shapes (Circle, Square) in different Colors (Red, Blue).
# The Problem: If you create classes like RedCircle, BlueCircle, RedSquare, and BlueSquare, your code will grow too fast (Class Explosion).
# Your Task: Create a Color interface (The Implementation) and a Shape abstract class (The Abstraction). Use the Bridge to link them so you can add new colors or shapes independently without changing the other.
# Color Interface (The Implementation)
class Color:
    def fill(self):
        pass
# Shape Abstract Class (The Abstraction)
class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        self.color.fill()
# Concrete Color Implementations
class Red(Color):
    def fill(self):
        print("Filling with Red color.")    
class Blue(Color):
    def fill(self):
        print("Filling with Blue color.")
# Concrete Shape Implementations
class Circle(Shape):
    def draw(self):
        print("Drawing a Circle.")
        super().draw()
class Square(Shape):
    def draw(self):
        print("Drawing a Square.")
        super().draw()
# Usage Example
red_circle = Circle(Red())
blue_square = Square(Blue())
red_circle.draw()
blue_square.draw()  
# Output:
# Drawing a Circle.
# Filling with Red color.
# Drawing a Square.
# Filling with Blue color.



