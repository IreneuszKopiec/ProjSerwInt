import aiohttp
from typing import  List
from utils import consts
from domains.posts import PostsRecord
from repositories.iposts_repository import IPostsRepository

class PostsRepository(IPostsRepository):
    async def get_all_posts(self) -> List[PostsRecord] | None:
        all_params = await self._get_params()
        if all_params is None:
            return None
        parsed_params = self._parse_params(all_params)
        return parsed_params

    async def _get_params(self) -> List[dict] | None:
        async with aiohttp.ClientSession() as session:
            async with session.get(consts.API_SENSOR_URL) as response:
                if response.status != 200:
                    return None
                return await response.json()

    def _parse_params(self, params: List[dict]) -> List[PostsRecord]:
        return [
            PostsRecord(
                userID=record.get("userId"),
                id=record.get("id"),
                title=record.get("title"),
                body=record.get("body")
            ) for record in params
        ]