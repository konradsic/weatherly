Quickstart
=================

.. note::
    Make sure you have installed ``weatherly`` before running code examples. Check out the :doc:`installing` section for more info.

This section will show you some quick and easy examples of using the ``weatherly`` module.

Creating a simple client
---------------------------
To create a basic client, run

.. code:: python

    import weatherly

    client = weatherly.WeatherAPIClient(api_key="your-api-key")

.. note::
    You need to create a application on WeatherAPI.com to use this module. To get an api key, head to `WeatherAPI.com <https://weatherapi.com/>`_, click singup and create an account\n

    After creating an account, head to https://www.weatherapi.com/my/ and copy you API key.

Here, we've created a simple client. Save the file, with a good name like ``example_client.py`` and run it. Nothing will happen, because we've only created a client.

Check out "Getting current weather" section for the next step.

Getting current weather
----------------------------
Once a client is initialized, you can get weather data, for example current weather.

Code example:

.. code:: python
    
    # lets say that you have a client under the "client" variable
    current_weather = client.get_current_weather("London")

    print(current_weather.temp_c)
    print(current_weather.temp_f)

If you run this code, you will see that you've got London's current temperature in celsius (``temp_c``). Weather temperature is also provided in fahrenheit (``temp_f``).