from dataclasses import dataclass

@dataclass
class PostsRecord:
    userID: int
    id: int
    title: str
    body: str

