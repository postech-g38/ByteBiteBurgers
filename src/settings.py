from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic import Field


class ApplicationSettings(BaseSettings):
    app_name: str = 'ByteBiteBurguers'
    debug:   bool = True
    app_host: str = Field(default='0.0.0.0', alias='APP_HOST', title='Application Host Address', description='')
    app_port: int = Field(8000)
    workers: int = 2


class DatabaseSettings(BaseSettings):
    database_username: str = Field('postgres')
    database_password: str = Field('postgres')
    database_host: str = Field('postgres')
    database_port: int = Field(5432)
    database_name: str = Field('postgres')


class GeneralSettings():
    app_settings = ApplicationSettings()
    database_settings = DatabaseSettings()


@lru_cache
def get_settings() -> GeneralSettings:
    return GeneralSettings()
