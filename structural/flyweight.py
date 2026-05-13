# The Setup: You are developing a Forest Simulator game where you need to render 1,000,000 Trees on the screen.
# The Problem: Each Tree object has "Intrinsic State" (shared data like the 3D model, texture, and color) and "Extrinsic State" (unique data like X, Y coordinates). If you create 1 million full objects, the computer will run out of RAM.
# Your Task: Create a TreeType class to store the heavy shared data (model, texture). Use a Flyweight Factory to ensure you only create one instance of each tree type (e.g., one 'Oak' object, one 'Pine' object). Then, create a Tree class that only stores the coordinates and a reference to the shared TreeType.
class TreeType:
    def __init__(self, model, texture, color):
        self.model = model
        self.texture = texture
        self.color = color
class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type  
class TreeFactory:
    _tree_types = {}

    @staticmethod
    def get_tree_type(model, texture, color):
        key = (model, texture, color)
        if key not in TreeFactory._tree_types:
            TreeFactory._tree_types[key] = TreeType(model, texture, color)
        return TreeFactory._tree_types[key]
# Usage Example
tree1 = Tree(10, 20, TreeFactory.get_tree_type("OakModel",
                                                "OakTexture",
                                                "Green"))   
tree2 = Tree(30, 40, TreeFactory.get_tree_type("OakModel",
                                                "OakTexture",
                                                "Green"))
tree3 = Tree(50, 60, TreeFactory.get_tree_type("PineModel",
                                                "PineTexture",  
                                                "Dark Green"))
print(f"Tree1 and Tree2 share the same TreeType: {tree1.tree_type is tree2.tree_type}")
print(f"Tree1 and Tree3 share the same TreeType: {tree1.tree_type is tree3.tree_type}")
# Output:
# Tree1 and Tree2 share the same TreeType: True     
# Tree1 and Tree3 share the same TreeType: False
