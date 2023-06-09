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
    Dict,
    Any,
    Optional
)

from .base import APIResponse
from .location import LocationData
from .air_quality import AirQualityData

__all__ = (
    "CurrentWeatherData",
)

class CurrentWeatherData(APIResponse):
    """Current weather data, a common return type from methods that requests this from WeatherAPI.com.
    
    Attributes
    ----------
    raw: Dict[:class:`str`, Any]
        Raw response in a JSON-like format (converted to a python dictionary)
    status: :class:`int`
        HTTP status of the response. 200 is OK, and is the most common status.
    code: Optional[:class:`int`]
        Response code. In some cases this can be ``None``
    location: :class:`LocationData`
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
    aqi: Optional[:class:`AirQualityData`]
        Air quality data. Can be ``None`` (if this field of data was not requested)
    """
    def __init__(
        self,
        raw: Dict[str, Any],
        status: int,
        code: Optional[int]
    ) -> None:
        super().__init__(raw, status, code)
        
        self.location: LocationData = LocationData(raw["location"], status, code)
        raw = raw["current"]
        
        self.aqi: Optional[AirQualityData] = AirQualityData(raw["air_quality"]) if raw.get("air_quality") else None
        self.last_updated_epoch: int = raw["last_updated_epoch"]
        self.temp_c: float = raw["temp_c"]
        self.temp_f: float = raw["temp_f"]
        self.is_day: bool = bool(raw["is_day"])
        self.condition_text: str = raw["condition"]["text"]
        self.condition_icon: str = raw["condition"]["icon"]
        self.condition_code: int = raw["condition"]["code"]
        self.wind_mph: float = raw["wind_mph"]
        self.wind_kph: float = raw["wind_kph"]
        self.wind_degree: int = raw["wind_degree"]
        self.wind_dir: str = raw["wind_dir"]
        self.pressure_mb: float = raw["pressure_mb"]
        self.pressure_in: float = raw["pressure_in"]
        self.precip_mm: float = raw["precip_mm"]
        self.precip_in: float = raw["precip_in"]
        self.humidity: int = raw["humidity"]
        self.cloud: int = raw["cloud"]
        self.feelslike_c: float = raw["feelslike_c"]
        self.feelslike_f: float = raw["feelslike_f"]
        self.uv: float = raw["uv"]