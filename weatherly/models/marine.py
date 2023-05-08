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
    Iterator,
    List,
)

from .base import APIResponse, PartialAPIResponse
from .location import LocationData
from .forecast import ForecastHour
from .astro import AstronomicalData
from ..enums import TideHeight

__all__ = (
    "TideData",
    "MarineHour",
    "MarineDay",
    "MarineData",
)

class TideData(PartialAPIResponse):
    """Represents tide data, part of Marine API response
    
    Attributes
    --------------
    raw: Dict[:class:`str`, Any]
        Raw response in a JSON-like format (converted to a python dictionary)
    tide_time: :class:`str`
        Local tide time
    tide_height_mt: :class:`float`
        Tide height in meters
    tide_type: :class:`TideHeight`
        Type of height of the tide represented as a :class:`TideHeight` enum. Can be ``LOW`` or ``HIGH``
    """
    def __init__(self, 
        raw: Dict[str, Any], 
    ) -> None:
        super().__init__(raw)

        self.tide_time: str = raw["tide_time"]
        self.tide_height_mt: float = float(raw["tide_height_mt"])
        self.tide_type: TideHeight = getattr(TideHeight, raw["tide_type"].upper())

class MarineHour(ForecastHour):
    """Marine hour, part of :class:`MarineDay`, this class contains marine and forecast informations from a specific hour.
    Inherits from :class`ForecastData` to avoid more messy code

    Attributes
    ------------
    raw: Dict[:class:`str`, Any]
        Raw response in a JSON-like format (converted to a python dictionary)
    time_epoch: :class:`int`
        Time as epoch
    time: :class:`str`
        Date and time
    temp_c: :class:`float`
        Temperature in celsius
    temp_f: :class:`float`
        Temperature in fahrenheit
    condition_text: :class:`str`
        Weather condition text
    condition_icon: :class:`str`
        Weather condition icons
    condition_code: :class:`int`
        Weather condition code
    wind_mph: :class:`float`
        Maximum wind speed in miles per hour
    wind_kph: :class:`float`
        Maximum wind speed in kilometer per hour
    wind_degree: :class:`int`
        Wind direction in degrees
    wind_dir: :class:`str`
        Wind direction as 16 point compass. e.g.: NSW
    pressure_mb: :class:`float`
        Pressure in millibars
    pressure_in: :class:`float`
        Pressure in inches
    precip_mm: :class:`float`
        Precipitation amount in millimeters
    precip_in: :class:`float`
        Precipitation amount in inches
    humidity: :class:`int`
        Humidity as percentage
    cloud: :class:`int`
        Cloud cover as percentage
    feelslike_c: :class:`float`
        Feels like temperature as celcius
    feelslike_f: :class:`float`
        Feels like temperature as fahrenheit
    windchill_c: :class:`float`
        Windchill temperature in celcius
    windchill_f: :class:`float`
        Windchill temperature in fahrenheit
    headindex_c: :class:`float`
        Heat index in celcius
    headindex_f: :class:`float`
        Heat index in fahrenheit
    dewpoint_c: :class:`float`
        Dew point in celcius
    dewpoint_f: :class:`float`
        Dew point in fahrenheit
    is_day: :class:`bool`
        Whether to show day condition icon or night icon
    vis_km: :class:`float`
        Visibility in kilometer
    vis_miles: :class:`float`
        Visibility in miles
    gust_mph: :class:`float`
        Wind gust in miles per hour
    gust_kph: :class:`float`
        Wind gust in kilometer per hour
    uv: :class:`float`
        UV Index.
    sig_ht_mt: :class:`float`
        Significant wave height in metres
    swell_ht_mt: :class:`float`
        Swell wave height in metres
    swell_ht_ft: :class:`float`
        Swell wave height in feet
    swell_dir: :class:`float`
        Swell direction in degrees
    swell_dir_16_point: :class:`str`
        Swell direction in 16 point compass e.g. NNW
    swell_period_secs: :class:`float`
        Swell period in seconds
    water_temp_c: :class:`float`
        Water temperature in Celcius
    water_temp_f: :class:`float`
        Water temperature in Fahrenheit
    """
    def __init__(
        self,
        raw: Dict[str, Any],
    ) -> None:
        super().__init__(raw)
        # cleanup absent elements
        del self.aqi
        del self.will_it_rain
        del self.will_it_snow
        del self.chance_of_rain
        del self.chance_of_snow

        self.sig_ht_mt: float = raw["sig_ht_mt"]
        self.swell_ht_mt: float = raw["swell_ht_mt"]
        self.swell_ht_ft: float = raw["swell_ht_ft"]
        self.swell_dir: float = raw["swell_dir"]
        self.swell_dir_16_point: str = raw["swell_dir_16_point"]
        self.swell_period_secs: float = raw["swell_period_secs"]
        self.water_temp_c: float = raw["water_temp_c"]
        self.water_temp_f: float = raw["water_temp_f"]

class MarineDay(PartialAPIResponse):
    """Marine day, part of :class:`MarineData`, representing a single day with forecast information
    
    Attributes
    ------------
    raw: Dict[:class:`str`, Any]
        Raw response in a JSON-like format (converted to a python dictionary)
    date: :class:`str`
        Forecast date
    date_epoch: :class:`int`
        Forecast date as unix time.
    maxtemp_c: :class:`float`
        Maximum temperature in celsius for the day.
    maxtemp_f: :class:`float`
        Maximum temperature in fahrenheit for the day
    mintemp_c: :class:`float`
        Minimum temperature in celsius for the day
    mintemp_f: :class:`float`
        Minimum temperature in fahrenheit for the day
    avgtemp_c: :class:`float`
        Average temperature in celsius for the day
    avgtemp_f: :class:`float`
        Average temperature in fahrenheit for the day
    maxwind_mph: :class:`float`
        Maximum wind speed in miles per hour
    maxwind_kph: :class:`float`
        Maximum wind speed in kilometer per hour
    totalprecip_mm: :class:`float`
        Total precipitation in milimeter
    totalprecip_in: :class:`float`
        Total precipitation in inches
    avgvis_km: :class:`float`
        Average visibility in kilometer
    avgvis_miles: :class:`float`
        Average visibility in miles
    avghumidity: :class:`int`
        Average humidity as percentage
    uv: :class:`float`
        UV Index
    condition_text: :class:`str`
        Weather condition text
    condition_icon: :class:`str`
        Weather condition icon
    condition_code: :class:`int`
        Weather condition code
    hour_data: List[:class:`MarineHour`]
        A list of :class:`MarineHour` objects representing hourly weather data.
    astro: :class:`AstronomicalData`
        Astronomical data object
    tide_data: List[:class:`TideData`]
        A list of issues tides
    """
    def __init__(
        self,
        raw: Dict[str, Any],
    ) -> None:
        super().__init__(raw)

        self.date = raw["date"]
        self.date_epoch = raw["date_epoch"]
        
        before_raw = raw.copy()
        raw = raw["day"]
        
        self.maxtemp_c: float = raw["maxtemp_c"]
        self.maxtemp_f: float = raw["maxtemp_f"]
        self.mintemp_c: float = raw["mintemp_c"]
        self.mintemp_f: float = raw["mintemp_f"]
        self.avgtemp_c: float = raw["avgtemp_c"]
        self.avgtemp_f: float = raw["avgtemp_f"]
        self.maxwind_mph: float = raw["maxwind_mph"]
        self.maxwind_kph: float = raw["maxwind_kph"]
        self.totalprecip_in: float = raw["totalprecip_in"]
        self.totalprecip_mm: float = raw["totalprecip_mm"]
        self.avgvis_km: float = raw["avgvis_km"]
        self.avgvis_miles: float = raw["avgvis_miles"]
        self.avghumidity: int = raw["avghumidity"]
        self.uv: float = raw["uv"]
        self.condition_text: str = raw["condition"]["text"]
        self.condition_icon: str = raw["condition"]["icon"]
        self.condition_code: int = raw["condition"]["code"]

        _all_tides = []
        for tide in raw["tides"]:
            _all_tides.extend(tide["tide"])
        self.tide_data: List[TideData] = list([
            TideData(tidedata) for tidedata in _all_tides
        ])
        
        raw = before_raw
        self.hour_data = list([
            MarineHour(elem) for elem in raw["hour"]
        ])
        self.astro: AstronomicalData = AstronomicalData(raw["astro"], 0, None)
    

class MarineData(APIResponse):
    """Marine data, response from Marine API as a class
    
    Attributes
    ------------
    raw: Dict[:class:`str`, Any]
        Raw response in a JSON-like format (converted to a python dictionary)
    status: :class:`int`
        HTTP status of the response. 200 is OK, and is the most common status.
    code: Optional[:class:`int`]
        Response code. In some cases this can be ``None``
    location: :class:`LocationData`
        Location of the requested marine data
    marine_days: List[:class:`MarineDay`]
        A list of marine days for the requested period
    """
    def __init__(
        self,
        raw: Dict[str, Any],
        status: int,
        code: Optional[int]
    ) -> None:
        super().__init__(raw, status, code)
        
        self.location: LocationData = LocationData(raw["location"], status, code)
        self.marine_days: List[MarineDay] = list([
            MarineDay(daydata) for daydata in raw["forecast"]["forecastday"]
        ])

    def iter_hours(self) -> Iterator[MarineHour]:
        """
        Iterate over all possible hours from this class.

        .. container:: operations

            .. describe:: for x in y

                Iterate over hour data from this instance.

        Returns
        -------------
        Iterator[:class:`MarineHour`]
            A generator object you can iterate over made of :class:`MarineHour`
        """
        for day in self.marine_days:
            for hour in day.hour_data:
                yield hour
