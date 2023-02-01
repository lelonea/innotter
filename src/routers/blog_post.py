from typing import List
from fastapi import APIRouter, Query, Path, Request

from src.schemas import BlogModel, BlogResponseModel, UpdateBlogModel, BlogCategoryEnum

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, request: Request, version: int = 1, ):
    return {'data': blog,
            'version': version,
            'id': id,
            'request': request.headers}


@router.post('/new/{blog_id}/comment/{comment_id}')
def create_comment(blog: BlogModel, blog_id: int = Path(None,
                                                        description='The ID of the blog to create a comment for'),
                   comment_title: str = Query("some comment",
                                              description='Some description for comment_id',
                                              alias='commentId',
                                              deprecated=True
                                              ),
                   version: List[int] = Query([1, 2, 3]),
                   comment_id: int = Path(None, gt=5)

                   ):
    return BlogResponseModel(blog=blog,
                             id=blog_id,
                             comment_title=comment_title,
                             comment_id=comment_id,
                             versions_list=version)

    #     {
    #     'blog': blog,
    #     'id': blog_id,
    #     'comment_title': comment_title,
    #     'comment_id': comment_id,
    #     'versions_list': version
    # }

@router.patch('/update/{blog_id}')
def update_blog(blog_id: int, blog: UpdateBlogModel):
    return {"updated_fields": blog.dict(exclude_unset=True),
            "blog_id": blog_id}
