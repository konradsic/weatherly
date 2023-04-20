.. currentmodule:: weatherly

Feature documentation
==========================
This section is a documentation of the weatherly API interface.


Client
----------
.. attributetable:: WeatherAPIClient

.. autoclass:: WeatherAPIClient
    :members:

Enums
----------
.. autoclass:: Languages
    :members:

Responses from WeatherAPI
------------------------------
.. attributetable:: CurrentWeatherData

.. autoclass:: CurrentWeatherData
    :members:

.. attributetable:: LocationData

.. autoclass:: LocationData
    :members:

Exceptions
-------------

.. autoexception:: WeatherlyException
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