.. currentmodule:: weatherly

==========================
Feature documentation
==========================
This section is a documentation of the weatherly API interface.

Version informations
=======================
You can gather version info in two ways:

.. data:: __version__

    Version of the project following the `PEP 440 <https://peps.python.org/pep-0440/>`_ standard.

    For example, this can be ``1.2.0a2``

.. data:: version_info

    A named tuple containing version informations. Similiar to :obj:`sys.version_info`


Clients
==============

Client
------------
.. attributetable:: Client

.. autoclass:: Client
    :members:
    :exclude-members: event

    .. automethod:: Client.event()
        :decorator:

Event reference
====================
Weatherly provides an easy to use event system. There are two ways to register an event function.

**First** method is to use :meth:`Client.event` decorator.

.. code:: python

    import weatherly
    client = weatherly.Client("your-api-key")

    @client.event
    def on_error(func_name, exception):
        print(f"Exception occured in {func_name}!")

**Second** way is to make a custom client class inheriting from :class:`Client`.

.. code:: python

    import weatherly

    class CustomClient(weatherly.Client):
        def __init__(self, api_key):
            super().__init__(api_key=api_key)

        def on_error(func_name, exception):
            print(f"Exception occured in {func_name}!")

.. important::
    All event functions **mustn't be** coroutines.
    A :exc:`ValueError` is raised when a function is a coroutine.

Error handling
--------------------
.. function:: on_error(func, exc)

    Called when an error occured during calling a client method

    :param func: The function name where the exception occured.
    :type func: :class:`str`

    :param exc: The exception that occured
    :type exc: Inherits from :exc:`Exception`

API calls
------------
.. function:: on_api_call_successful(request, response)

    Called when an API call (e.g. :meth:`Client.get_current_weather`) was successfully done.

    :param request: The request URL e.g. https://api.weatherapi.com/v1/endpoint?param=value
    :type request: :class:`str`

    :param response: Response class
    :type response: :external:py:class:`requests.Response`

Enums
=========

Languages
-------------
.. autoclass:: Languages()
    :members:

Sports event type
-----------------------
.. autoclass:: SportsEventType()
    :members:

Tide height type
-------------------
.. autoclass:: TideHeight()
    :members:


Responses from WeatherAPI
============================
.. warning::
    Those classes should not be created manually, instead they are returned from methods like ``get_current_weather`` of the :class:`Client` class.

.. note::
    When adding a ``lang`` parameter to the request only ``condition_text`` is translated into requested language.

Current weather
---------------------

.. attributetable:: CurrentWeatherData

.. autoclass:: CurrentWeatherData()
    :members:

Location
------------
.. attributetable:: LocationData

.. autoclass:: LocationData()
    :members:

Air Quality
--------------

.. attributetable:: AirQualityData

.. autoclass:: AirQualityData()
    :members:

.. attributetable:: AlertData

.. autoclass:: AlertData()
    :members:

Forecast related
-------------------

.. attributetable:: ForecastData

.. autoclass:: ForecastData()
    :members:

.. attributetable:: ForecastDay

.. autoclass:: ForecastDay()
    :members:

.. attributetable:: ForecastHour

.. autoclass:: ForecastHour()
    :members:

Future
----------

.. attributetable:: FutureData

.. autoclass:: FutureData()
    :members:

IP
-------

.. attributetable:: IPData

.. autoclass:: IPData()
    :members:

Astronomical
------------

.. attributetable:: AstronomicalData

.. autoclass:: AstronomicalData()
    :members:

Sports related
-------------------

.. attributetable:: SportsEvent

.. autoclass:: SportsEvent()
    :members:

.. attributetable:: SportsData

.. autoclass:: SportsData()

Marine
-----------------------

.. attributetable:: MarineHour

.. autoclass:: MarineHour()
    :members:

.. attributetable:: MarineDay

.. autoclass:: MarineDay()
    :members:

.. attributetable:: MarineData

.. autoclass:: MarineData()
    :members:

.. attributetable:: TideData

.. autoclass:: TideData()

Exceptions
===============

.. autoexception:: WeatherlyException
    :members:

.. autoexception:: InvalidDate
    :members:

.. autoexception:: WeatherAPIException
    :members:

.. autoexception:: NoLocationFound
    :members:

.. autoexception:: InvalidAPIKey
    :members:

.. autoexception:: APILimitExceeded
    :members:

.. autoexception:: APIKeyDisabled
    :members:

.. autoexception:: AccessDenied
    :members:

.. autoexception:: InternalApplicationError
    :members: