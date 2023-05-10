# this example shows how to create a custom client class, 
# add functions and handlers,
# and create an input loop so user can query current weather data 
# feel free to modify this example to fit your needs

import weatherly
from traceback import format_exc # for formatting traceback

class BetterClient(weatherly.Client):
    def __init__(self, api_key, *args, **kwargs):
        super().__init__(api_key=api_key, *args, **kwargs)

    def on_error(self, func, exc):
        # error handler
        print(f"[ERROR] exception in {func}:\n{exc.__class__.__name__}: {str(exc)}{format_exc()}")

    def on_api_call_successful(self, req, res):
        # inform a user about the successful call
        # find endpoint and flags, print a message
        parts = req.split("/")[4] # access only the endpoint
        endpoint, flags = parts.split("?")
        endpoint = endpoint[:-len(".json")] # remove .json at the end

        final_flags = ""
        for flag in flags.split("&"):
            k, v = flag.split("=")
            if k != "key":
                final_flags += k + "=" + v + " " # add to string

        print(f"[INFO] Request for endpoint {endpoint} with flags {final_flags}successful (status code {res.status_code})")

    def handle_query(self, method, query, **kwargs):
        print(f"Handling {query}...")
        res = getattr(self, method)(query, **kwargs)
        print("Success!")
        return res

client = BetterClient(api_key="your-api-key")
while True:
    # loop
    q = input("Enter query: ")
    res = client.handle_query("get_current_weather", q, aqi=True)
    print("Results:\n===================================")
    print(f"Weather ({res.condition_text}): temp {res.temp_c}C, feelslike {res.feelslike_c}C. Wind dir: {res.wind_dir}, speed {res.wind_kph}kph")
    aqi = res.aqi
    print(f"Air Quality (in μg/m3): CO {aqi.co:.1f}, SO2 {aqi.so2:.1f}, NO2 {aqi.no2:.1f}, PM2.5 {aqi.pm2_5:.1f}, PM10 {aqi.pm10:.1f}. Band: GB - {aqi.gb_defra_band}, USA - {aqi.us_epa_band}\n\n") # add newlines before the new query