from fastapi import FastAPI
import os

from src.settings import get_settings
from src.routes import health_check_router, v1_router

from src.adapters.database.settings import run_migrations


def create_app() -> FastAPI:
    _app = FastAPI(
        title=get_settings().application_settings.application_name
    )
    _app.include_router(health_check_router)
    _app.include_router(v1_router)
    return _app


app = create_app()
