from dataclasses import dataclass
from datetime import datetime

@dataclass
class PostsRecord:
    userID: int
    id: int
    title: str
    body: str


