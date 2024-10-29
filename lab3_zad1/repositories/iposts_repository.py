from abc import ABC
from typing import Iterable

from domains.posts import PostsRecord


class IPostsRepository(ABC):
    async def get_last_air_quality_params(self, sensor_id: int) -> PostsRecord | None:
        pass

    async def get_all_air_quality_params(self, sensor_id: int) -> Iterable[PostsRecord] | None:
        pass