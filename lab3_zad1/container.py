from dependency_injector import containers, providers

from repositories.posts_repository import PostsRepository
from services.posts_services import PostsService

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    repository = providers.Singleton(
        PostsRepository,
    )

    service = providers.Factory(
        PostsService,
        repository=repository,
    )