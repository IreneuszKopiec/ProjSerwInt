import aiohttp
import asyncio

async def fetch(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            temperature = data['hourly']['temperature_2m']
            new_data =  await avgFunction(temperature)
            return new_data



async def avgFunction(list) -> float:
    suma = 0.0
    for el in list:
        suma += el;
    return suma/len(list)





async def main() -> None:
    urls = { "Porlamar": "https://api.open-meteo.com/v1/forecast?latitude=28.66&longitude=56.62&hourly=temperature_2m&start_date=2024-10-22&end_date=2024-10-22",
             "Moroni": "https://api.open-meteo.com/v1/forecast?latitude=7.78&longitude=18.22&hourly=temperature_2m&start_date=2024-10-22&end_date=2024-10-22",
             "Helsinki": "https://api.open-meteo.com/v1/forecast?latitude=10.27&longitude=7.62&hourly=temperature_2m&start_date=2024-10-22&end_date=2024-10-22"}

    tasks = [fetch(url) for url in urls.values()]
    results = await asyncio.gather(*tasks)
    sort = sorted(results, reverse=True)

    users = {city: result for city, result in zip(urls.keys(), sort)}

    print(users)


if __name__ == "__main__":
    asyncio.run(main())