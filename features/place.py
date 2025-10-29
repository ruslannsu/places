import asyncio
from aiohttp import ClientSession

class PlaceFinder:
    def __init__(self, place_api_key: str) -> None:
        self.place_api_key = place_api_key

    

    async def find_place(self, place: str):
        async with ClientSession() as session:
            url = 'https://graphhopper.com/api/1/geocode'
            params = {'q': place, 'key': self.place_api_key, 'limit': 2}

            async with session.get(url=url, params=params) as response:
                self.resp  = await response.json()
                names = [(hit['name'], hit['point']) for hit in self.resp['hits']]
                return names

    async def run(self, place: str):
        task = asyncio.create_task(self.find_place(place))

        results = await asyncio.gather(task)

        return results


        
        






