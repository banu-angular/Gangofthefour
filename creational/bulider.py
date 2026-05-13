# A bowl can have dozens of different combinations. If you used a standard constructor, it would look like a confusing mess of strings and booleans:
# Meal bowl = new Meal("Quinoa", "Chicken", true, false, true, true, "Tahini", false, true);
# This makes it impossible to tell which true refers to "Extra Greens" versus "Double Protein."
# The Builder Pattern solves this by providing a clear, step-by-step way to construct complex objects. You can chain method calls to specify exactly what you want in your meal bowl, making the code much more readable and maintainable.
# Builder Pattern Implementation in Python
class MealBuilder:
    def __init__(self):
        self.meal = {}

    def set_base(self, base):
        self.meal['base'] = base
        return self

    def set_protein(self, protein):
        self.meal['protein'] = protein
        return self

    def add_extra_greens(self, extra_greens=True):
        self.meal['extra_greens'] = extra_greens
        return self

    def add_double_protein(self, double_protein=True):
        self.meal['double_protein'] = double_protein
        return self

    def set_dressing(self, dressing):
        self.meal['dressing'] = dressing
        return self

    def build(self):
        return self.meal
# Example usage:
if __name__ == "__main__":  
    meal = MealBuilder()
    meal_bowl = (meal.set_base("Quinoa")
                    .set_protein("Chicken")
                    .add_extra_greens()
                    .add_double_protein()
                    .set_dressing("Tahini")
                    .build())
    print(meal_bowl)
    # Output: {'base': 'Quinoa', 'protein': 'Chicken', 'extra_greens': True, 'double_protein': True, 'dressing': 'Tahini'}
    # : True, 'double_protein': True, 'dressing': 'Tahini'
    


