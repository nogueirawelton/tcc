from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.controller.api_controller import router


def app():
    api = FastAPI(title='TCC', version='1.0.0')

    api.mount('/public', StaticFiles(directory='app/public'), name='public')
    api.include_router(router, tags=['api'])

    return api


server = app()
