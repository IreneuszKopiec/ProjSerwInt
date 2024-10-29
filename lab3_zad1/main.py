from dependency_injector.wiring import Provide

import asyncio

from container import Container
from services.ipost_services import IPostsService
from utils import consts

async def main(
        service: IPostsService = Provide[Container.service],
) -> None:
    all = await service.get_params()


    print(f"Posty: {all}")


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    asyncio.run(main())