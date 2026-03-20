import asyncio
import aiohttp
import time

urls = [
    "https://example.com",
    "https://google.com",
    "https://github.com",
    "https://stackoverflow.com/questions",
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
}


async def fetch(session, url):
    async with session.get(url, headers=headers) as response:
        print(url, response.status)


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        await asyncio.gather(*tasks)


start = time.time()
asyncio.run(main())
print("Time:", time.time() - start)