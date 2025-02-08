from fastapi import FastAPI
from app.routes.api_controller import router


def app():
    api = FastAPI(title="TCC", version="1.0.0")
    api.include_router(router, tags=["api"])

    return api


server = app()
