import uvicorn

from src.settings import get_settings
from src.app import app


if __name__ == '__main__':
    uvicorn.run(
        app=app, 
        host=get_settings().application_settings.application_host,
        port=get_settings().application_settings.application_port,
        workers=get_settings().application_settings.workers,
        timeout_graceful_shutdown=get_settings().application_settings.timeout_graceful_shutdown,
    )
    