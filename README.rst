====================
⛅ weatherly
====================
Weatherly is a simple package that retrieves weather data from WeatherAPI.com. It provides an easy to use interface to access current and historical weather data for a specific location.

📜 Features
-----------
* Easy to use,
* Intuitive design,
* Can provide current weather data aswell as forecast, historical data, future predictions and even more!
* Modern and typed Python package,
* Support for languages (provided by WeatherAPI)

💻 Code example
---------------

.. code:: python

    import weatherly
    
    client = weatherly.WeatherAPIClient(api_key="your WeatherAPi key")
    # you can set language to all request, or pass it manually
    client.set_language("fr")     # lang code
    client.set_language("German") # language full name

    # getting weather info
    current_weather = client.get_current_weather(query="London")

    # getting forecast info
    forecast = client.get_forecast_data(query="Paris")

    # historical data
    history = client.get_historical_data(query="48.8567,2.3508") # query could also be latitude,longitude

    # marine data
    marine = client.get_marine_data(query="Madrid")