import os
import sys
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from loguru import logger

class Settings(BaseSettings):
    app_name: str = "etl-kaggle"
    dataset: str
    extension: str = "csv"
    log_level: str = "INFO"
    log_file: str = "logs/app.log"
    data_path: Path = Path("./data/")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()

logger.remove()

logger.add(
    sys.stdout,
    level=settings.log_level,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
)

logger.add(
    settings.log_file,
    level="DEBUG",
    rotation="10 MB",
    retention="10 days",
    compression="zip"
)

KAGGLE_CACHE_DIR = settings.data_path / "raw"
BRONZE_DIR = settings.data_path / "bronze"
SILVER_DIR = settings.data_path / "silver"
GOLD_DIR = settings.data_path / "gold"

for path in [KAGGLE_CACHE_DIR,BRONZE_DIR,SILVER_DIR,GOLD_DIR]:
    path.mkdir(parents=True,exist_ok=True)

os.environ["KAGGLEHUB_CACHE"] = str(KAGGLE_CACHE_DIR)