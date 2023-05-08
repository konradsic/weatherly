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

from .base import PartialAPIResponse

__all__ = (
    "AirQualityData",
    "GB_DEFRA_BAND",
)

GB_DEFRA_BAND = ("Low", "Low", "Low", "Moderate", "Moderate", "Moderate", "High", "High", "High", "Very High")

class AirQualityData(PartialAPIResponse):
    """Air Quality data

    Attributes
    --------------
    raw: Dict[:class:`str`, Any]
        Raw response in a JSON-like format (converted to a python dictionary)
    co: :class:`float`
        Carbon Monoxide (μg/m3)
    o3: :class:`float`
        Ozone (μg/m3)
    no2: :class:`float`	
        Nitrogen dioxide (μg/m3)
    so2: :class:`float`
        Sulphur dioxide (μg/m3)
    pm2_5: :class:`float`
        PM2.5 (μg/m3)
    pm10: :class:`float`
        PM10 (μg/m3)
    us_epa_index: :class:`int`
        US - EPA standard.
            * 1 means Good
            * 2 means Moderate
            * 3 means Unhealthy for sensitive group
            * 4 means Unhealthy
            * 5 means Very Unhealthy
            * 6 means Hazardous
    gb_defra_index: :class:`int`
        UK Defra Index
        
        +--------+------+-------+-------+----------+----------+----------+-------+-------+-------+------------+
        | Index  | 1    | 2     | 3     | 4        | 5        | 6        | 7     | 8     | 9     | 10         |
        +========+======+=======+=======+==========+==========+==========+=======+=======+=======+============+
        | Band   | Low  | Low   | Low   | Moderate | Moderate | Moderate | High  | High  | High  | Very High  |
        +--------+------+-------+-------+----------+----------+----------+-------+-------+-------+------------+
        | µgm^-3 | 0-11 | 12-23 | 24-35 | 36-41    | 42-47    | 48-53    | 54-58 | 59-64 | 65-70 | 71 or more |
        +--------+------+-------+-------+----------+----------+----------+-------+-------+-------+------------+
    
    gb_defra_band: :class:`str`
        A band corresponding to the :py:attr:`~gb_defra_index`
    """
    def __init__(
        self,
        raw: Dict[str, Any],
    ) -> None:
        super().__init__(raw)
        
        self.co: float = raw["co"]
        self.o3: float = raw["o3"]
        self.no2: float = raw["no2"]
        self.so2: float = raw["so2"]
        self.pm2_5: float = raw["pm2_5"]
        self.pm10: float = raw["pm10"]
        self.us_epa_index: int = raw["us-epa-index"]
        self.gb_defra_index: int = raw["gb-defra-index"]

        self.gb_defra_band: str = GB_DEFRA_BAND[self.gb_defra_index-1]