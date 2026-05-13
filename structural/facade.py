# The Setup: You are building a Home Theater System.
# The Problem: To watch a movie, you have to: 1. Turn on the Lights, 2. Dim them, 3. Turn on the Projector, 4. Set input to DVD, 5. Turn on the Sound System, 6. Start the Player. It’s too complex for the user.
# Your Task: Create a Facade class called HomeTheaterFacade. It should have one simple method called watchMovie(). This method will handle all those complex steps internally so the user only clicks one button
class Lights:
    def on(self):
        print("Lights are ON.")

    def dim(self):
        print("Lights are DIMMED.")
class Projector:
    def on(self):
        print("Projector is ON.")

    def set_input(self, input_source):
        print(f"Projector input set to {input_source}.")
class SoundSystem:
    def on(self):
        print("Sound System is ON.")
class Player:
    def on(self):
        print("Player is ON.")
class HomeTheaterFacade:
    def __init__(self):
        self.lights = Lights()
        self.projector = Projector()
        self.sound_system = SoundSystem()
        self.player = Player()

    def watchMovie(self):
        self.lights.on()
        self.lights.dim()
        self.projector.on()
        self.projector.set_input("DVD")
        self.sound_system.on()
        self.player.on()    
# Usage Example
home_theater = HomeTheaterFacade()
home_theater.watchMovie()
# Output:
# Lights are ON.
# Lights are DIMMED.
# Projector is ON.
# Projector input set to DVD.
# Sound System is ON.
# Player is ON.
