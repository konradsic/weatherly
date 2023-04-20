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

from .abc import CurrentWeather, LocationModel
from typing import (
    Dict,
    Any,
    Union
)

__all__ = (
    "CurrentWeatherData",
    "LocationData",
)

class CurrentWeatherData(CurrentWeather):
    """
    Current weather data, a common return type from methods that requests this from WeatherAPI.com.
    
    Please note, that only ``condition_text`` is translated into requested language.

    Attributes
    ----------
    raw: Dict[:class:`str`, Any]
        Raw response in a JSON-like format (converted to a python dictionary)
    status: :class:`int`
        HTTP status of the response. 200 is OK, and is the most common status.
    code: Union[:class:`int`, None]
        Response code. In some cases this can be ``None``
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
    def __init__(
        self,
        raw: Dict[str, Any],
        status: int,
        code: Union[int, None]
    ) -> None:
        super().__init__()
        
        self.status = status
        self.code = code
        self.raw = raw
        self.last_updated_epoch = raw["last_updated_epoch"]
        self.temp_c = raw["temp_c"]
        self.temp_f = raw["temp_f"]
        self.is_day = bool(raw["is_day"])
        self.condition_text = raw["condition"]["text"]
        self.condition_icon = raw["condition"]["icon"]
        self.condition_code = raw["condition"]["code"]
        self.wind_mph = raw["wind_mph"]
        self.wind_kph = raw["wind_kph"]
        self.wind_degree = raw["wind_degree"]
        self.wind_dir = raw["wind_dir"]
        self.pressure_mb = raw["pressure_mb"]
        self.pressure_in = raw["pressure_in"]
        self.precip_mm = raw["precip_mm"]
        self.precip_in = raw["precip_in"]
        self.humidity = raw["humidity"]
        self.cloud = raw["cloud"]
        self.feelslike_c = raw["feelslike_c"]
        self.feelslike_f = raw["feelslike_f"]
        self.uv = raw["uv"]

class LocationData(LocationModel):
    """
    Location data, returned with most requests.
    
    Attributes
    --------------
    raw: Dict[:class:`str`, Any]
        Raw response in a JSON-like format (converted to a python dictionary)
    status: :class:`int`
        HTTP status of the response. 200 is OK, and is the most common status.
    code: Union[:class:`int`, None]
        Response code. In some cases this can be ``None``
    id: Optional[:class:`int`]
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
    def __init__(
        self, 
        raw: Dict[str, Any],
        status: int,
        code: Union[int, None]
    ) -> None:
        self.raw = raw
        self.status = status
        self.code = code

        self.id = raw.get('id', None)
        self.name = raw['name']
        self.region = raw['region']
        self.country = raw['country']
        self.latitude = raw['lat']
        self.longitude = raw['lon']
        self.timezone_id = raw.get('tz_id', None)
        self.localtime_epoch = raw.get('localtime_epoch')
        self.localtime_formatted = raw.get('localtime', None)