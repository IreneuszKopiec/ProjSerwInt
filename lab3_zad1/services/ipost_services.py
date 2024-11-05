from abc import ABC
from typing import Iterable
from domains.posts import PostsRecord

class IPostsService(ABC):

    async def fetch_and_store_posts(self) -> None:
        pass


    def filter_posts(self, keyword: str) -> Iterable[PostsRecord]:
        pass