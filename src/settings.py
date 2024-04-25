from functools import lru_cache
from typing import ClassVar
from enum import Enum

from pydantic_settings import BaseSettings
from pydantic import Field
from sqlalchemy.engine import URL


class Env(str, Enum):
    PRD = 'prd'
    UNITTEST = 'unittest'


def execution_environment(env: Env) -> bool:
    return get_settings().application_settings.environment == env.value


class ApplicationSettings(BaseSettings):
    application_name: str = Field(..., validation_alias='APPLICATION_NAME')
    application_host: str = Field(..., validation_alias='APPLICATION_HOST')
    application_port: int = Field(..., validation_alias='APPLICATION_PORT')
    environment: str = Field(..., validation_alias='ENVIRONEMNT')
    workers:  int = Field(..., validation_alias='WORKERS')


class DatabaseSettings(BaseSettings):
    database_username: str = Field(..., validation_alias='DATABASE_USERNAME')
    database_password: str = Field(..., validation_alias='DATABASE_PASSWORD')
    database_host:     str = Field(..., validation_alias='DATABASE_HOST')
    database_port:     int = Field(..., validation_alias='DATABASE_PORT')
    database_name:     str = Field(..., validation_alias='DATABASE_NAME')

    @property
    def unittest_sync_uri(self):
        return ''

    @property
    def sync_uri(self) -> URL:
        return URL.create(
            drivername='postgresql+psycopg2',
            username=self.database_username, 
            password=self.database_password, 
            host=self.database_host, 
            port=self.database_port, 
            database=self.database_name
            )


class GeneralSettings(BaseSettings):
    application_settings: ClassVar = ApplicationSettings()
    database_settings: ClassVar = DatabaseSettings()


@lru_cache
def get_settings() -> GeneralSettings:
    return GeneralSettings()
