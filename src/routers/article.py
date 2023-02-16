from typing import List

from auth.oauth2 import oauth2_schema, get_current_user
from schemas import ArticleBase, ArticleDisplay, UserSchema, Article, UserDisplaySchema
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article

router = APIRouter(
    prefix='/article',
    tags=['article']
)


# Create article
@router.post('/', status_code=201)
def create_article(payload: ArticleBase, db: Session = Depends(get_db)):
    if db_article.create_article(db, payload):
        return {"message": "Ok"}


# Get specific article
@router.get('/{article_id}')
def get_article(article_id: int, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    return {"article": ArticleDisplay.from_orm(db_article.get_article(db, article_id)),
            "current_user": UserDisplaySchema.from_orm(current_user)}


@router.get('/get_by_user_id/{user_id}', response_model=List[Article])
def get_articles_by_user_id(user_id: int, db: Session = Depends(get_db)):
    articles = db_article.get_article_by_user_id(db, user_id)
    print(articles)
    return articles
