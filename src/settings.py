from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic import Field
from sqlalchemy.engine import URL


class ApplicationSettings(BaseSettings):
    app_name: str = 'ByteBiteBurguers'
    debug:   bool = True
    app_host: str = Field(default='0.0.0.0', alias='APP_HOST', title='Application Host Address', description='')
    app_port: int = Field(8000)
    workers:  int = 2


class DatabaseSettings(BaseSettings):
    database_username: str = Field('postgres')
    database_password: str = Field('postgres')
    database_host:     str = Field('localhost')
    database_port:     int = Field(5433)
    database_name:     str = Field('postgres')

    @property
    def unittest_sync_uri(self) -> URL:
        return URL.create(
            drivername='postgresql+psycopg2',
            username=self.database_username, 
            password=self.database_password, 
            host=self.database_host, 
            port=self.database_port, 
            database=self.database_name
            )


class GeneralSettings():
    app_settings = ApplicationSettings()
    database_settings = DatabaseSettings()


@lru_cache
def get_settings() -> GeneralSettings:
    return GeneralSettings()
