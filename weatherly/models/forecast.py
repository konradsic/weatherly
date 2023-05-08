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
    List,
    Iterator
)

from .base import APIResponse, PartialAPIResponse
from .air_quality import AirQualityData
from .location import LocationData
from .astro import AstronomicalData
from .alert import AlertData

__all__ = (
    "ForecastHour",
    "ForecastDay",
    "ForecastData",
)

class ForecastHour(PartialAPIResponse):
    """Forecast hour, an element of :class:`ForecastDay`
    
    Attributes
    -------------
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
    will_it_rain: :class:`bool`
        Will it will rain or not
    will_it_snow: :class:`bool`
        Will it will snow or not
    is_day: :class:`bool`
        Whether to show day condition icon or night icon
    vis_km: :class:`float`
        Visibility in kilometer
    vis_miles: :class:`float`
        Visibility in miles
    chance_of_rain: :class:`int`
        Chance of rain as percentage
    chance_of_snow: :class:`int`
        Chance of snow as percentage
    gust_mph: :class:`float`
        Wind gust in miles per hour
    gust_kph: :class:`float`
        Wind gust in kilometer per hour
    uv: Optional[:class:`float`]
        UV Index. Can be ``None`` when this class is returned from Future API
    aqi: Optional[:class:`AirQualityData`]
        Air Quality data. See :class:`AirQualityData` for more info.
    """
    def __init__(
        self,
        raw: Dict[str, Any],
    ) -> None:
        super().__init__(raw)

        self.time_epoch: int = raw["time_epoch"]
        self.time: str = raw["time"]
        self.temp_c: float = raw["temp_c"]
        self.temp_f: float = raw["temp_f"]
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
        self.windchill_c: float = raw["windchill_c"]
        self.windchill_f: float = raw["windchill_f"]
        self.heatindex_c: float = raw["heatindex_c"]
        self.heatindex_f: float = raw["heatindex_f"]
        self.dewpoint_c: float = raw["dewpoint_c"]
        self.dewpoint_f: float = raw["dewpoint_f"]
        # when used for inheritance in MarineHour somehow these four are absent lol
        self.will_it_rain: bool = bool(raw.get("will_it_rain")) # type: ignore
        self.will_it_snow: bool = bool(raw.get("will_it_snow")) # type: ignore
        self.chance_of_rain: int = raw.get("chance_of_rain") # type: ignore
        self.chance_of_snow: int = raw.get("chance_of_snow") # type: ignore
        self.is_day: bool = bool(raw["is_day"])
        self.vis_km: float = raw["vis_km"]
        self.vis_miles: float = raw["vis_miles"]
        self.gust_mph: float = raw["gust_mph"]
        self.gust_kph: float = raw["gust_kph"]
        self.uv: Optional[float] = raw.get("uv")
        
        self.aqi: Optional[AirQualityData] = None
        if raw.get("air_quality"): 
            self.aqi: Optional[AirQualityData] = AirQualityData(raw["air_quality"])
    
class ForecastDay(PartialAPIResponse):
    """A forecast day, element of :class:`ForecastData`

    Attributes
    -------------
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
    uv: Optional[:class:`float`]
        UV Index. Can be ``None`` when this class is returned from Future API
    condition_text: :class:`str`
        Weather condition text
    condition_icon: :class:`str`
        Weather condition icon
    condition_code: :class:`int`
        Weather condition code
    hour_data: List[:class:`ForecastHour`]
        A list of :class:`ForecastHour` objects representing hourly weather data.
    astro: :class:`AstronomicalData`
        Astronomical data object
    aqi: Optional[:class:`AirQualityData`]
        Air Quality data as :class:`AirQualityData` object. Can be ``None``
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
        self.uv: Optional[float] = raw.get("uv")
        self.condition_text: str = raw["condition"]["text"]
        self.condition_icon: str = raw["condition"]["icon"]
        self.condition_code: int = raw["condition"]["code"]
        if raw.get("air_quality"): self.aqi: AirQualityData = AirQualityData(raw["air_quality"])
        else: self.aqi = None
        
        raw = before_raw
        self.hour_data = list([
            ForecastHour(elem) for elem in raw["hour"]
        ])
        self.astro: AstronomicalData = AstronomicalData(raw["astro"], 0, None)

    
class ForecastData(APIResponse):
    """Forecast data returned from Forecast API
    
    Attributes
    -------------
    raw: Dict[:class:`str`, Any]
        Raw response in a JSON-like format (converted to a python dictionary)
    status: :class:`int`
        HTTP status of the response. 200 is OK, and is the most common status.
    code: Optional[:class:`int`]
        Response code. In some cases this can be ``None``
    location: :class:`LocationData`
        Location of the forecast data.
    forecast_days: List[:class:`ForecastDay`]
        A list of forecast days
    alerts: List[:class:`AlertData`]
        A list of alerts, this list can be empty. List is also empty, when the user disabled alerts in the request.
    """
    def __init__(
        self,
        raw: Dict[str, Any],
        status: int,
        code: Optional[int]
    ) -> None:
        super().__init__(raw, status, code)
        
        self.location: LocationData = LocationData(raw["location"], status, code)
        self.forecast_days: List[ForecastDay] = list([ForecastDay(elem) for elem in raw["forecast"]["forecastday"]])
        self.alerts: List[AlertData] = []
        alert_data = raw.get("alerts", {})
        
        for k,v in alert_data.items():
            if v is not []:
                self.alerts.extend(list([
                    AlertData(elem) for elem in v
                ]))
    
    def iter_hours(self) -> Iterator[ForecastHour]:
        """
        Iterate over all possible hours from this class.

        .. container:: operations

            .. describe:: for x in y

                Iterate over hour data from this instance.

        Returns
        -------------
        Iterator[:class:`ForecastHour`]
            A generator object you can iterate over made of :class:`ForecastHour`
        """

        for day in self.forecast_days:
            for hour in day.hour_data:
                yield hour

