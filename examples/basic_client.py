# This example shows how to create a client and get current weather data. 

import weatherly
import os

# one common way to store an API Key is environment variable
# example of getting it from env assuming you've set it before
API_KEY = os.environ.get('API_KEY')

client = weatherly.Client(api_key=API_KEY)

# get current weather data
query = "Paris"

current_weather = client.get_current_weather(query, aqi=True) # add air quality data to the response
location = current_weather.location

print(f"Retrieved current weather data for: {location.name} ({location.region} {location.country})")
print("===================")
print(f"Temp: {current_weather.temp_c}°C, Feels like: {current_weather.feelslike_c}°C")