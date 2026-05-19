# Consider a Navigation App that calculates the best route between two points. Depending on the user's preference, the app can use different algorithms: one for the fastest driving route, one for walking paths, and another for public transit. The app's core logic remains the same, but it swaps out the "strategy" (the specific algorithm) based on what the user selects.
class RouteStrategy:
    def calculate_route(self, start, end):
        pass
class DrivingRouteStrategy(RouteStrategy):
    def calculate_route(self, start, end):
        print(f"Calculating the fastest driving route from {start} to {end}.")
class WalkingRouteStrategy(RouteStrategy):
    def calculate_route(self, start, end):
        print(f"Calculating the best walking path from {start} to {end}.")
class PublicTransitRouteStrategy(RouteStrategy):
    def calculate_route(self, start, end):
        print(f"Calculating the best public transit route from {start} to {end}.")
class NavigationApp:
    def __init__(self, strategy: RouteStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: RouteStrategy):
        self._strategy = strategy

    def calculate_route(self, start, end):
        self._strategy.calculate_route(start, end)
# Usage Example
app = NavigationApp(DrivingRouteStrategy())
app.calculate_route("Home", "Work")
app.set_strategy(WalkingRouteStrategy())
app.calculate_route("Home", "Park")
app.set_strategy(PublicTransitRouteStrategy())
app.calculate_route("Home", "Airport")
# Output:
# Calculating the fastest driving route from Home to Work.
# Calculating the best walking path from Home to Park.
# Calculating the best public transit route from Home to Airport.
