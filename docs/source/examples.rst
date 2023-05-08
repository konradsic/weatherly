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

    # marine
    marine = client.get_marine_data("Oslo", tides=True) # requires pro+ plan

Bulk requests
---------------

.. note::
    Bulk requests work only on Pro+ plan or higher.

    If you register a new account you will recieve a 14 day free trial with this plan.

To make a bulk request:

1. You need to build a ``BulkRequest`` First
2. Select an endpoint you want to make a bulk request on
3. Call a client function

Example of code for a simple bulk request:

.. code:: python

    import weatherly

    client = weatherly.Client("api-key-that-has-proplus-plan")

    # 1. build the obj
    # first way - classmethod
    bulk = weatherly.BulkRequest.build(
        ("id-one", "London"),("id-two", "Berlin"), # here pass tuples (id, query)
        endpoint=weatherly.WeatherEndpoints.CURRENT_WEATHER # select an endpoint from the WeatherEndpoint enum
    )
    # second way - build with methods from empty class
    bulk = BulkRequest() # currently empty 
    # we will add endpoints and query tuples by using methods
    bulk.add_query(("id-one", "London")) # tuple (id, query)
    bulk.add_query(("id-two", "Berlin"))
    # 2. set endpoint
    bulk.set_endpoint(weatherly.WeatherEndpoints.CURRENT_WEATHER)

    # 3. call the client function
    bulk_result = client.bulk_request(data=bulk)
    bulk_current_weather = bulk_result.data # a list of (id, CurrentWeatherData) tuples

    # example of prining the bulk request results
    for custom_id, weather_obj in bulk_current_weather:
        print(f"{custom_id}/{weather_obj.location.name}: {weather_obj.temp_c}C, feels like: {weather_obj.feelslike_c}C")