# 📜 Weatherly changelog
In this file you can view the changelog, including updates and changes that were made to the package.

### Version 0.1.0
This is the first release of the `weatherly` package. It adds:
* A client (`WeatherAPIClient`)
* Client needs to have an API key
* After setting up the client you can get current weather. Code example:
```py
import weatherly

client = weatherly.WeatherAPIClient("Your API Key")
current_weather = weatherly.get_current_weather(query="London") # ret: CurrentWeatherData
# get informations from it
print(current_weather.temp_c) # temperature in celsius
print(current_weather.wind_dir) # wind direction (e.g. "W")
#... and more!
```