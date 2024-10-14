import asyncio

async def plik(wczytanie: int, pobieranie: int, zapis: int) -> None:
    print("Wczytywanie (czas: " +str(wczytanie)+")")
    await asyncio.sleep(wczytanie)
    print("Koniec wczytywania")
    print("Pobieranie (czas: " + str(pobieranie) + ")")
    await asyncio.sleep(pobieranie)
    print("Koniec pobieranie")
    print("Zapis (czas: " + str(zapis) + ")")
    await asyncio.sleep(zapis)
    print("Koniec zapisu")
async def run() -> None:
    await asyncio.gather(plik(2,8,3), plik(1,3,5),
                         plik(3,2,4), plik(4,1,5),
                         plik(5,3,6))


if __name__ == "__main__":
     asyncio.run(run())
