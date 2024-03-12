from fastapi import FastAPI

from src.settings import get_settings
from src.routes import health_check_router, v1_router

from src.adapters.database.settings import run_migrations


def create_app() -> FastAPI:
    run_migrations()
    
    _app = FastAPI(
        title=get_settings().app_settings.app_name,
        debug=get_settings().app_settings.debug,
    )
    _app.include_router(health_check_router)
    _app.include_router(v1_router)
    return _app


app = create_app()
