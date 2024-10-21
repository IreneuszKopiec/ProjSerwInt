import aiohttp
import asyncio

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            dane = await response.json()
            location = [ dane['latitude'], dane['longitude'] ]
            timeZone = dane['timezone']
            currentWeather = [ dane['current']['time'], dane['current']['temperature_2m'], dane['current']['wind_speed_10m'] ]
            result =  f"{location}, {timeZone}, {currentWeather} "
            return result


async def main() -> None:
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    users = await fetch(url)

    file = open("wynik.txt", mode='w')
    file.write(users)
    file.close()

    print(users)


if __name__ == "__main__":
    asyncio.run(main())
















