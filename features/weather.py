import asyncio
from aiohttp import ClientSession

class Weather:
    def __init__(self, weather_api_key: str) -> None:
        self.weather_api_key = weather_api_key
    
    def set_coord(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def format_weather(self, data):
        name = data['name']
        country = data['sys']['country']
        temp = int(data['main']['temp'] - 273.15)
        feels_like = int(data['main']['feels_like'] - 273.15)
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        
        return f"""Погода в {name}, {country}:Температура: {temp}°C (ощущается как {feels_like}°C)
                                            Погодные условия: {description}
                                            Ветер: {wind_speed} м/с
                                            Влажность: {humidity}%
                                            Давление: {pressure} гПа"""    



    async def get_weather(self):
        async with ClientSession() as session:
            url = f'https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={self.weather_api_key}'

            async with session.get(url=url) as response:
                self.resp  = await response.json()
                return self.format_weather(self.resp)




        
        






