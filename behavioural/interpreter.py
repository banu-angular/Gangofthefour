# Consider a Basic Calculator that reads a string like 5 + 2 * 3. The Interpreter pattern builds a tree structure where each number and operator is a "rule." It then evaluates this tree to produce a result. This pattern is essentially used whenever you need to define a simple language and process its grammar.
from abc import ABC, abstractmethod
class Expression(ABC):
    @abstractmethod
    def interpret(self):
        pass
class Number(Expression):
    def __init__(self, value):
        self.value = value
    def interpret(self):
        return self.value
class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def interpret(self):
        return self.left.interpret() + self.right.interpret()
class Multiply(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def interpret(self):
        return self.left.interpret() * self.right.interpret()
# Example usage
# Represents the expression: 5 + 2 * 3

expression = Add(Number(5), Multiply(Number(2), Number(3)))
result = expression.interpret()
print(f"Result of the expression: {result}")
# Output:
# Result of the expression: 11
