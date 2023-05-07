.. currentmodule:: weatherly

=====================
Examples and usage
=====================

.. note::
    For full documentation of this module check :doc:`weatherly`

Repository
-------------
Many examples of using this package can be found `in this repository <https://github.com/konradsic/weatherly/tree/master/examples>`_

Creating a simple client
---------------------------
.. code:: python

    import weatherly

    client = weatherly.Client("your-api-key")

Variable ``client`` will be used across this documentation

Creating a custom client
--------------------------
.. code:: python

    import weatherly

    class MyCustomClient(weatherly.Client):
        def __init__(self, api_key):
            super().__init__(api_key)

This is a simple example of creating a custom client by inheriting from ``weatherly.Client``

Handling events
------------------
You can create event handlers by decorators and custom client methods.

.. code:: python

    @client.event
    async def on_error(func, error):
        # so something
        print(f"Error in {func}!")
    
    # custom client
    import weatherly

    class ClientThatHandlesEvents(weatherly.Client):
        def __init__(self, api_key):
            super().__init__(api_key)

        # event handler
        def on_error(func, error):
            print(f"Error in {func}!")

Examples of retrieving weather informations
-----------------------------------------------

.. warning::
    Depending on your WeatherAPI plan (check `here <https://weatherapi.com/my>`_) functions may raise :exc:`AccessDenied`. 
    Check `plans & pricing <https://www.weatherapi.com/pricing.aspx>`_ for more informations

.. code:: python

    # current
    current_weather = client.get_current_weather(query="London", aqi=True) # enable Air Quality data

    # forecast
    forecast = client.get_forecast_data("Paris", days=3)

    # history
    historical = client.get_historical_data("Berlin", date="2023-05-05")