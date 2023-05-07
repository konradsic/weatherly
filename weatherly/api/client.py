"""
MIT License

Copyright (c) 2023 Konrad (@konradsic)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import datetime
import inspect
import traceback
from typing import (Any, Callable, Dict, List, Literal, Optional, ParamSpec,
                    Tuple, TypeVar, Union)

from .. import utils as utils
from ..enums import Languages, WeatherEndpoints
from ..errors import (AccessDenied, APIKeyDisabled, APILimitExceeded,
                      InternalApplicationError, InvalidAPIKey, InvalidDate,
                      NoLocationFound, WeatherAPIException)
from ..responses import (AstronomicalData, BulkRequest, BulkResponse,
                         CurrentWeatherData, ForecastData, FutureData, IPData,
                         LocationData, MarineData, SportsData)
from .core import BaseAPIClient

WEATHERAPI_BASE_URL = "https://api.weatherapi.com/v1/"
BOOL_REPLACE = {True: "yes", False: "no"}

__all__ = (
    "Client",
)

T = TypeVar("T")
P = ParamSpec("P")

class Client(BaseAPIClient):
    """
    A WeatherAPI.com client for fetching various weather information

    Parameters
    ----------
    api_key: :class:`str`
        API Key used to authenticate when sending requests
    lang: Optional[ Union[:class:`str`, :class:`Languages`] ]
        Language from the :class:`Languages` enum or a string representing the language or language code (preferably).
        To get a list of languages visit :class:`Languages`. If ``None`` then the default language is used (English)
    dt: Optional[:class:`int`]
        Restrict date output for Forecast and History API method. (Required for History and Future API)
    end_dt: Optional[:class:`int`]
        Restrict date output for History API method. Only works for API on Pro plan and above. (Available for History API)
    hour: Optional[:class:`int`]
        Restricting forecast or history output to a specific hour in a given day.
    aqi: :class:`bool`
        Enable/Disable Air Quality data in forecast API output. Defaults to "no".
    tides: :class:`bool`
        Enable/Disable Tide data in Marine API output. Defaults to "no".
    kwargs: Dict[:class:`str`, Any]
        Additional keyword arguments passed by default to requests made by the client
        
    Attributes
    -------------
    lang: Optional[:class:`Languages`]
        Language from the :class:`Languages` enum or a string representing the language or language code (preferably).
        To get a list of languages visit :class:`Languages`. If ``None`` then the default language is used (English)
    dt: Optional[:class:`int`]
        Restricted date output for Forecast and History API method. (Required for History and Future API)
    end_dt: Optional[:class:`int`]
        Restricted date output for History API method. Only works for API on Pro plan and above.
    hour: Optional[:class:`int`]
        Restricted forecast or history output to a specific hour in a given day.
    aqi: :class:`bool`
        Indicates if Air Quality data has been enabled
    tides: :class:`bool`
        Indicates if tides data in the Marine API has been enabled
    kwargs: Dict[:class:`str`, Any]
        Additional keyword arguments passed by default to requests made by the client
    """
    def __init__(
        self,
        api_key: str,
        lang: Optional[Union[str, Languages]] = None,
        dt: Optional[int] = None,
        end_dt: Optional[int] = None,
        hour: Optional[int] = None,
        aqi: bool = False,
        tides: bool = False,
        **kwargs: Dict[str, Any]
    ) -> None:
        lang_code = None
        if lang is not None: 
            lang_code = utils.find_language(lang, asobj=True)
        opts = {
            "key": api_key,
            **kwargs
        }
        if lang_code: opts.update(lang = lang_code.value if lang_code is not None else None)

        super().__init__(base_url=WEATHERAPI_BASE_URL,
                         default_options=opts)
        
        self.dt = dt
        self.end_dt = end_dt
        self.hour = hour
        self.aqi = aqi
        self.tides = tides
        self.kwargs = kwargs
        self.lang = Languages(lang_code) if lang_code else None
    
    
    def _call_request(self, endpoint: str, options: Dict[str, Any]) -> Dict[str, Any]:
        """Private method used to make requests to WeatherAPI"""
        final_options = self.default_options.copy()

        for k,v in final_options.items(): # check - remove NoneType values
            if v is None: del final_options[k]
        # add options to final_options
        for k,v in options.items():
            # also - replace bool with "yes"/"no"
            if v is not None: final_options[k] = BOOL_REPLACE.get(v, v)

        resp = self._request(endpoint, **final_options)

        if not resp[1].status_code < 400:
            # raise errors yay
            error_data = resp[0]["error"]
            code = error_data["code"]
            status = resp[1].status_code
            msg = error_data["message"]

            if code == 1006: raise NoLocationFound(status, code, msg)
            elif code == 2006: raise InvalidAPIKey(status, code, msg)
            elif code == 2007: raise APILimitExceeded(status, code, msg)
            elif code == 2008: raise APIKeyDisabled(status, code, msg)
            elif code == 2009: raise AccessDenied(status, code, msg)
            elif code == 9999: raise InternalApplicationError(status, code, msg)
            else: raise WeatherAPIException(status, code, msg)

        full_url = str(self.url + endpoint + utils.parse_kwargs_to_urlargs({**self.default_options, **final_options}))
        self.on_api_call_successful(full_url, resp[1])
        return resp
    
    def on_error(self, func: str, exc: Exception) -> None:
        """Default implementation of error handling in this client.
        
        Parameters
        ---------------
        func: :class:`str`
            Name of function that raised an error
        exc: :exc:`Exception`
            Exception that was caught during func callback
        """
        print(f"Exception occured during \"{func}\":\n\n{traceback.format_exc()}")
    
    def event(self, func: Callable[P, T]) -> Callable[P, T]:
        """A decorator that turns a function into an event. For example

        .. code:: python

            import weatherly
            client = weatherly.Client(api_key=...)

            @client.event
            def on_error(func, exc):
                print(f"An error occured! Function: {func}, error: {str(exc)}")
        
        In the example above, by adding ``@client.event`` the ``on_error`` function has turned into an error handler function
        
        .. important::
        
            The function **SHOULD NOT** be a coroutine function!
        """
        if inspect.iscoroutinefunction(func):
            raise ValueError("Event functions should not be coroutines")
        
        # overwrite default client event implementation to user's func
        setattr(self, func.__name__, func)
        return func

    def set_language(self, lang: Union[str, Languages]) -> Optional[Languages]:
        """Set client's language when requesting data.
        
        Parameters
        -----------
        lang: Union[:class:`str`, :class:`Languages`]
            Language to set. Can be either a string that is lanuage's name or code or a :class:`Languages` enum object.
            
        Returns
        ---------
        Optional[:class:`Languages`]
            An enum class representing the language of the client. Is ``None`` when something went wrong and the language was not set.
        """
        try:
            lang_class = utils.find_language(lang, asobj=True)
        except Exception as exc:
            self.on_error("set_language", exc)
        if not lang_class:
            return None

        self.lang = lang_class 
        return self.lang

    def get_current_weather(self, 
        query: str, 
        *,
        lang: Optional[Union[str, Languages]] = None,
        aqi: Optional[bool] = None,
        **kwargs: Dict[str, Any]
    ) -> CurrentWeatherData:
        """Get current weather data

        Parameters
        ----------
        query: :class:`str`
            Query string - location you want to get weather data for
        lang: Optional[Union[:class:`str`, Languages]]
            Language from the :class:`Languages` enum or a string representing the language or language code (preferably).
            To get a list of languages visit :class:`Languages`.
        aqi: Optional[:class:`bool`]
            Enable/Disable Air Quality data in forecast API output. If nothing is passed, then it defaults to client default value.
        kwargs: Dict[:class:`str`, Any]
            Additional keyword arguments to request

        Returns
        -------
        :class:`CurrentWeatherData`
            Current weather data class

        Raises
        ---------
        :exc:`NoLocationFound`
            Raised when no location for given query was found
        :exc:`InvalidAPIKey`
            Raised when the API key is invalid
        :exc:`APILimitExceeded`
            Raised when API key calls limit was exceeded
        :exc:`APIKeyDisabled`
            Raised when API key is disabled
        :exc:`AccessDenied`
            Raised when access to given resource was denied
        :exc:`InternalApplicationError`
            Raised when there was a very rare internal application error
        :exc:`WeatherAPIException`
            Raised when something else went wrong, that does not have a specific exception class.
        """
        options = {
            "aqi": aqi or self.aqi,
            "q": query,
            **kwargs
        }
        if lang is not None: options["lang"] = lang
        try:
            resp = self._call_request("current.json", options)

            weather = CurrentWeatherData(resp[0], resp[1].status_code, None)
            return weather
        except Exception as exc:
            self.on_error("get_current_weather", exc)

    def get_locations(self, query: str):
        """Get locations for given query

        Parameters
        ---------------
        query: :class:`str`
            Query string, a location you are searching for

        Returns
        -----------
        List[:class:`LocationData`]
            A list of :class:`LocationData` classes.

        Raises
        ---------
        :exc:`NoLocationFound`
            Raised when no location for given query was found
        :exc:`InvalidAPIKey`
            Raised when the API key is invalid
        :exc:`APILimitExceeded`
            Raised when API key calls limit was exceeded
        :exc:`APIKeyDisabled`
            Raised when API key is disabled
        :exc:`AccessDenied`
            Raised when access to given resource was denied
        :exc:`InternalApplicationError`
            Raised when there was a very rare internal application error
        :exc:`WeatherAPIException`
            Raised when something else went wrong, that does not have a specific exception class.
        """
        try:
            resp = self._call_request("search.json",{"q": query})

            locations = []
            for loc in resp[0]:
                locations.append(LocationData(loc, resp[1].status_code, None))
            return locations
        except Exception as exc:
            self.on_error("get_locations", exc)

    def get_forecast_data(
        self,
        query: str, 
        days: int,
        *,
        aqi: Optional[bool] = None,
        alerts: Optional[bool] = None,
        lang: Optional[Union[str, Languages]] = None,
        **kwargs: Dict[str, Any]
    ) -> ForecastData:
        """Get forecast data from Forecast API

        Parameters
        -------------
        query: :class:`str`
            Query string, location you want to get forecast data for
        days: :class:`int`
            Number of days of weather forecast. Value ranges from 1 to 10
        aqi: Optional[:class:`bool`]
            Enable/Disable Air Quality data. Defaults to ``None`` (will use client's default)
        alerts: Optional[:class:`bool`]
            Enable/Disable alerts data. Defaults to ``None`` (will use client's default)
        lang: Optional[Union[:class`str`, :class`Languages`]]
            Language from the :class:`Languages` enum or a string representing the language or language code (preferably).
            To get a list of languages visit :class:`Languages`.
        kwargs: Dict[:class:`str`, Any]
            Additional keyword arguments that will be passed to the request.
            
        Returns
        ----------
        :class:`ForecastData`
            Fetched forecast data as a class.

        Raises
        ---------
        :exc:`NoLocationFound`
            Raised when no location for given query was found
        :exc:`InvalidAPIKey`
            Raised when the API key is invalid
        :exc:`APILimitExceeded`
            Raised when API key calls limit was exceeded
        :exc:`APIKeyDisabled`
            Raised when API key is disabled
        :exc:`AccessDenied`
            Raised when access to given resource was denied
        :exc:`InternalApplicationError`
            Raised when there was a very rare internal application error
        :exc:`WeatherAPIException`
            Raised when something else went wrong, that does not have a specific exception class.
        """
        options = {
            "aqi": aqi or self.aqi,
            "q": query,
            "alerts": alerts or self.kwargs.get("alerts"),
            "days": days,
            **kwargs
        }
        if lang is not None: options["lang"] = lang

        try:
            resp = self._call_request("forecast.json", options)
            forecast = ForecastData(resp[0], resp[1].status_code, None)
            return forecast
        except Exception as exc:
            self.on_error("get_forecast_data", exc)

    def get_historical_data(
        self,
        query: str,
        date: str,
        *,
        aqi: Optional[bool] = None,
        alerts: Optional[bool] = None,
        lang: Optional[Union[str, Languages]] = None,
        **kwargs: Dict[str, Any]
    ) -> ForecastData:
        """Retrieve historical data for given day and query. Uses History API.

        Parameters
        -----------------
        query: :class:`str`
            Query string, location you want to get forecast data for
        date: :class:`str`
            A date string in format yyyy-mm-dd representing the day you want to get data for
        aqi: Optional[:class:`bool`]
            Enable/Disable Air Quality data. Defaults to ``None`` (will use client's default)
        alerts: Optional[:class:`bool`]
            Enable/Disable alerts data. Defaults to ``None`` (will use client's default)
        lang: Optional[Union[:class`str`, :class`Languages`]]
            Language from the :class:`Languages` enum or a string representing the language or language code (preferably).
            To get a list of languages visit :class:`Languages`.
        kwargs: Dict[:class:`str`, Any]
            Additional keyword arguments that will be passed to the request.
        
        Returns
        ----------
        :class:`ForecastData`
            Forecast data for given day and query.

        Raises
        ---------
        :exc:`NoLocationFound`
            Raised when no location for given query was found
        :exc:`InvalidAPIKey`
            Raised when the API key is invalid
        :exc:`APILimitExceeded`
            Raised when API key calls limit was exceeded
        :exc:`APIKeyDisabled`
            Raised when API key is disabled
        :exc:`AccessDenied`
            Raised when access to given resource was denied
        :exc:`InternalApplicationError`
            Raised when there was a very rare internal application error
        :exc:`WeatherAPIException`
            Raised when something else went wrong, that does not have a specific exception class.
        :exc:`InvalidDate`
            Raised when the ``date`` parameter is invalid (doesn't match the format or isn't a date before (or) today)
        """
        options = {
            "aqi": aqi or self.aqi,
            "q": query,
            "alerts": alerts or self.kwargs.get("alerts"),
            "dt": date,
            **kwargs
        }
        if lang is not None: options["lang"] = lang
        try:
            # check if given date is really "historical"
            try:
                splitted = date.split("-")
                datetuple = datetime.datetime(
                    int(splitted[0]), 
                    int(splitted[1][1:]) if splitted[1].startswith("0") else int(splitted[1]), 
                    int(splitted[2][1:]) if splitted[2].startswith("0") else int(splitted[2]),
                    0,0)
                epoch = datetuple.timestamp()
            except Exception as exc:
                raise InvalidDate(f"Failed to convert date {date}: Invalid format") from exc

            now = datetime.datetime.timestamp(datetime.datetime.utcnow())

            if epoch > now: raise InvalidDate("Date should be before current time, switch from History API to Future to use future dates.")

            resp = self._call_request("history.json", options)
            history = ForecastData(resp[0], resp[1].status_code, None)
            return history
        except Exception as exc:
            self.on_error("get_historical_data", exc)
        
    def get_future_data(
        self,
        query: str,
        date: str,
        *,
        lang: Optional[Union[str, Languages]] = None,
        **kwargs: Dict[str, Any]
    ) -> FutureData:
        """Retrieve future data for given day and query. Uses Future API.

        Parameters
        -----------------
        query: :class:`str`
            Query string, location you want to get forecast data for
        date: :class:`str`
            A date string in format yyyy-mm-dd representing the day you want to get data for
        lang: Optional[Union[:class`str`, :class`Languages`]]
            Language from the :class:`Languages` enum or a string representing the language or language code (preferably).
            To get a list of languages visit :class:`Languages`.
        kwargs: Dict[:class:`str`, Any]
            Additional keyword arguments that will be passed to the request.
        
        Returns
        ----------
        :class:`FutureData`
            Future data for given day and query.

        Raises
        ---------
        :exc:`NoLocationFound`
            Raised when no location for given query was found
        :exc:`InvalidAPIKey`
            Raised when the API key is invalid
        :exc:`APILimitExceeded`
            Raised when API key calls limit was exceeded
        :exc:`APIKeyDisabled`
            Raised when API key is disabled
        :exc:`AccessDenied`
            Raised when access to given resource was denied
        :exc:`InternalApplicationError`
            Raised when there was a very rare internal application error
        :exc:`WeatherAPIException`
            Raised when something else went wrong, that does not have a specific exception class.
        :exc:`InvalidDate`
            Raised when the ``date`` parameter is invalid (doesn't match the format or isn't a date after today)
        """
        options = {
            "q": query,
            "dt": date,
            **kwargs
        }
        if lang is not None: options["lang"] = lang
        
        try:
            # check if given date is really "historical"
            try:
                splitted = date.split("-")
                datetuple = datetime.datetime(
                    int(splitted[0]), 
                    int(splitted[1][1:]) if splitted[1].startswith("0") else int(splitted[1]), 
                    int(splitted[2][1:]) if splitted[2].startswith("0") else int(splitted[2]),
                    0,0)
                epoch = datetuple.timestamp()
            except Exception as exc:
                raise InvalidDate(f"Failed to convert date {date}: Invalid format") from exc

            now = datetime.datetime.timestamp(datetime.datetime.utcnow())

            if epoch < now: raise InvalidDate("Date should be after current time, switch from Future API to History to use past dates.")

            resp = self._call_request("future.json", options)
            future = FutureData(resp[0], resp[1].status_code, None)
            return future
        except Exception as exc:
            self.on_error("get_future_data", exc)
        
    def get_astronomical_data(
        self,
        query: str,
        date: str,
        **kwargs: Dict[str, Any]
    ) -> AstronomicalData:
        """Get astronomical data from Astronomy API

        Parameters
        -------------
        query: :class:`str`
            Query string, location you want to get forecast data for
        date: :class:`str`
            Date in format yyyy-MM-dd and on or after 1st Jan, 2010 (2010-01-01)
        kwargs: Dict[:class:`str`, Any]
            Additional keyword arguments that will be passed to the request.
            
        Returns
        ----------
        :class:`AstronomicalData`
            Fetched astronomical data as a class.

        Raises
        ---------
        :exc:`NoLocationFound`
            Raised when no location for given query was found
        :exc:`InvalidAPIKey`
            Raised when the API key is invalid
        :exc:`APILimitExceeded`
            Raised when API key calls limit was exceeded
        :exc:`APIKeyDisabled`
            Raised when API key is disabled
        :exc:`AccessDenied`
            Raised when access to given resource was denied
        :exc:`InternalApplicationError`
            Raised when there was a very rare internal application error
        :exc:`WeatherAPIException`
            Raised when something else went wrong, that does not have a specific exception class.
        """
        options = {
            "q": query,
            "dt": date,
            **kwargs
        }
        try:
            resp = self._call_request("astronomy.json", options)
            astro = AstronomicalData(resp[0], resp[1].status_code, None)
            return astro
        except Exception as exc:
            self.on_error("get_astronomical_data", exc)

    def get_marine_data(
        self,
        query: str,
        *,
        tides: Optional[bool] = None,
        **kwargs: Dict[str, Any]
    ) -> MarineData:
        """Get marine data from Marine API

        Parameters
        -------------
        query: :class:`str`
            Query string, location you want to get forecast data for
        tides: Optional[:class:`bool`]
            Enable/disable tide data.
        kwargs: Dict[:class:`str`, Any]
            Additional keyword arguments that will be passed to the request.
            
        Returns
        ----------
        :class:`MarineData`
            Fetched marine data as a class.

        Raises
        ---------
        :exc:`NoLocationFound`
            Raised when no location for given query was found
        :exc:`InvalidAPIKey`
            Raised when the API key is invalid
        :exc:`APILimitExceeded`
            Raised when API key calls limit was exceeded
        :exc:`APIKeyDisabled`
            Raised when API key is disabled
        :exc:`AccessDenied`
            Raised when access to given resource was denied
        :exc:`InternalApplicationError`
            Raised when there was a very rare internal application error
        :exc:`WeatherAPIException`
            Raised when something else went wrong, that does not have a specific exception class.
        """
        options = {
            "q": query,
            "tides": tides or self.tides,
            **kwargs
        }
        try:
            resp = self._call_request("marine.json", options)
            marine = MarineData(resp[0], resp[1].status_code, None)
            return marine
        except Exception as exc:
            self.on_error("get_marine_data", exc)

    def get_ip_data(
        self,
        ip_address: str,
        **kwargs: Dict[str, Any]
    ) -> IPData:
        """
        Look for data for the given IP address.

        Parameters
        -------------
        ip_address: :class:`str`
            IP address you want to get data for. Can be ipv4 or ipv6
        kwargs: Dict[:class:`str`, Any]
            Additional keyword arguments that will be passed to the request.
            
        Returns
        ----------
        :class:`IPData`
            Fetched IP data as a class.

        Raises
        ---------
        :exc:`NoLocationFound`
            Raised when either IP address was invalid or no matching location was found.
        :exc:`InvalidAPIKey`
            Raised when the API key is invalid
        :exc:`APILimitExceeded`
            Raised when API key calls limit was exceeded
        :exc:`APIKeyDisabled`
            Raised when API key is disabled
        :exc:`AccessDenied`
            Raised when access to given resource was denied
        :exc:`InternalApplicationError`
            Raised when there was a very rare internal application error
        :exc:`WeatherAPIException`
            Raised when something else went wrong, that does not have a specific exception class.
        """
        options = {
            "q": ip_address,
            **kwargs
        }
        try:
            resp = self._call_request("ip.json", options)
            ip = IPData(resp[0], resp[1].status_code, None)
            return ip
        except Exception as exc:
            self.on_error("get_ip_data", exc)

    def get_sports_data(
        self,
        query: str,
        **kwargs: Dict[str, Any]
    ) -> SportsData:
        """
        Get sports data for a given query. Uses Sports API.

        Parameters
        -------------
        query: :class:`str`
            Query string, location you want to get sports data for
        kwargs: Dict[:class:`str`, Any]
            Additional keyword arguments that will be passed to the request.
            
        Returns
        ----------
        :class:`SportsData`
            Retrieved sports data as a class.

        Raises
        ---------
        :exc:`NoLocationFound`
            Raised when no matching location was found.
        :exc:`InvalidAPIKey`
            Raised when the API key is invalid
        :exc:`APILimitExceeded`
            Raised when API key calls limit was exceeded
        :exc:`APIKeyDisabled`
            Raised when API key is disabled
        :exc:`AccessDenied`
            Raised when access to given resource was denied
        :exc:`InternalApplicationError`
            Raised when there was a very rare internal application error
        :exc:`WeatherAPIException`
            Raised when something else went wrong, that does not have a specific exception class.
        """
        options = {
            "q": query,
            **kwargs
        }
        try:
            resp = self._call_request("sports.json", options)
            sports = SportsData(resp[0], resp[1].status_code, None)
            return sports
        except Exception as exc:
            self.on_error("get_sports_data", exc)
            
    def bulk_request(
        self,
        data: BulkRequest,
        **kwargs
    ) -> BulkResponse:
        """A bulk request allowing you to retrieve data for multiple locations at once
        
        .. note::
            Bulk requests only work on one endpoint, so you cannot use it to get data from multiple endpoints e.g. forecast and current weather
            
        .. note::
            To do a bulk request you should build a :class:`BulkRequest` object and pass it as a data parameter first
            
        Parameters
        --------------
        data: :class:`BulkRequest`
            Data for the bulk request.
            To build this class consider using two following methods:
            
            .. code:: python
                import weatherly
                
                # 1. by BulkRequest.build
                req = BulkRequest.build(("my-id", "London"), ("second", "Paris"), endpoint=weatherly.WeatherEndpoints.CURRENT_WEATHER)
                
                # 2. by manually setting bulk request params
                bulk = BulkRequest()
                bulk.add_endpoint(weatherly.WeatherEndpoints.FORECAST)
                bulk.add_query(id="my-id", location="Paris")
                bulk.add_query(id="second", location="London")
        kwargs: Dict[:class:`str`, Any]
            Additional keyword arguments. You need to think of them manually, look for them in other methods and pass them in ``key=val`` schema.
            For example: ``client.bulk_request(req, aqi=True, days=7)``
        
        Returns
        ----------
        :class:`BulkResponse`
            Results of the bulk request

        Raises
        ---------
        :exc:`NoLocationFound`
            Raised when no matching location was found.
        :exc:`InvalidAPIKey`
            Raised when the API key is invalid
        :exc:`APILimitExceeded`
            Raised when API key calls limit was exceeded
        :exc:`APIKeyDisabled`
            Raised when API key is disabled
        :exc:`AccessDenied`
            Raised when access to given resource was denied
        :exc:`InternalApplicationError`
            Raised when there was a very rare internal application error
        :exc:`WeatherAPIException`
            Raised when something else went wrong, that does not have a specific exception class.
        """
        pass
    
    def __str__(self):
        return f"<{self.__class__.__name__} api_key={self.default_options['key']} lang={self.lang}>"
    
    def __repr__(self):
        return repr(self.__str__())
    