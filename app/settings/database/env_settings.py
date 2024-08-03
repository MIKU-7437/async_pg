from pydantic_settings import BaseSettings
from pydantic import Field
from dataclasses import dataclass
import os


class EnvSettings(BaseSettings):
    POSTGRES_USER:str = Field(..., env='POSTGRES_USER')
    POSTGRES_PASSWORD: str = Field(..., env='POSRGES_PASSWORD')
    POSTGRES_DB:str = Field(..., env='POSTGRES_DB')
    POSTGRES_HOST:str = Field(..., env='POSTGRES_HOST')
    POSTGRES_PORT:str = Field(..., env='POSTGRES_PORT')
    POSTGRES_ECHO:str = Field(..., env='POSTGRES_ECHO')
    POSTGRES_POOL_SIZE:str = Field(..., env='POSTGRES_POOL_SIZE')

    SECRET_KEY:str = Field(..., env='SECRET_KEY')

    class Config():
        env_file = os.path.join(os.path.dirname(__file__), '../../.env.local')
        extra = 'ignore'

env_settings = EnvSettings()


@dataclass
class PostgresConfig():
    POSTGRES_USER: str = env_settings.POSTGRES_USER
    POSTGRES_PASSWORD: str = env_settings.POSTGRES_PASSWORD
    POSTGRES_DB: str = env_settings.POSTGRES_DB
    POSTGRES_HOST: str = env_settings.POSTGRES_HOST
    POSTGRES_PORT: str = env_settings.POSTGRES_PORT
    POSTGRES_ECHO: str = env_settings.POSTGRES_ECHO
    POSTGRES_POOL_SIZE: str = env_settings.POSTGRES_POOL_SIZE


@dataclass
class AppCpnfig():
    SECRET_KEY: str = env_settings.SECRET_KEY
