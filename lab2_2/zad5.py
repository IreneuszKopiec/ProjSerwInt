import aiohttp
import asyncio

async def fetch(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data['current']['temperature_2m']




async def main() -> None:
    urls = { "Porlamar": "https://api.open-meteo.com/v1/forecast?latitude=28.66&longitude=56.62&current=temperature_2m&forecast_days=1",
             "Moroni": "https://api.open-meteo.com/v1/forecast?latitude=7.78&longitude=18.22&current=temperature_2m&forecast_days=1",
             "Helsinki": "https://api.open-meteo.com/v1/forecast?latitude=10.27&longitude=7.62&current=temperature_2m&forecast_days=1"}

    tasks = [fetch(url) for url in urls.values()]
    results = await asyncio.gather(*tasks)

    users = {city: result for city, result in zip(urls.keys(), results)}

    print(users)





if __name__ == "__main__":
    asyncio.run(main())