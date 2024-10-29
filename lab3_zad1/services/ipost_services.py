from abc import ABC


class IPostsService(ABC):
    async def get_all_posts_params(self) -> str:
        pass

