from abc import ABC
from typing import Iterable
from domains.posts import PostsRecord


class IPostsRepository(ABC):

    async def get_all_posts(self) -> Iterable[PostsRecord] | None:
        pass