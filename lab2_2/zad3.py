import aiohttp
import asyncio

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def download(link: str) -> None:
    url = link
    users = await fetch(url)

    print(users)
    print()


async def main() -> None:
    await asyncio.gather(download("https://670bef0e7e5a228ec1cf1824.mockapi.io/api/v1/user"),
                         download("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"),
                         download("https://pokeapi.co/api/v2/"),
                         download("https://api.chess.com/pub/player/hikaru"),
                         download("http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataAdvancedPlayoffs/name/Kyrie Irving")
                         )

if __name__ == "__main__":
    asyncio.run(main())
