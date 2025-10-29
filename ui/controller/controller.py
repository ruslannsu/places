from ui.view.view import View
from features.place import PlaceFinder
from features.weather import Weather
from features.interest import FindInteresting
import asyncio

class Controller:
    def __init__(self, view: View, place_finder: PlaceFinder, weather: Weather, int_places: FindInteresting) -> None:
        self.view = view
        self._place_finder = place_finder
        self._inter = int_places
        self._weather = weather

        view.set_text_button_handler(self.text_button_handler)
        
    async def run_weather_interesting_places(self) -> tuple:
        weather_task = asyncio.create_task(self._weather.get_weather())
        interest_task = asyncio.create_task(self._inter.get_places())
        results = await asyncio.gather(weather_task, interest_task)

        return results

    def text_button_handler(self) -> None:
        if (self.view.get_text_input_placeholder() != 'Сюда нужно что-то написать'):
            if (int(self.view.get_text_input()) == 1):
                
                self._weather.set_coord(self.main_resp[0][1]['lat'], self.main_resp[0][1]['lng'])
                self._inter.set_coord(self.main_resp[0][1]['lat'], self.main_resp[0][1]['lng'])
                
            if (int(self.view.get_text_input()) == 2):
                self._weather.set_coord(self.main_resp[1][1]['lat'], self.main_resp[1][1]['lng'])
                self._inter.set_coord(self.main_resp[1][1]['lat'], self.main_resp[1][1]['lng'])

            if (int(self.view.get_text_input()) == 3):
                self._weather.set_coord(self.main_resp[2][1]['lat'], self.main_resp[2][1]['lng'])
                self._inter.set_coord(self.main_resp[2][1]['lat'], self.main_resp[2][1]['lng'])
                
            out = asyncio.run(self.run_weather_interesting_places())
            self.view.set_area_text(out[0] + '\n' + str(out[1]))
            return

        self.main_resp = asyncio.run(self._place_finder.run(self.view.get_text_input()))[0]

        print(self.main_resp)
        places = '1:' + self.main_resp[0][0] + '   2:' + self.main_resp[1][0] + '3:   ' + self.main_resp[2][0]
        self.view.set_text_placeholder(places)

    
    
