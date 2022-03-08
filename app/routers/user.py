from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm.session import Session
from fastapi.responses import JSONResponse

from app.db.database import get_db
from app.db.db_user import create_new_user
from app.schemas.schemas import UserDisplay, UserFull
from celery_worker import create_task


router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('', response_model=UserDisplay)
def create_user(request: UserFull, db: Session = Depends(get_db)):
    return create_new_user(db, request)


@router.post("/ex1")
def run_task(data=Body(...)):
    amount = int(data["amount"])
    x = data["x"]
    y = data["y"]
    task = create_task.delay(amount, x, y)
    return JSONResponse({"Result": task.get()})
