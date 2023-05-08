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
    Optional,
    Literal
)

from .base import APIResponse

__all__ = (
    "IPData",
)

class IPData(APIResponse):
    """Represents IP Data retuned from IP Lookup API
    
    Attributes
    ------------
    raw: Dict[:class:`str`, Any]
        Raw response in a JSON-like format (converted to a python dictionary)
    status: :class:`int`
        HTTP status of the response. 200 is OK, and is the most common status.
    code: Optional[:class:`int`]
        Response code. In some cases this can be ``None``
    ip: :class:`str`
        IP address
    type: Literal["ipv4", "ipv6"]
        Type of the IP address
    continent_code: :class:`str`
        Continent code
    continent_name: :class:`str`
        Continent name
    country_code: :class:`str`
        Country code
    country_name: :class:`str`
        Name of country
    is_eu: :class:`bool`
        Indicating if IP address is in Europe
    geoname_id: :class:`int`
        Geoname ID
    city: :class:`str`
        City name
    region: :class:`str`
        Region name
    latitude: :class:`float`
        Latitude in decimal degree
    longitude: :class:`float`
        Longitude in decimal degree
    tz_id: :class:`str`
        Time zone
    localtime_epoch: :class:`int`
        Local time epoch
    localtime_formatted: :class:`str`
        Formatted local time string (e.g. 2023-04-30 17:54)
    """
    def __init__(
        self,
        raw: Dict[str, Any],
        status: int,
        code: Optional[int]
    ) -> None:
        super().__init__(raw, status, code)
        
        self.ip: str = raw["ip"]
        self.type: Literal["ipv4", "ipv6"] = raw["type"]
        self.continent_code: str = raw["continent_code"]
        self.continent_name: str = raw["continent_name"]
        self.country_code: str = raw["country_code"]
        self.country_name: str = raw["country_name"]
        self.is_eu: bool = bool(raw["is_eu"])
        self.geoname_id: int = raw["geoname_id"]
        self.city: str = raw["city"]
        self.region: str = raw["region"]
        self.latitude: float = raw["lat"]
        self.longitude: float = raw["lon"]
        self.tz_id: str = raw["tz_id"]
        self.localtime_epoch: int = raw["localtime_epoch"]
        self.localtime_formatted: str = raw["localtime"]