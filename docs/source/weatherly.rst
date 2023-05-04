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

Enums
=========

Languages
-------------
.. autoclass:: Languages
    :members:

Sports event type
-----------------------
.. autoclass:: SportsEventType
    :members:


Responses from WeatherAPI
============================
.. important::
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