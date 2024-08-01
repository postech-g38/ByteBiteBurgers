import asyncio

from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.settings import get_settings
from src.routes import health_check_router, v1_router
from src.adapters.queue.settings import AwsSQS

queue = AwsSQS(url=get_settings().queue_settings.queue_url)


@asynccontextmanager
async def lifespan(app: FastAPI):
    
    asyncio.create_task(queue.exec())
    # loop = asyncio.get_event_loop()
    # loop.create_task(queue.exec())
    yield


def create_app() -> FastAPI:
    _app = FastAPI(
        title=get_settings().application_settings.application_name,
        lifespan=lifespan
    )
    _app.include_router(health_check_router)
    _app.include_router(v1_router)
    return _app


app = create_app()
