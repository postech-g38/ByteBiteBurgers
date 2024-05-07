from functools import lru_cache
from typing import ClassVar
from enum import Enum

from pydantic_settings import BaseSettings
from pydantic import Field
from sqlalchemy.engine import URL


class Env(str, Enum):
    PRD = 'prd'
    STG = 'stg'
    HML = 'hml'
    DEV = 'dev'
    UNITTEST = 'unittest'


def execution_environment(env: Env) -> bool:
    return get_settings().application_settings.environment == env.value


class ApplicationSettings(BaseSettings):
    application_name: str = Field(..., validation_alias='APPLICATION_NAME')
    application_host: str = Field(..., validation_alias='APPLICATION_HOST')
    application_port: int = Field(..., validation_alias='APPLICATION_PORT')
    environment: Env = Field(..., validation_alias='ENVIRONEMNT')
    workers: int = Field(..., validation_alias='WORKERS')
    timeout_graceful_shutdown: int = Field(..., validation_alias='TIMEOUT_GRACEFUL_SHUTDOWN')


class DatabaseSettings(BaseSettings):
    database_username: str = Field(..., validation_alias='DATABASE_USERNAME')
    database_password: str = Field(..., validation_alias='DATABASE_PASSWORD')
    database_host: str = Field(..., validation_alias='DATABASE_HOST')
    database_port: int = Field(..., validation_alias='DATABASE_PORT')
    database_name: str = Field(..., validation_alias='DATABASE_NAME')

    @property
    def unittest_sync_uri(self) -> str:
        return 'sqlite:///unittest.db'

    @property
    def sync_uri(self) -> URL:
        return self._build_uri(driver='postgresql', dialect='psycopg2')

    def _build_uri(self, driver: str, dialect: str) -> URL:
        return URL.create(
            drivername=f"{driver}+{dialect}",
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
