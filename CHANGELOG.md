# 📜 Weatherly changelog
In this file you can view the changelog, including updates and changes that were made to this package.

### Version 0.7.0
This version adds supports for the Sports API. Following things were added:
* `weatherly.Client(...).get_sports_data` for fetching sports data
* `SportsData` as a response from function above and `SportsEvent` that is a single event, part of the `SportsData` class. 

### Version 0.6.0
This version adds support for the Astronomy API and IP Lookup API. Two new methods for the `weatherly.Client` were implemented:
* `get_ip_data` for retrieving IP information
* `get_astronomical_data` for retrieving astronomical data (e.g. sunrise)

Slight improvements to the documentation were made, removed `abc.py` as there was no real reason for it to exist. All responses are in `responses.py` whatsoever.

### Version 0.5.1
This version removes unnecessary classes `FutureDay` and `FutureHour`. They have been removed because only one parameter was not returned from the Future API. 
So now `ForecastDay` and `ForecastHour` have the `uv` parameter optional. Also, some changes have been made to the documentation and docs build command.

### Version 0.5.0
This version adds support for Future API with 3 new classes and a client method.
* Added `Client(...).get_future_data()` for getting future weather data.
* Added `FutureData`, `FutureDay` and `FutureHour` classes because returned data from Future API is slightly different from forecast data standard.

### Version 0.4.0
This version adds support for History API with some new, cool features
* New exception: `weatherly.InvalidDate`, raised from `weatherly.get_historical_data` when the date is invalid
* `client.get_historical_data` assuming that *client* is an instance of `weatherly.Client` : you can now get historical forecast data as `ForecastData` object
* `weatherly.ForecastData.iter_hours` : an iterator that lets you easily iterate over every hour data from the class.

Improvements to the documentation:
* Added `.. container:: operations` handling with custom CSS and JS. This directive is used for desribing operations for a class, function etc.

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