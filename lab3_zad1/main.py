from dependency_injector.wiring import Provide
import asyncio
from container import Container
from services.ipost_services import IPostsService

async def main(service: IPostsService = Provide[Container.service]) -> None:

    await service.fetch_and_store_posts()

    all_posts = service.filter_posts("")
    print(f"All posts: {[post.__dict__ for post in all_posts]}")

    keyword = "dig"
    filtered_posts = service.filter_posts(keyword)
    print(f"Filtered posts: {[post.__dict__ for post in filtered_posts]}")

if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    asyncio.run(main())