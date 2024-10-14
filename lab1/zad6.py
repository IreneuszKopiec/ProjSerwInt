import asyncio

async def fetch(delay: int) -> None:
    print("Trwa pobieranie, czas pobierania: "+str(delay))
    await asyncio.sleep(delay)
    print("Zakończono pobieranie po: " +str(delay))

async def run() -> None:
    await asyncio.gather(fetch(5), fetch(1), fetch(7))


if __name__ == "__main__":
     asyncio.run(run())
