import uvicorn

from src.settings import get_settings
from app import app


if __name__ == '__main__':
    uvicorn.run(
        app, 
        host=get_settings().app_settings.app_host,
        port=get_settings().app_settings.app_port
    )
    