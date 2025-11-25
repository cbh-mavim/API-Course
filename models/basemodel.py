from enum import Enum
from pydantic import BaseModel,Field
from typing import Optional

class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


class BlogModel(BaseModel):
    title:str = Field(min_length=4,max_length=10)
    content:str = Field(min_length=10,max_length=100)
    nb_comments: int = Field(gt=0)
    published: Optional[bool] = None