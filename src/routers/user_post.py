from fastapi import APIRouter, Depends

from src.db.database import get_db
from src.schemas import UserSchema

router = APIRouter(
    prefix='/user',
    tags=['user']
)
#
#
# @router.post('/new/')
# def create_user(payload: UserSchema, db=Depends(get_db)):
#
#     db.add(payload.dict())
#     db.commit()
#     return "Ok"
