
class FetchWeatherData:
        def __init__(self, city):
            self.city = city
            self.weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
        }

        def get_weather_data(self, city):
          data =  self.weather_data.get(city, "Data not available.")
          print(f"Fetching weather data for...{data}")
 
class DataParser(FetchWeatherData):
        def __init__(self, data):
           super().__init__(self)
           self.data = data
               
        def parse_weather_data(self, city):
                
            data = self.weather_data.items()
            for city, value in data:
                print(f"Forecast for : {city}")
                for item, reading in value.items():
                    print(f' {item} : {reading}')


         

class UserInterface(DataParser):
        def __init__(self, city):
         super().__init__(self)
         self.city= city

        def get_city_forecast(self, city):
            for key, value in self.weather_data.items():
              if key == city:
                print(f'{key} : {value}')

        def get_detailed_forecast(self, city):
            self.parse_weather_data(city)
       
   

