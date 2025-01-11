#Aluno: Anderson S M Machado

import asyncio
import aiohttp
import time

start_time = time.time()

async def download_url(session, url):
    async with session.get(url) as response:
        #content = await response.text()
        pokemon = await response.json()
        print(f"Downloaded {url}: pokemon->"+pokemon['name'])#{len(content)} bytes")

async def main():
    async with aiohttp.ClientSession() as session:
        for number in range(1, 151):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            await asyncio.gather(download_url(session, url))

asyncio.run(main())
print("--- %s segundos ---" % (time.time() - start_time))