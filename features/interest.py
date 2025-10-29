import asyncio
from aiohttp import ClientSession

class FindInteresting:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def set_coord(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def parse_places_to_string(self, data):
        places = []
        
        for feature in data.get('features', []):
            properties = feature.get('properties', {})
            
            
            name = properties.get('formatted', '')
            if not name:
                
                street = properties.get('street', '')
                housenumber = properties.get('housenumber', '')
                city = properties.get('city', '')
                
                if street and housenumber:
                    name = f"{housenumber} {street}, {city}"
                elif street:
                    name = f"{street}, {city}"
                else:
                    name = city or 'Неизвестное место'
            
        
            if name and name not in places:
                places.append(name)
        
        result = "Найденные места:\n" + "\n".join(f" {place}" for place in places)
        return result

    async def get_places(self):
        async with ClientSession() as session:
            url = "https://api.geoapify.com/v2/places"
            params = {"filter": f"circle:{self.lon},{self.lat},{5000}",'apiKey': self.api_key, "type": "amenity" }

            async with session.get(url=url, params=params) as response:
                self.resp  = await response.json()
                return self.parse_places_to_string(self.resp)


        
        






