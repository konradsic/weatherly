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
    Optional,
    List
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
    location: ResponseModel # should inherit from this, actually its "weatherly.LocationData"
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
    
    The following classes implement this ABC:
    - :class:`~weatherly.LocationData`

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
    
class AirQuality(ResponseModel):
    """An ABC that provides information about air quality for a specific location.
    
    The following classes implement this ABC:
    - :class:`~weatherly.AirQualityData`
    
    Attributes
    --------------
    co: :class:`float`
        Carbon Monoxide (μg/m3)
    o3: :class`float`
        Ozone (μg/m3)
    no2: :class`float`	
        Nitrogen dioxide (μg/m3)
    so2: :class`float`
        Sulphur dioxide (μg/m3)
    pm2_5: :class`float`
        PM2.5 (μg/m3)
    pm10: :class`float`
        PM10 (μg/m3)
    us_epa_index: :class`int`
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
    """
    co: float
    o3: float
    no2: float
    so2: float
    pm2_5: float
    pm10: float
    us_epa_index: int
    gb_defra_index: int

class ForecastHourModel(ResponseModel):
    """
    An ABC defining a base forecast hour model from WeatherAPI

    The following classes implement this ABC:
    - :class:`~weatherly.ForecastHour`

    Attributes
    -------------
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
    aqi: Optional[:class:`AirQuality`]
        Air Quality data. See :class:`AirQualityData` for more info.
    """
    time_epoch: int
    time: str
    temp_c: float
    temp_f: float
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
    windchill_c: float
    windchill_f: float
    headindex_c: float
    headindex_f: float
    dewpoint_c: float
    dewpoint_f: float
    will_it_rain: bool
    will_it_snow: bool
    is_day: bool
    vis_km: float
    vis_miles: float
    chance_of_rain: int
    chance_of_snow: int
    gust_mph: float
    gust_kph: float
    uv: float

    aqi: Optional[AirQuality]
    

class ForecastDayModel(ResponseModel):
    """
    An ABC defining a base forecast day model from WeatherAPI

    The following classes implement this ABC:
    - :class:`~weatherly.ForecastDay`

    Attributes
    -------------
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
    maxwind_mph: :class:`float`
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
    hour_data: List[:class:`ForecastHourModel`]
        A list of :class:`ForecastHourModel` objects representing hourly weather data.
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
    aqi: Optional[:class:`AirQuality`]
        Air Quality data as :class:`AirQuality` object. Can be ``None``
    """
    date: str
    date_epoch: int
    # day
    maxtemp_c: float
    maxtemp_f: float
    mintemp_c: float
    mintemp_f: float
    avgtemp_c: float
    avgtemp_f: float

    maxwind_mph: float
    maxwind_mph: float

    totalprecip_mm: float
    totalprecip_in: float

    avgvis_km: float
    avgvis_miles: float
    avghumidity: int
    uv: int

    condition_text: str
    condition_icon: str
    condition_code: int
    # astro data
    sunrise: Optional[str]
    sunset: Optional[str]
    moonrise: Optional[str]
    moonset: Optional[str]
    moon_phase: Optional[str]
    moon_illumination: Optional[float]
    # aqi
    aqi: Optional[AirQuality]

    hour_data: List[ForecastHourModel]


class AlertModel(ResponseModel):
    """
    An ABC defining a base alert model from WeatherAPI

    The following classes implement this ABC:
    - :class:`~weatherly.AlertData`

    Attributes
    -------------
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
    headline: str
    msg_type: str
    severity: str
    urgency: str
    areas: str
    category: str
    certainty: str
    event: str
    note: str
    effective: str
    expires: str
    description: str
    instruction: str

class ForecastModel(ResponseModel):
    """
    An ABC defining a base response from Forecast API.

    The following classes implement this ABC:
    - :class:`~weatherly.ForecastData`
    
    Attributes
    -------------
    location: :class:`LocationModel`
        Location of the forecast data.
    forecast_days: List[:class:`ForecastDayModel`]
        A list of forecast days
    alerts: List[:class:`AlertModel`]
        A list of alerts, this list can be empty
    """
    location: LocationModel
    forecast_days: List[ForecastDayModel]
    alerts: List[AlertModel]