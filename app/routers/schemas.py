from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserDisplay(BaseModel):
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
