
from typing import List, Iterable
from repositories.posts_repository import PostsRepository
from services.ipost_services import IPostsService
from domains.posts import PostsRecord


class PostsService(IPostsService):
    repository: PostsRepository


    def __init__(self, repository: PostsRepository) -> None:
        self.repository = repository
        self.posts: List[PostsRecord] = []

    async def fetch_and_store_posts(self) -> None:
        posts = await self.repository.get_all_posts()
        if posts is not None:
            self.posts = posts


    def filter_posts(self, keyword: str) -> Iterable[PostsRecord]:
        return [
            post for post in self.posts
            if keyword.lower() in post.title.lower() or keyword.lower() in post.body.lower()
        ]