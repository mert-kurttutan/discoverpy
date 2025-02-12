from pydantic_settings import BaseSettings
from pydantic import (
    AnyUrl,
    BeforeValidator,
    HttpUrl,
    PostgresDsn,
    computed_field,
    model_validator,
)
import os
# loadenv
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    POSTGRES_USER: str = "discover"
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "testdiscover"
    @computed_field  # type: ignore[prop-decorator]
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+psycopg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )
    @staticmethod
    def from_env() -> "Settings":
        postgres_user = os.getenv("POSTGRES_USER")
        postgres_password = os.getenv("POSTGRES_PASSWORD")
        postgres_host = os.getenv("POSTGRES_HOST")
        postgres_port = os.getenv("POSTGRES_PORT")
        postgres_db = os.getenv("POSTGRES_DB")
        return Settings(
            POSTGRES_USER=postgres_user,
            POSTGRES_PASSWORD=postgres_password,
            POSTGRES_HOST=postgres_host,
            POSTGRES_PORT=postgres_port,
            POSTGRES_DB=postgres_db,
        )
    


settings = Settings.from_env()