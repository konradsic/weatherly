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

from typing import (
    Any,
    Literal,
    Dict,
    Optional
)
from abc import ABC

__all__ = (
    "ResponseModel",
    "CurrentWeather",
)

class ResponseModel(ABC):
    """
    ResponseModel is an ABC that defines a basic response model from WeatherAPI.
    Almost all models inherit from this class.
    
    Attributes
    ----------
    raw: Dict[:class:`str`, Any]
        Raw response in a JSON-like format (converted to a python dictionary)
    status: :class:`int`
        HTTP status of the response. 200 is OK, and is the most common status.
    code: Union[:class:`int`, None]
        Response code. In some cases this can be ``None``
    """
    raw: Dict[str, Any]
    status: int
    code: int | None

class CurrentWeather(ResponseModel):
    """
    An ABC defining current weather data.

    The following classes implement this ABC:
    - :class:`~weatherly.CurrentWeatherData`

    Attributes
    ------------
    location: :class:`~weatherly.LocationData`
        Location of the requested weather data
    last_updated_epoch: :class:`int`
        The timestamp when the weather data was last updated.
    temp_c: :class:`float`
        Weather temperature in Celsius
    temp_f: :class:`float`
        Weather temperature in Fahrenheit
    is_day: :class:`bool`
        Wherever the current time is considered day time.
    condition_text: :class:`str`
        Weather condition text
    condition_icon: :class:`str`
        Link to the weather condition icon
    condition_code: :class:`int`
        Code of current weather condition
    wind_mph: :class:`float`
        Current wind speed in miles per hour (mph)
    wind_kph: :class:`float`
        Current wind speed in kilometers per hour (kph)
    wind_degree: :class:`int`
        Direction of wind in degrees
    wind_dir: :class:`str`
        Direction of wind as a string (e.g. "W")
    pressure_mb: :class:`float`
        Pressure in millibars (mb)
    pressure_in: :class:`float`
        Pressure in inches (in)
    precip_mm: :class:`float`
        Precipation (water that is falling out of the sky) in millimeters (mm)
    precip_in: :class:`float`
        Precipation (water that is falling in the sky) in inches (in)
    humidity: :class:`int`
        Humidity in integer percentage
    cloud: :class:`int`
        Cloud cover as percentage
    feelslike_c: :class:`float`
        Feels like temperature in Celsius
    feelslike_f: :class:`float`
        Feels like temperature in Fahrenheit
    uv: :class:`float`
        UV Index
    """
    last_updated_epoch: int
    temp_c: float
    temp_f: float
    is_day: bool
    condition_text: str
    condition_icon: str
    condition_code: int
    wind_mph: float
    wind_kph: float
    wind_degree: int
    wind_dir: str
    pressure_mb: float
    pressure_in: float
    precip_mm: float
    precip_in: float
    humidity: int
    cloud: int
    feelslike_c: float
    feelslike_f: float
    uv: float

class LocationModel(ResponseModel):
    """An ABC that provides information about a location

    Attributes
    --------------
    id: :class:`int`
        A specific ID of the location. Can be ``None``
    name: :class:`str`
        Name of the location (e.g. London)
    region: :class:`str`
        A region of the location
    country: :class:`str`
        Country where the location is
    latitude: :class:`float`
        Latitude coordinate of the location
    longitude: :class:`float`
        Longitude coordinate of the location
    timezone_id: Optional[:class:`str`]
        Timezone ID of the location (e.g. Europe/London). Could be ``None`` when using the Search/Autocomplete API.
    localtime_epoch: Optional[:class:`int`]
        Local time of the location as a timestamp
    localtime_formatted: Optional[:class:`str`]
        Formatted local time of the location
    """
    id: Optional[int]
    name: str
    region: str
    country: str
    latitude: float
    longitude: float
    timezone_id: Optional[str]
    localtime_epoch: Optional[int]
    localtime_formatted: Optional[str]