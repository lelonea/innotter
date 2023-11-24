from fastapi import APIRouter, Depends

from db.database import get_db
from schemas import UserSchema, UserDisplaySchema, UserUpdateSchema
import db.db_user as db_user

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('/new/', response_model=UserDisplaySchema, status_code=201)
def create_user(payload: UserSchema, db=Depends(get_db)):
    return db_user.create_user(db, payload)


@router.get('/all', response_model=list[UserDisplaySchema])
def get_all_users(db=Depends(get_db)):
    return db_user.get_all_users(db)


@router.get('/{user_id}', response_model=UserDisplaySchema)
def get_user(user_id: int, db=Depends(get_db)):
    return db_user.get_user(db, user_id)


@router.patch('/{user_id}')
def update_user(user_id: int, payload: UserUpdateSchema, db=Depends(get_db)):
    return db_user.update_user(db, user_id, payload)

@router.delete('/{user_id}')
def delete_user(user_id: int, db=Depends(get_db)):
    return db_user.delete_user(db, user_id)
