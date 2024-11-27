from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from freeline.routers.test import test_router
from freeline.routers.files import file_router
from freeline.routers.chat_bot import bot_router
# from . import db, routers, config


# @asynccontextmanager
# async def lifespan(_: FastAPI):
#     db.BaseSqlModel.metadata.create_all(bind=db.engine)
#     yield


def create_app() -> FastAPI:
    _app = FastAPI(title="API for FreeLine",
                   description="Was created 26-29.11.2024 by MADE_IN_MISIS",
                   version="1.0")
    # lifespan=lifespan,

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["POST", "GET"],
        allow_headers=["*"],
    )

    _app.include_router(test_router)
    _app.include_router(file_router)
    _app.include_router(bot_router)

    return _app
