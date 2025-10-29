from ui.view.view import View
from features.place import PlaceFinder
import asyncio

class Controller:
    def __init__(self, view: View, place_finder: PlaceFinder) -> None:
        self.view = view

        view.set_text_button_handler(self.text_button_handler)

        self._place_finder = place_finder

        
        

    def text_button_handler(self) -> None:
        
        resp = asyncio.run(self._place_finder.run(self.view.get_text_input()))

        print(resp[0])
        self.view.set_text_placeholder(str(resp[0]))

        
