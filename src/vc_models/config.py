import os
from typing import Union

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    POSTGRES_HOST: str = 'localhost'
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = 'vc'
    POSTGRES_USER: str = 'admin'
    POSTGRES_PASSWORD: str = 'admin'

    @property
    def db_url(self):
        return f'postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}/{self.POSTGRES_DB}'


settings = Settings()
