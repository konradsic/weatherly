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

from .core import BaseAPIClient
from ..enums import Languages
from ..responses import CurrentWeatherData, LocationData
from ..errors import (
    WeatherAPIException,
    NoLocationFound,
    InvalidAPIKey,
    APILimitExceeded,
    APIKeyDisabled,
    AccessDenied,
    InternalApplicationError
)
from .. import (
    utils as utils
)

from typing import (
    Any,
    Literal,
    Dict,
    Optional,
    Union,
    List
)

WEATHERAPI_BASE_URL = "http://api.weatherapi.com/v1/"

__all__ = (
    "WeatherAPIClient",
)

class WeatherAPIClient(BaseAPIClient):
    """
    A WeatherAPI.com client for fetching various weather information

    Parameters
    ----------
    api_key: :class:`str`
        API Key used to authenticate when sending requests
    lang: Optional[ Union[:class:`str`, :class:`Languages`] ]
        Language from the :class:`Languages` enum or a string representing the language or language code (preferably).
        To get a list of languages visit :class:`Languages`.
    dt: Optional[:class:`int`]
        Restrict date output for Forecast and History API method. (Required for History and Future API)
    end_dt: Optional[:class:`int`]
        Restrict date output for History API method. Only works for API on Pro plan and above. (Available for History API)
    hour: Optional[:class:`int`]
        Restricting forecast or history output to a specific hour in a given day.
    aqi: Literal["yes", "no"]
        Enable/Disable Air Quality data in forecast API output. Defaults to "no".
    tides: Literal["yes", "no"]
        Enable/Disable Tide data in Marine API output. Defaults to "no".
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
        aqi: Literal["yes", "no"] = "no",
        tides: Literal["yes", "no"] = "no",
        **kwargs: Dict[str, Any]
    ) -> None:
        lang_code = None
        if lang is not None: 
            lang_code = utils.find_language(lang)
        opts = {
            "key": api_key,
            **kwargs
        }
        if lang_code: opts.update(lang=lang_code)

        super().__init__(base_url=WEATHERAPI_BASE_URL,
                         default_options=opts)
        
        self.dt = dt
        self.end_dt = end_dt
        self.hour = hour
        self.aqi = aqi
        self.tides = tides
        self.kwargs = kwargs
    
    def _call_request(self, endpoint: str, options: Dict[str, Any]) -> Dict[str, Any]:
        """Private method used to make requests to WeatherAPI"""
        final_options = self.default_options.copy()

        for k,v in final_options.items(): # check - remove NoneType values
            if v is None: del final_options[k]
        # add options to final_options
        for k,v in options.items():
            if v is not None: final_options[k] = v

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

        return resp

    def get_current_weather(self, 
        query: str,
        lang: Optional[Union[str, Languages]] = None,
        aqi: Literal["yes", "no", None] = None,
        **kwargs: Dict[str, Any]
    ) -> CurrentWeatherData:
        """
        Get current weather data

        Parameters
        ----------
        query: :class:`str`
            Query string - location you want to get weather data for
        lang: Optional[Union[:class:`str`, Languages]]
            Language from the :class:`Languages` enum or a string representing the language or language code (preferably).
            To get a list of languages visit :class:`Languages`.
        aqi: Literal["yes", "no", None]
            Enable/Disable Air Quality data in forecast API output. If nothing is passes, then it defaults to client default value.
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
        resp = self._call_request("current.json", options)

        weather = CurrentWeatherData(resp[0]["current"], resp[1].status_code, None)
        return weather

    def get_locations(self, query: str):
        """
        Get locations for given query

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
        resp = self._call_request("search.json",{"q": query})

        locations = []
        for loc in resp[0]:
            locations.append(LocationData(loc, resp[1].status_code, None))
        return locations