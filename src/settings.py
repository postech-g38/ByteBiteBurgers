from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic import Field


class ApplicationSettings(BaseSettings):
    app_name: str = 'ByteBiteBurguers'
    debug:   bool = True
    app_host: str = Field('0.0.0.0', env='APP_HOST')
    app_port: int = Field(8000,      env='APP_PORT')


class GeneralSettings():
    app_settings = ApplicationSettings()


@lru_cache()
def get_settings() -> GeneralSettings:
    return GeneralSettings()
