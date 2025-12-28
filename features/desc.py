import asyncio
from aiohttp import ClientSession

class PlacesDescription:
    def __init__(self):
        return None
    
    async def get_wiki_description(self, place: dict) -> str:
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        async with ClientSession(headers=headers) as session:
            params = {
                "action": "query",
                "list": "geosearch",
                "gscoord": f"{place['lat']}|{place['lon']}",
                "gsradius": "1000",
                "gslimit": "1",
                "format": "json"
            }
            
            try:
                async with session.get("https://ru.wikipedia.org/w/api.php", 
                                    params=params, timeout=5) as resp:
                    
                    if resp.status == 200:
                        data = await resp.json()
                        pages = data.get('query', {}).get('geosearch', [])
                        
                        if pages:
                            page_id = str(pages[0]['pageid'])
                            content_params = {
                                "action": "query",
                                "prop": "extracts",
                                "pageids": page_id,
                                "exintro": "1",
                                "explaintext": "1",
                                "format": "json"
                            }
                            
                            async with session.get("https://ru.wikipedia.org/w/api.php", 
                                                params=content_params, timeout=5) as content_resp:
                                
                                if content_resp.status == 200:
                                    content_data = await content_resp.json()
                                    page = content_data.get('query', {}).get('pages', {}).get(page_id, {})
                                    
                                    extract = page.get('extract', '')
                                    if extract:
                                        return extract.split('\n')[0]
                                    
                                    return f"INFO: '{page.get('title', '')}'"
                        
                        return "No inf"
                    
                    return f"ERR: {resp.status}"
                    
            except Exception as e:
                return f"Conn err: {str(e)}"