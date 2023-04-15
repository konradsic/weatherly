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
from ..errors import WeatherAPIException
from ..abc import ResponseModel
from .. import (
    utils as utils
)

from typing import (
    Any,
    Literal,
    Dict,
    Optional
)

WEATHERAPI_BASE_URL = "http://api.weatherapi.com/v1/"

class WeatherAPIClient(BaseAPIClient):
    """
    A WeatherAPI.com client for fetching various weather information

    Parameters
    ----------
    api_key: :class:`str`
        API Key used to authenticate when sending requests
    lang: Optional[:class:`str`]

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
    response_format: Literal["XML", "JSON"]
        Response format for requests made by the client. Defaults to JSON
    kwargs: Dict[:class:`str`, Any]
        Additional keyword arguments passes by default to requests made by the client
    """
    def __init__(
        self,
        api_key: str,
        lang: Optional[str],
        dt: Optional[int],
        end_dt: Optional[int],
        hour: Optional[int],
        aqi: Literal["yes", "no"] = "no",
        tides: Literal["yes", "no"] = "no",
        response_format: Literal["XML", "JSON"] = "JSON",
        **kwargs: Dict[str, Any]
    ) -> None:
        lang_code = utils.find_language(lang)
        opts = {
            "api_key": api_key,
        }
        if lang_code: opts.update(lang=lang_code)

        super().__init__(base_url=WEATHERAPI_BASE_URL,
                         default_options=opts)
        
        self.dt = dt
        self.end_dt = end_dt
        self.hour = hour
        self.aqi = aqi
        self.tides = tides
        self.response_format = response_format