import os
from pathlib import Path

from dotenv import load_dotenv

__all__ = ["settings"]


class Config:
    # Explicit path to root dir
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    ENV_PATH = BASE_DIR / ".env"

    if not ENV_PATH.exists():
        raise FileNotFoundError(f".env file not found at {ENV_PATH}")

    load_dotenv(ENV_PATH)
    DEBUG = os.getenv("DEBUG", "False").strip().lower() == "true"
    MOCK_DATA = os.getenv("DEBUG", "False").strip().lower() == "true"
    SEO_DATA_API_KEY = os.getenv("SEO_DATA_API_KEY")
    OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")


settings = Config()
