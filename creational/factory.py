# Imagine you are building an app for a logistics company. Initially, the app only handles Truck deliveries. As the business grows, they start using Ships for sea deliveries.

# If you hard-code new Truck() everywhere, adding "Ships" (or later, "Airplanes") would require you to rewrite your entire codebase. The Factory Method solves this by letting a "Factory" decide which object to create based on what you need.

# Factory Method Pattern Implementation in Python
class VehicleFactory:
    def create_vehicle(self, vehicle_type):
        if vehicle_type == "Truck":
            return Truck()
        elif vehicle_type == "Ship":
            return Ship()
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")

class Truck:
    def deliver(self):
        return "Delivering by truck"

class Ship:
    def deliver(self):
        return "Delivering by ship"

# Example usage:
if __name__ == "__main__":  
    factory = VehicleFactory()
    truck = factory.create_vehicle("Truck")
    ship = factory.create_vehicle("Ship")
    print(truck.deliver())  # Delivering by truck
    print(ship.deliver())   # Delivering by ship
    try:
        factory.create_vehicle("Airplane")
    except ValueError as e:
        print(e)      # Unknown vehicle type: Airplane


