import aiohttp

from typing import Iterable

from utils import consts
from domains.posts import PostsRecord
from repositories.iposts_repository import IPostsRepository

class PostsRepository(IPostsRepository):
    async def get_all_posts_params(self) -> Iterable[PostsRecord] | None:
     all_params = await self._get_params()
     parsed_params = await self._parse_params(all_params)

     return parsed_params

    async def _get_params(self) -> Iterable[dict] | None:
     async with aiohttp.ClientSession() as session:
         async with session.get(consts.API_SENSOR_URL) as response:
             if response.status != 200:
                 return None

             return await response.json()

    async def _parse_params(self, params: Iterable[dict]) -> Iterable[PostsRecord]:
     return [PostsRecord(userID=record.get("userID"), id=record.get("id"), title=record.get("title"), body=record.get("body")) for record in
            params["values"]]

