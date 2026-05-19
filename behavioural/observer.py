# Imagine a Weather Station that tracks temperature and humidity. Whenever the weather data changes, the station needs to update several different displays—a mobile app, a physical LCD screen, and a web dashboard. Instead of the station manually calling each device, the displays "subscribe" to the station. When an update occurs, the station simply notifies all its subscribers at once.
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)
class Observer:
    def update(self, data):
        pass
class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = 0
        self._humidity = 0

    def set_weather_data(self, temperature, humidity):
        self._temperature = temperature
        self._humidity = humidity
        self.notify((self._temperature, self._humidity))
class MobileApp(Observer):
    def update(self, data):
        temperature, humidity = data
        print(f"Mobile App: Temperature={temperature}°C, Humidity={humidity}%") 
class LCDScreen(Observer):
    def update(self, data):
        temperature, humidity = data
        print(f"LCD Screen: Temperature={temperature}°C, Humidity={humidity}%")
class WebDashboard(Observer):
    def update(self, data):
        temperature, humidity = data
        print(f"Web Dashboard: Temperature={temperature}°C, Humidity={humidity}%")
# Usage Example
weather_station = WeatherStation()
mobile_app = MobileApp()
lcd_screen = LCDScreen()
web_dashboard = WebDashboard()
weather_station.attach(mobile_app)
weather_station.attach(lcd_screen)
weather_station.attach(web_dashboard)
weather_station.set_weather_data(25, 60)
# Output:
# Mobile App: Temperature=25°C, Humidity=60%
# LCD Screen: Temperature=25°C, Humidity=60%
# Web Dashboard: Temperature=25°C, Humidity=60%
weather_station.set_weather_data(30, 55)
# Output:
# Mobile App: Temperature=30°C, Humidity=55%
# LCD Screen: Temperature=30°C, Humidity=55%
# Web Dashboard: Temperature=30°C, Humidity=55%
weather_station.detach(mobile_app)
weather_station.set_weather_data(28, 58)
# Output:
# LCD Screen: Temperature=28°C, Humidity=58%
# Web Dashboard: Temperature=28°C, Humidity=58%

