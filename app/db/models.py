from sqlalchemy import Column, Integer, String

from app.db.database import Base


class UserDB(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
