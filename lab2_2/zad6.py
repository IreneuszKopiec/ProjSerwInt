import aiohttp
import asyncio

async def fetch(url: str, mask: float) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            current = data['current']['temperature_2m']
            if current < mask['temperature_2m']:
                return current







async def main() -> None:
    urls = { "Porlamar": "https://api.open-meteo.com/v1/forecast?latitude=28.66&longitude=56.62&current=temperature_2m&forecast_days=1",
             "Moroni": "https://api.open-meteo.com/v1/forecast?latitude=7.78&longitude=18.22&current=temperature_2m&forecast_days=1",
             "Helsinki": "https://api.open-meteo.com/v1/forecast?latitude=10.27&longitude=7.62&current=temperature_2m&forecast_days=1"}

    mask = {
        "temperature_2m": 24.0
    }

    tasks = [fetch(url, mask) for url in urls.values()]
    results = await asyncio.gather(*tasks)

    users = {city: result for city, result in zip(urls.keys(), results)}

    for city, result in users.items():
        if(result != None):
            print(f"{city}: {result}")


if __name__ == "__main__":
    asyncio.run(main())