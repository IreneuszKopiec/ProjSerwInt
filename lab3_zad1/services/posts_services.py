from collections.abc import Iterable

from repositories.posts_repository import PostsRepository
from services.ipost_services import IPostsService

#from utils.utils import PM10IndexEnum

class PostsService(IPostsService):
    repository: PostsRepository

    def __init__(self, repository: PostsRepository) -> None:
        self.repository = repository

    async def get_params(self) -> Iterable:
        all_posts_params = await self.repository.get_all_posts_params()
        return all_posts_params