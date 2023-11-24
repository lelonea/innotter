from fastapi import FastAPI, status
from starlette.responses import JSONResponse

from src.db import models
from src.db.database import engine
from src.routers.blog_get import router as router_get, NotFoundException
from src.routers.blog_post import router as router_post
from src.routers.user_post import router as router_user_post

app = FastAPI()
app.include_router(router_get)
app.include_router(router_post)
app.include_router(router_user_post)


@app.exception_handler(Exception)
def internal_exception_handler(_, exc: Exception):
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        content={
                            "code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                            "is_error": True,
                            "message": f"An error occurred: {exc}"
                        },
                        )


@app.exception_handler(NotFoundException)
def not_found_exception_handler(_, exc: NotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "code": status.HTTP_404_NOT_FOUND,
            "is_error": True,
            "message": exc.message
        },
    )


@app.get('/hello', tags=["utils"])
def index():
    return {'message': 'Hello world!'}


models.Base.metadata.create_all(engine)
