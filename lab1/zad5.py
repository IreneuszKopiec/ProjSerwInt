import asyncio


async def main(n: int) -> None:  # 1
    if(n>0):

      p = 1
      d = 1
      i = n-2
      if (n == 1):
          print(p)
          await asyncio.sleep(1)
      elif (n == 2):
          await main(1)
          print(d)
          await asyncio.sleep(1)
      else:
          await main(2)
          while i>0:
              result = p+d
              print(result)
              await asyncio.sleep(1)
              p=d
              d=result
              i=i-1




if __name__ == "__main__":
    asyncio.run(main(5))