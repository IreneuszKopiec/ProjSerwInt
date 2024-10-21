import aiohttp
import asyncio

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main() -> None:
    url = "https://api.open-meteo.com/v1/forecast?latitude=49.3&longitude=19.95&current=temperature_2m&forecast_days=1"
    users = await fetch(url)

    print(users)


if __name__ == "__main__":
    asyncio.run(main())