"""
Application configuration module.

This module centralizes all environment-driven settings so the rest of the
application does not need to read environment variables directly.
"""
from pathlib import Path

from pydantic import Field
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)

Base_DIR = Path(__file__).resolve().parents[3]
ENV_FILE = Base_DIR / ".env"


class Settings(BaseSettings):
    """
    Strongly typed application settings loaded from environment variables
    and optional .env files.
    """

    app_name: str = Field(default="DevOps Event System API")
    debug: bool = Field(default=False)
    environment: str = Field(default="dev")

    api_host: str = Field(default="0.0.0.0")
    api_port: int = Field(default=8000)

    database_url: str

    log_level: str = Field(default="INFO")

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

settings = Settings()