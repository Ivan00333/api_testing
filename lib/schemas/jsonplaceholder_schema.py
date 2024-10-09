from typing import Optional
from pydantic import BaseModel

class JsonplaceholderSchema(BaseModel):
    userId: int
    id: int
    title: str
    body: str

class JsonplaceholderListing(BaseModel):
    postId: int
    id: int
    name: str
    email: str
    body: str