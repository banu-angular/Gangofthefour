# 1. Adapter Pattern Scenario
# The Setup: You are building a Weather Dashboard that expects temperature in Celsius using a method called getTemperatureCelsius().
# The Problem: You are forced to use an external Legacy Weather Service that only provides data in Fahrenheit through a method called getTemperatureFahrenheit().
# Your Task: Write an Adapter class that wraps the Legacy Service and converts the Fahrenheit value to Celsius so your Dashboard can display it correctly.
class LegacyWeatherService:
    def getTemperatureFahrenheit(self):
        # Simulating a call to an external service that returns temperature in Fahrenheit
        return 77.0  # Example temperature in Fahrenheit
class WeatherAdapter:
    def __init__(self, legacy_service):
        self.legacy_service = legacy_service

    def getTemperatureCelsius(self):
        fahrenheit = self.legacy_service.getTemperatureFahrenheit()
        celsius = (fahrenheit - 32) * 5.0/9.0
        return celsius
# Usage Example
legacy_service = LegacyWeatherService()
adapter = WeatherAdapter(legacy_service)
temperature_celsius = adapter.getTemperatureCelsius()
print(f"Temperature in Celsius: {temperature_celsius:.2f}°C")
# Output: Temperature in Celsius: 25.56°C
