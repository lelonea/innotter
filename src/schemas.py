from enum import Enum

from pydantic import BaseModel
from typing import Optional, List


class BlogCategoryEnum(Enum):
    NEW = "New"
    PROMOTED = "Promoted"
    ACTUAL = "Actual"
    DELETED = "Deleted"


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str = "Some title"
    content: str
    nb_comments: int
    published: Optional[bool]
    image: Optional[Image]
    category: BlogCategoryEnum = BlogCategoryEnum.NEW


class UpdateBlogModel(BaseModel):
    title: Optional[str]
    content: Optional[str]
    image: Optional[Image]


class BlogResponseModel(BaseModel):
    blog: BlogModel
    id: int
    comment_title: str
    comment_id: int
    versions_list: List[str]


class UserSchema(BaseModel):
    username: str
    email: str
    password: str


class UserDisplaySchema(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True


class UserUpdateSchema(BaseModel):
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]

    class Config:
        orm_mode = True


