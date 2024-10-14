import asyncio

async def danie(krojenie: int, gotowanie: int, smazenie: int) -> None:
    print("Rozpoczęto krojenie warzyw (czas: " +str(krojenie)+")")
    await asyncio.sleep(krojenie)
    print("Rozpoczęto gotowanie warzyw (czas: " + str(gotowanie) + ")")
    await asyncio.sleep(gotowanie)
    print("Rozpoczęto smażenie warzyw (czas: " + str(smazenie) + ")")
    await asyncio.sleep(smazenie)
async def run() -> None:
    await asyncio.gather(danie(2,8,3), danie(1,3,5),
                         danie(3,2,4))


if __name__ == "__main__":
     asyncio.run(run())
