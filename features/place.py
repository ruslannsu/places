import asyncio
from aiohttp import ClientSession

class PlaceFinder:
    def __init__(self):
        pass

    async def _get_place(self, city: str):
        async with ClientSession() as session:
            url = ''
            params = {'q': city, 'key': '5c5fb604-9611-45ff-a21b-6b7114008f4d', 'limit': 1}

            async with session.get(url=url, params=params) as response:
                self.resp  = await response.json()
                print(self.resp)

async def start():
        await asyncio.create_task(w._get_place(' В'))


w = Place()

asyncio.run(main=start())




