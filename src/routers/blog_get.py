from enum import Enum

from fastapi import APIRouter, status
from starlette.exceptions import HTTPException
from starlette.status import HTTP_404_NOT_FOUND

router = APIRouter(prefix="/blog", tags=["blog"])


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@router.get('/all')
def get_all_blogs(page: int = 1, page_size: int = 10):
    return {'message': f'All {page_size} blogs on page {page/0}'}


@router.get('/type/{type}')
def get_blog_type(type: BlogType):
    """Some description"""
    return {'message': f'Blog type {type}'}


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int):
    if id > 5:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    else:
        return id

@router.get('/newblog/{id}')
def get_new_blog(id: int):
    if id == 7:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
