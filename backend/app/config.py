from pydantic_settings import BaseSettings
from typing import Union

class Settings(BaseSettings):
    app_name: str = "Bulkinskaya"
    debug: bool = True
    database_url: str = "sqlite:///./bulka.db"
    cors_origins: Union[list[str], str] = [
        "http://localhost:5173",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://127.0.0.1:5173",
    ]
    static_dir: str = "static"
    images_dir: str = "static/images"

    class Config:
        env_file  = ".env"

settings = Settings()