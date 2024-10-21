import aiohttp
import asyncio

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            status = response.status
            if status >= 500 and status < 600:
                new_status = fetch(url)
                if new_status >= 500 and new_status < 600:
                    new_status2 = fetch(url)
                    if new_status2 >= 500 and new_status2 < 600:
                        new_status3 = fetch(url)
                        if new_status3 >= 500 and new_status3 < 600:
                            return None
                        return new_status3
                    return new_status2
                return new_status
            return status


async def main() -> None:
    url = "https://pokeapi.co/api/v2/"
    tasks = [fetch(url)];
    for i in range(99):
        tasks.append(fetch(url))
    results = await asyncio.gather(*tasks)

    print(results)

    length = 0
    for i in results:
        if(i>=200 and i<=299):
            length+=1;

    print(length)

if __name__ == "__main__":
    asyncio.run(main())