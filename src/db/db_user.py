from db.hash import Hash
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError
from schemas import UserSchema, UserUpdateSchema
from db.models import DbUser
from custom_exceptions import NotFoundException, DuplicationException


def create_user(db: Session, payload: UserSchema):
    try:
        new_user = DbUser(
            username=payload.username,
            email=payload.email,
            password=Hash.bcrypt(payload.password)
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError as ie:
        if "Duplicate entry" in ie.orig.args[1]:
            raise DuplicationException(ie.orig.args[1])


def get_all_users(db: Session):
    return db.query(DbUser).all()


def get_user(db: Session, user_id: int):
    resp = db.query(DbUser).filter(DbUser.id == user_id).first()
    if not resp:
        raise NotFoundException(f"User with id {user_id} not found")


def update_user(db: Session, user_id: int, payload: UserUpdateSchema):
    try:
        user = db.query(DbUser).filter(DbUser.id == user_id)
        payload.password = Hash.bcrypt(payload.password)
        user.update(payload.dict(exclude_unset=True))
        db.commit()
        return {"message": "User updated successfully"}
    except IntegrityError as ie:
        if "Duplicate entry" in ie.orig.args[1]:
            raise DuplicationException(ie.orig.args[1])


def delete_user(db: Session, user_id: int):
    user = db.query(DbUser).filter(DbUser.id == user_id).first()
    if not user:
        raise NotFoundException(f"User with id {user_id} not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}


def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise NotFoundException(f'User with username {username} not found')
    return user
