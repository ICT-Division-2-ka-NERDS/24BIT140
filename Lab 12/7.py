class Weather:
	def __init__(self, temperature, humidity, wind_speed, pressure):
		self.weather_params = {
			"temperature": temperature,
			"humidity": humidity,
			"wind speed": wind_speed, 
			"pressure": pressure
		}
	def __contains__(self, item):
		return item in self.weather_params

weather_today = Weather(30, 60, 15, 1013)

print("temperature" in weather_today)  
print("rainfall" in weather_today)     
print("wind speed" in weather_today)   
print("pressure" in weather_today)     
