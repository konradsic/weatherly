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
.. attributetable:: Client

.. autoclass:: Client
    :members:
    :exclude-members: event

    .. automethod:: Client.event()
        :decorator:

Enums
=========
.. autoclass:: Languages
    :members:

.. autoclass:: SportsEventType
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

.. attributetable:: FutureData

.. autoclass:: FutureData
    :members:

.. attributetable:: IPData

.. autoclass:: IPData
    :members:

.. attributetable:: AstronomicalData

.. autoclass:: AstronomicalData
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