⛅ weatherly
====================
.. image:: https://img.shields.io/github/license/konradsic/weatherly?color=blue&style=for-the-badge
    :target: https://github.com/konradsic/weatherly/blob/master/LICENSE
    :alt: Weatherly license
.. image:: https://img.shields.io/pypi/v/weatherly?color=blue&style=for-the-badge
    :target: https://pypi.python.org/project/weatherly
    :alt: Weatherly version on PyPI
.. image:: https://img.shields.io/pypi/pyversions/weatherly?color=blue&style=for-the-badge
    :target: https://pypi.python.org/project/weatherly
    :alt: Supported Python versions
.. image:: https://img.shields.io/pypi/status/weatherly?style=for-the-badge
    :target: https://pypi.python.org/project/weatherly
    :alt: Project status
.. image:: https://img.shields.io/github/actions/workflow/status/konradsic/weatherly/build.yml?style=for-the-badge
    :target: https://github.com/konradsic/weatherly
    :alt: Build status

Weatherly is a simple package that retrieves weather data from WeatherAPI.com. It provides an easy to use interface to access current and historical weather data for a specific location.

Features
---------------
* Easy to use,
* Intuitive design,
* Can provide current weather data aswell as forecast, historical data, future predictions and even more!
* Modern and typed Python package,
* Support for languages (provided by WeatherAPI)

Installing
------------
To install weatherly on your computer Python 3.10 or higher is required. If your python version meets the requirements run:

.. code:: shell
    
    # Windows
    py -3 -m pip install -U weatherly

    # MacOS / Linux
    python3 -m pip install -U weatherly

Congratulations! Now weatherly is ready to use on your machine.

Code example
---------------------

.. code:: python

    import weatherly
    
    client = weatherly.Client(api_key="your WeatherAPI key")
    # you can set language to all request, or pass it manually
    client.set_language("fr")     # lang code
    client.set_language("German") # language full name

    # getting weather info
    current_weather = client.get_current_weather(query="London")

    # getting forecast info
    forecast = client.get_forecast_data(query="Paris", days=3)

    # historical data
    history = client.get_historical_data(query="48.8567,2.3508", date="2010-01-01") # query could also be latitude,longitude

    # marine data
    marine = client.get_marine_data(query="Madrid")
