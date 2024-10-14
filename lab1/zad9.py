import asyncio

async def maszynaA() -> None:
    print("Działa maszyna A")
    await asyncio.sleep(3)

async def maszynaB() -> None:
    await maszynaA()
    print("Działa maszyna B")
    await asyncio.sleep(5)

async def maszynaC() -> None:
    await maszynaB()
    print("Działa maszyna C")
    await asyncio.sleep(7)

async def run() -> None:
    await asyncio.gather(maszynaC(),maszynaC(),maszynaC())


if __name__ == "__main__":
     asyncio.run(run())
