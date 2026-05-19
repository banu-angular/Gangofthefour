# Think of an Airport Control Tower. If every pilot tried to communicate directly with every other pilot to coordinate landings, there would be chaos. Instead, all pilots talk only to the Control Tower (the Mediator). The tower handles the complex coordination and tells each pilot when it is safe to land, keeping the individual planes decoupled from one another.
class Mediator:
    def __init__(self):
        self._colleagues = []

    def register(self, colleague):
        self._colleagues.append(colleague)
        colleague.set_mediator(self)

    def send(self, message, sender):
        for colleague in self._colleagues:
            if colleague != sender:
                colleague.receive(message)
class Colleague:
    def __init__(self, name):
        self.name = name
        self.mediator = None

    def set_mediator(self, mediator):
        self.mediator = mediator

    def send(self, message):
        print(f"{self.name} sends: {message}")
        self.mediator.send(message, self)

    def receive(self, message):
        print(f"{self.name} receives: {message}")
# Usage Example
if __name__ == "__main__":
    mediator = Mediator()
    pilot1 = Colleague("Pilot 1")
    pilot2 = Colleague("Pilot 2")
    pilot3 = Colleague("Pilot 3")
    mediator.register(pilot1)
    mediator.register(pilot2)
    mediator.register(pilot3)
    pilot1.send("Requesting permission to land.")
    pilot2.send("Requesting permission to take off.")
# Output:
# Pilot 1 sends: Requesting permission to land.
# Pilot 2 receives: Requesting permission to land.
# Pilot 3 receives: Requesting permission to land.
# Pilot 2 sends: Requesting permission to take off.
# Pilot 1 receives: Requesting permission to take off.
# Pilot 3 receives: Requesting permission to take off.
