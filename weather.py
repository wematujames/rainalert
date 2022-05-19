import requests
import os

# Open weather map 
OPWM_API_KEY = os.environ['OPWM_API_KEY']

class Weather ():
    def __init__(self, lat =-27.469770, lon = 153.025131 ) -> None:
        self.weather_data = None
        self.lat = lat
        self.lon = lon
        self.get_weather_today()
        
    
    def get_weather_today(self) -> None:
        params = {
            "lat": self.lat,
            "exclude": "current,daily,minutely",
            "lon": self.lon,
            "appid": OPWM_API_KEY
        }
        res = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall", params=params)
        res.raise_for_status()
        self.weather_data = res.json()


    def will_rain(self) -> bool:
        daily_hourly_data = self.weather_data["hourly"][0:12]
        for item in daily_hourly_data:
            if item["weather"][0]["id"] < 700:
                return True
        return False