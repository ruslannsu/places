import os
import yaml
from dotenv import load_dotenv
from ui.view.view import View
from ui.controller.controller import Controller
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from features.place import PlaceFinder




class PlacesApp:
    def __init__(self):
        load_dotenv()
        self._places_api_key = os.getenv('PLACES_API_KEY')

        self._config = self._load_config('config.yaml')

        app = QApplication([])

        self.view = View('PLACES', self._config['main_window_size']['height'], self._config['main_window_size']['width'])

        self._place_finder = PlaceFinder(place_api_key=self._places_api_key)

        self.controller = Controller(self.view, self._place_finder)


        app.exec()

    def _load_config(self, path: str):
        with open(path, 'r') as f:
            return yaml.safe_load(f)  

  

        