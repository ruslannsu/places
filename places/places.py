import os
import yaml
from dotenv import load_dotenv
from ui.view.view import View
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow




class PlacesApp:
    def __init__(self):
        load_dotenv()
        self.__places_api_key = os.getenv('PLACES_API_KEY')

        self._config = self._load_config('config.yaml')

        

        app = QApplication([])

        self.view = View(self._config['main_window_size']['height'], self._config['main_window_size']['width'])
    
        app.exec()

    def _load_config(self, path: str):
        with open(path, 'r') as f:
            return yaml.safe_load(f)  

    def run(self):
        pass
                

        