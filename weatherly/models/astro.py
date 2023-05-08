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

__all__ = (
    "AstronomicalData",
)

class AstronomicalData(APIResponse):
    """Represents astronomical data as a response from WeatherAPI
    
    Attributes
    -----------
    raw: Dict[:class:`str`, Any]
        Raw response in a JSON-like format (converted to a python dictionary)
    status: :class:`int`
        HTTP status of the response. 200 is OK, and is the most common status.
    code: Optional[:class:`int`]
        Response code. In some cases this can be ``None``
    location: Optional[:class:`LocationData`]
        Location of the requested data. Is not ``None`` only if this object is returned from ``astronomy.json`` endpoint.
    sunrise: :class:`str`
        Sunrise local time
    sunset: :class:`str`
        Sunset local time
    moonrise: :class:`str`
        Moonrise local time
    moonset: :class:`str`
        Moonset local time
    moon_phase: Optional[:class:`str`]
        Moon phases. Value returned:
            * New Moon
            * Waxing Crescent
            * First Quarter
            * Waxing Gibbous
            * Full Moon
            * Waning Gibbous
            * Last Quarter
            * Waning Crescent
        
        Can be ``None``
    moon_illumination: Optional[:class:`int`]
        Moon illumination. Can be ``None``
    """
    def __init__(
        self,
        raw: Dict[str, Any],
        status: int,
        code: Optional[int],    
    ) -> None:
        super().__init__(raw, status, code)
        
        # there are two types of "raw" data we need to convert
        # 1. from astronomy.json 
        # 2. from other types of endpoints, e.g. forecast data
        # we set location to None to avoid errors
        self.location: Optional[LocationData] = None
                
        if raw.get("astronomy") is not None:
            # first type
            self.location = LocationData(raw["location"], status, code)
            raw = raw["astronomy"]["astro"]
        
        self.sunrise: str = raw["sunrise"]
        self.sunset: str = raw["sunset"]
        self.moonrise: str = raw["moonrise"]
        self.moonset: str = raw["moonset"]
        self.moon_phase: Optional[str] = raw.get("moon_phase")
        self.moon_illumination: Optional[int] = int(raw.get("moon_illumination")) if raw.get("moon_illumination") is not None else None
