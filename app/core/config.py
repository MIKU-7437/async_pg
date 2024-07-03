from typing import Any
from pydantic import Field, PostgresDsn, validator
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load environment variables from the specified .env file
dotenv_path = os.path.join(os.path.dirname(__file__), 'app', '.env.local')
load_dotenv(dotenv_path)

# Ensure that the environment variables are loaded
load_dotenv()

class Settings(BaseSettings):
    VERSION: str = Field("0.0.1")
    PROJECT_NAME: str = Field("Astrawood")
    POSTGRES_USER: str = Field("postgres", env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field("qwerty", env="POSTGRES_PASSWORD")
    POSTGRES_DB: str = Field("postgres", env="POSTGRES_DB")
    POSTGRES_HOST: str = Field("localhost", env="POSTGRES_HOST")
    POSTGRES_PORT: int = Field(5432, env="POSTGRES_PORT")
    POSTGRES_ECHO: bool = Field(False, env="POSTGRES_ECHO")
    POSTGRES_POOL_SIZE: int = Field(10, env="POSTGRES_POOL_SIZE")
    ASYNC_POSTGRES_URI: str = Field("", env="ASYNC_POSTGRES_URI")

    class Config:
        case_sensitive = True
        env_file = ".env"

    @validator("ASYNC_POSTGRES_URI", pre=True)
    def assemble_db_connection(cls, v: str | None, values: dict[str, Any]) -> str:
        if isinstance(v, str) and v:
            return v
        return f"postgresql+asyncpg://{values['POSTGRES_USER']}:{values['POSTGRES_PASSWORD']}@" \
               f"{values['POSTGRES_HOST']}:{values['POSTGRES_PORT']}/{values['POSTGRES_DB']}"

# Instantiate the settings after loading the environment variables
settings = Settings()

# Test the loaded settings
