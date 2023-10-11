from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic import Field


class ApplicationSettings(BaseSettings):
    app_name: str = 'ByteBiteBurguers'
    debug:   bool = True
    app_host: str = Field('0.0.0.0', env='APP_HOST')
    app_port: int = Field(8000,      env='APP_PORT')
    workers: int = 2


class DatabaseSettings(BaseSettings):
    database_username: str
    database_password: str
    database_host: str
    database_port: int
    database_name: str


class GeneralSettings():
    app_settings = ApplicationSettings()
    database_settings = DatabaseSettings()


@lru_cache
def get_settings() -> GeneralSettings:
    return GeneralSettings()
