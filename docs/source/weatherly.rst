.. currentmodule:: weatherly

==========================
Feature documentation
==========================
This section is a documentation of the weatherly API interface.


Clients
==============
.. attributetable:: Client

.. autoclass:: Client
    :members:

Enums
=========
.. autoclass:: Languages
    :members:


Responses from WeatherAPI
============================
.. note::
    Those classes should not be created manually, instead they are returned from methods like ``get_current_weather`` of the :class:`Client` class.

.. attributetable:: CurrentWeatherData

.. autoclass:: CurrentWeatherData
    :members:

.. attributetable:: LocationData

.. autoclass:: LocationData
    :members:

.. attributetable:: AirQualityData

.. autoclass:: AirQualityData
    :members:

.. attributetable:: AlertData

.. autoclass:: AlertData
    :members:

.. attributetable:: ForecastData

.. autoclass:: ForecastData
    :members:

.. attributetable:: ForecastDay

.. autoclass:: ForecastDay
    :members:

.. attributetable:: ForecastHour

.. autoclass:: ForecastHour
    :members:

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