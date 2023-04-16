import requests
from config import OPENWEATHER_TOKEN

class Weather:
    def __init__(self):
        self.TOKEN = OPENWEATHER_TOKEN
        self.lat = 55.5433
        self.lon = 37.5483

    def get_weather_for_now(self):
        params = {'units': 'metric',
                  'lang': 'ru'}
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={self.TOKEN}'
        weather_now = requests.get(url, params=params)
        return weather_now.json()

    def get_weather_info(self):
        weather_data = self.get_weather_for_now()
        feels_like = weather_data['main']['feels_like']
        temp = weather_data['main']['temp']
        wind_speed = weather_data['wind']['speed']
        return feels_like, temp, wind_speed

    def print_info_on_russian(self):
        feels_like, temp, wind_speed = self.get_weather_info()
        msg = f'Погодка сейчас такая себе: градусов-то всего: {temp}, но из-за ' \
              f'ебейшего ветра в {wind_speed} метров в секуду, ' \
              f'ощущается на {feels_like}'
        return msg

