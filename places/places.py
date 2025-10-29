import os
import yaml
from dotenv import load_dotenv
from ui.view.view import View
from ui.controller.controller import Controller
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from features.place import PlaceFinder
from features.weather import Weather
from features.interest import FindInteresting


class PlacesApp:
    def __init__(self):
        load_dotenv()
        self._places_api_key = os.getenv('PLACES_API_KEY')
        self._weather_api_key = os.getenv('WEATHER_API_KEY')
        self._int_api_key = os.getenv('INT_API_KEY')

        self._config = self._load_config('config.yaml')

        app = QApplication([])

        self._view = View('PLACES', self._config['main_window_size']['height'], self._config['main_window_size']['width'])
        self._place_finder = PlaceFinder(place_api_key=self._places_api_key)
        self._weather = Weather(self._weather_api_key)
        self._int_places = FindInteresting(self._int_api_key)

        self._controller = Controller(self._view, self._place_finder, self._weather, self._int_places)


        app.exec()

    def _load_config(self, path: str):
        with open(path, 'r') as f:
            return yaml.safe_load(f)  

  

        