from fastapi import FastAPI, status
from fastapi.staticfiles import StaticFiles
from starlette.responses import JSONResponse

from routers.blog_get import router as router_get
from routers.blog_post import router as router_post
from routers.user import router as router_user
from routers.article import router as router_article
from auth.aunthentication import router as auth_router
from routers.file_routers import router as file_router
from custom_exceptions import NotFoundException, DuplicationException

app = FastAPI()
app.include_router(router_get)
app.include_router(router_post)
app.include_router(router_user)
app.include_router(router_article)
app.include_router(auth_router)
app.include_router(file_router)

app.mount('/files', StaticFiles(directory="files"), name='files')


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


@app.exception_handler(DuplicationException)
def not_found_exception_handler(_, exc: DuplicationException):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "code": status.HTTP_409_CONFLICT,
            "is_error": True,
            "message": exc.message
        },
    )


@app.get('/hello', tags=["utils"])
def index():
    return {'message': 'Hello world!'}
