# 📜 Weatherly changelog
In this file you can view the changelog, including updates and changes that were made to the package.

### Version 0.3.0
This version adds support for Forecast API with a lot of new features and classes.
* Renamed `WeatherAPIClient` to `Client`
* `ForecastData` is a return object from `Client.get_forecast_data`
* `ForecastDay` is a component of `ForecastData`.
* `ForecastHour` is a component of `ForecastDay`.
* `AlertData` is an object representing a weather alert, e.g. a flood
* Bugfixes as always

It all adds up to the new, large update.

### Version 0.2.0
This version introduced the `weatherly.LocationData` class, so you can retrieve location information.
* NEW: `weatherly.CurrentWeatherData` now has a `location` attribute, which is exactly `weatherly.LocationData`
* Added `weatherly.WeatherAPIClient.get_locations` method that returns an array of `weatherly.LocationData` objects - found locations for the given query.

### Version 0.1.1
This version fixes all bugs when uploading to PyPI. The package is now live on https://pypi.org/project/weatherly/

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