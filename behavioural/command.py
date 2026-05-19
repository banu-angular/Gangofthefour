# Think of a Smart Home Remote with programmable buttons. Each button represents a command, such as TurnOnLight or OpenGarageDoor. When you press a button, the remote doesn't need to know the complex wiring of the light or the garage motor; it simply triggers the "Execute" method of the command object assigned to that button. This allows you to easily reassign buttons or queue actions.
class Command:
    def execute(self):
        pass
class Light:
    def turn_on(self):
        print("The light is on.")
    def turn_off(self):
        print("The light is off.")
class TurnOnLightCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_on()
class TurnOffLightCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_off()
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()
# Usage Example
light = Light()
remote = RemoteControl()
turn_on_command = TurnOnLightCommand(light)
turn_off_command = TurnOffLightCommand(light)
remote.set_command(turn_on_command)
remote.press_button()  # Output: The light is on.
remote.set_command(turn_off_command)
remote.press_button()  # Output: The light is off.
# Output:
# The light is on.
# The light is off.

