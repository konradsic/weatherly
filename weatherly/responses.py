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

from .abc import (
    CurrentWeather, 
    LocationModel, 
    AirQuality, 
    ForecastDayModel, 
    ForecastHourModel, 
    ForecastModel,
    AlertModel,
)
from typing import (
    Dict,
    Any,
    Union,
    Optional,
    List, 
    Iterator,   
)

__all__ = (
    "CurrentWeatherData",
    "LocationData",
    "AirQualityData",
    "ForecastData",
    "ForecastDay",
    "ForecastHour",
    "AlertData",
)


GB_DEFRA_BAND = ("Low", "Low", "Low", "Moderate", "Moderate", "Moderate", "High", "High", "High", "Very High")

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
        super().__init__()
        
        self.status = status
        self.code = code
        self.raw = raw
        
        self.location = LocationData(raw["location"], status, code)
        raw = raw["current"]
        
        self.aqi = AirQualityData(raw["air_quality"], status, code) if raw.get("air_quality") else None
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
    code: Optional[:class:`int`]
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
        code: Optional[int]
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


class AirQualityData(AirQuality):
    """
    Attributes
    --------------
    raw: Dict[:class:`str`, Any]
        Raw response in a JSON-like format (converted to a python dictionary)
    status: :class:`int`
        HTTP status of the response. 200 is OK, and is the most common status.
    code: Optional[:class:`int`]
        Response code. In some cases this can be ``None``
    co: :class:`float`
        Carbon Monoxide (μg/m3)
    o3: :class:`float`
        Ozone (μg/m3)
    no2: :class`float`	
        Nitrogen dioxide (μg/m3)
    so2: :class:`float`
        Sulphur dioxide (μg/m3)
    pm2_5: :class`float`
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
        A band corresponding to the :ref:`gb_defra_index`
    """
    def __init__(
        self,
        raw: Dict[str, Any],
        status: int,
        code: Optional[int]
    ) -> None:
        self.raw = raw
        self.status = status
        self.code = code
        
        self.co = raw["co"]
        self.o3 = raw["o3"]
        self.no2 = raw["no2"]
        self.so2 = raw["so2"]
        self.pm2_5 = raw["pm2_5"]
        self.pm10 = raw["pm10"]
        self.us_epa_index = raw["us-epa-index"]
        self.gb_defra_index = raw["gb-defra-index"]

        self.gb_defra_band = GB_DEFRA_BAND[self.gb_defra_index-1]

class AlertData(AlertModel):
    """
    An alert from WeatherAPI

    Attributes
    -------------
    raw: Dict[:class:`str`, Any]
        Raw response in a JSON-like format (converted to a python dictionary)
    status: :class:`int`
        HTTP status of the response. 200 is OK, and is the most common status.
    code: Optional[:class:`int`]
        Response code. In some cases this can be ``None``
    headline: :class:`str`
        Alert headline
    msg_type: :class:`str`
        Type of alert
    severity: :class:`str`
        Severity of alert
    urgency: :class:`str`
        Urgency
    areas: :class:`str`
        Areas covered
    category: :class:`str`
        Category
    certainty: :class:`str`
        Certainty
    event: :class:`str`
        Event
    note: :class:`str`
        Note
    effective: :class:`str`
        Effective
    expires: :class:`str`
        Expires
    description: :class:`str`
        Description
    instruction: :class:`str`
        Instruction
    """
    def __init__(
        self,
        raw: Dict[str, Any],
        status: int,
        code: Optional[int]
    ) -> None:
        self.raw = raw
        self.status = status
        self.code = code
        
        self.headline = raw["headline"]
        self.msg_type = raw["msgType"]
        self.severity = raw["severity"]
        self.urgency = raw["urgency"]
        self.areas = raw["areas"]
        self.category = raw["category"]
        self.certainty = raw["certainty"]
        self.event = raw["event"]
        self.note = raw["note"]
        self.effective = raw["effective"]
        self.expires = raw["expires"]
        self.description = raw["desc"]
        self.instruction = raw["instruction"]

class ForecastHour(ForecastHourModel):
    """
    Forecast hour, an element of :class:`ForecastDay`
    
    Attributes
    -------------
    raw: Dict[:class:`str`, Any]
        Raw response in a JSON-like format (converted to a python dictionary)
    status: :class:`int`
        HTTP status of the response. 200 is OK, and is the most common status.
    code: Optional[:class:`int`]
        Response code. In some cases this can be ``None``
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
    uv: :class:`float`
        UV Index
    aqi: Optional[:class:`AirQualityData`]
        Air Quality data. See :class:`AirQualityData` for more info.
    """
    def __init__(
        self,
        raw: Dict[str, Any],
        status: int,
        code: Optional[int]
    ) -> None:
        self.raw = raw
        self.status = status
        self.code = code

        self.time_epoch = raw["time_epoch"]
        self.time = raw["time"]
        self.temp_c = raw["temp_c"]
        self.temp_f = raw["temp_f"]
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
        self.windchill_c = raw["windchill_c"]
        self.windchill_f = raw["windchill_f"]
        self.heatindex_c = raw["heatindex_c"]
        self.heatindex_f = raw["heatindex_f"]
        self.dewpoint_c = raw["dewpoint_c"]
        self.dewpoint_f = raw["dewpoint_f"]
        self.will_it_rain = bool(raw["will_it_rain"])
        self.will_it_snow = bool(raw["will_it_snow"])
        self.is_day = bool(raw["is_day"])
        self.vis_km = raw["vis_km"]
        self.vis_miles = raw["vis_miles"]
        self.chance_of_rain = raw["chance_of_rain"]
        self.chance_of_snow = raw["chance_of_snow"]
        self.gust_mph = raw["gust_mph"]
        self.gust_kph = raw["gust_kph"]
        self.uv = raw["uv"]
        
        if raw.get("air_quality"): self.aqi = AirQualityData(raw["air_quality"], status, code)
        else: self.aqi = None
    
class ForecastDay(ForecastDayModel):
    """
    A forecast day, element of :class:`ForecastData`

    Attributes
    -------------
    raw: Dict[:class:`str`, Any]
        Raw response in a JSON-like format (converted to a python dictionary)
    status: :class:`int`
        HTTP status of the response. 200 is OK, and is the most common status.
    code: Optional[:class:`int`]
        Response code. In some cases this can be ``None``
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
    uv: :class:`int`
        UV Index
    condition_text: :class:`str`
        Weather condition text
    condition_icon: :class:`str`
        Weather condition icon
    condition_code: :class:`int`
        Weather condition code
    hour_data: List[:class:`ForecastHour`]
        A list of :class:`ForecastHour` objects representing hourly weather data.
    sunrise: :class:`str`
        Sunrise time
    sunset: :class:`str`
        Sunset time
    moonrise: :class:`str`
        Moonrise time
    moonset: :class:`str`
        Moonset time
    moon_phase: :class:`str`
        Moon phases. Value returned:
            * New Moon
            * Waxing Crescent
            * First Quarter
            * Waxing Gibbous
            * Full Moon
            * Waning Gibbous
            * Last Quarter
            * Waning Crescent
    moon_illumination: :class:`float`
        Moon illumination as %
    aqi: Optional[:class:`AirQualityData`]
        Air Quality data as :class:`AirQualityData` object. Can be ``None``
    """
    def __init__(
        self,
        raw: Dict[str, Any],
        status: int,
        code: Optional[int]
    ) -> None:
        self.raw = raw
        self.status = status
        self.code = code
        self.date = raw["date"]
        self.date_epoch = raw["date_epoch"]
        
        before_raw = raw.copy()
        raw = raw["day"]
        
        self.maxtemp_c = raw["maxtemp_c"]
        self.maxtemp_f = raw["maxtemp_f"]
        self.mintemp_c = raw["mintemp_c"]
        self.mintemp_f = raw["mintemp_f"]
        self.avgtemp_c = raw["avgtemp_c"]
        self.avgtemp_f = raw["avgtemp_f"]
        self.maxwind_mph = raw["maxwind_mph"]
        self.maxwind_kph = raw["maxwind_kph"]
        self.totalprecip_in = raw["totalprecip_in"]
        self.totalprecip_mm = raw["totalprecip_mm"]
        self.avgvis_km = raw["avgvis_km"]
        self.avgvis_miles = raw["avgvis_miles"]
        self.avghumidity = raw["avghumidity"]
        self.uv = raw["uv"]
        self.condition_text = raw["condition"]["text"]
        self.condition_icon = raw["condition"]["icon"]
        self.condition_code = raw["condition"]["code"]
        if raw.get("air_quality"): self.aqi = AirQualityData(raw["air_quality"], status, code)
        else: self.aqi = None
        
        raw = before_raw
        self.hour_data = list([
            ForecastHour(elem, status, code) for elem in raw["hour"]
        ])
        self.sunrise = raw["astro"]["sunrise"]
        self.sunset = raw["astro"]["sunset"]
        self.moonrise = raw["astro"]["moonrise"]
        self.moonset = raw["astro"]["moonset"]
        self.moon_phase = raw["astro"]["moon_phase"]
        self.moon_illumination = raw["astro"]["moon_illumination"]

    
class ForecastData(ForecastModel):
    """
    Forecast data returned from Forecast API
    
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
        self.raw = raw
        self.status = status
        self.code = code
        
        self.location = LocationData(raw["location"], status, code)
        self.forecast_days = list([ForecastDay(elem, status, code) for elem in raw["forecast"]["forecastday"]])
        self.alerts = []
        alert_data = raw.get("alerts", {})
        
        for k,v in alert_data.items():
            if v is not []:
                self.alerts.extend(list([
                    AlertData(elem, status, code) for elem in v
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
