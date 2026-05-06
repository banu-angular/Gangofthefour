# Imagine you are developing a war game like Age of Empires or Total War. You need to create 1,000 Soldier units.

# The Problem:
# Each Soldier has a complex 3D model, textures, base health, and a heavy set of initial weapons. If you use new Soldier() 1,000 times, the game will lag because the CPU has to reload all that heavy data from the disk for every single soldier.
# The Prototype Pattern solves this by allowing you to create a "prototype" Soldier with all the heavy data loaded once, and then clone that prototype whenever you need a new Soldier. This way, you only load the heavy data once, and cloning is much faster.
# Prototype Pattern Implementation in Python
import copy
class Soldier:
    def __init__(self, health, weapons):
        self.health = health
        self.weapons = weapons

    def clone(self):
        return copy.deepcopy(self)
# Example usage:
if __name__ == "__main__":  
    prototype = Soldier(100, ["Sword", "Shield"])
    soldier1 = prototype.clone()
    soldier2 = prototype.clone()
    print(soldier1.health)  # 100
    print(soldier2.health)  # 100   
    print(soldier1.weapons)  # ['Sword', 'Shield']
    print(soldier2.weapons)  # ['Sword', 'Shield']
    soldier1.weapons.append("Bow")
    print(soldier1.weapons)  # ['Sword', 'Shield', 'Bow
    print(soldier2.weapons)  # ['Sword', 'Shield'], soldier2 is unaffected by changes to soldier1's weapons
    print(prototype.weapons)  # ['Sword', 'Shield'], prototype is unaffected by changes to soldier1's weapons

    