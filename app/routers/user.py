from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from app.db.database import get_db
from app.db.db_user import create_new_user
from app.routers.schemas import UserDisplay, UserBase


router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return create_new_user(db, request)
