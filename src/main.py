import uvicorn

from src.settings import get_settings
from src.app import app


if __name__ == '__main__':
    uvicorn.run(
        app=app, 
        host=get_settings().app_settings.app_host,
        port=get_settings().app_settings.app_port
    )
    