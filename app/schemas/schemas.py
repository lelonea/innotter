from pydantic import BaseModel, EmailStr


class UserFull(BaseModel):
    """All fields from User model"""
    username: str
    email: EmailStr
    password: str


class UserDisplay(BaseModel):
    """Fields from User model to display after saving User. The password is not displayed"""
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
