from sqlalchemy.orm.session import Session

from app.schemas.schemas import UserFull
from app.db.models import UserDB
from app.services.hashing import Hash


def create_new_user(db: Session, api_input: UserFull):
    """Saves users data to db"""
    new_user = UserDB(
        username=api_input.username,
        email=api_input.email,
        password=Hash.bcrypt(api_input.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
