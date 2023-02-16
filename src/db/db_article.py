from sqlalchemy.orm.session import Session
from db.models import DbArticle
from schemas import ArticleBase


def create_article(db: Session, payload: ArticleBase):
    new_article = DbArticle(**payload.dict())
    db.add(new_article)
    db.commit()
    return "Ok"


def get_article(db: Session, article_id: int):
    article = db.query(DbArticle).filter(DbArticle.id == article_id).first()
    # Handle errors
    return article

def get_article_by_user_id(db: Session, user_id: int):
    articles = db.query(DbArticle).filter(DbArticle.user_id == user_id).all()
    return articles
