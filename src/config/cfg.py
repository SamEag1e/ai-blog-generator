import os

from dotenv import load_dotenv

__all__ = ["settings"]


class Config:
    load_dotenv()
    DEBUG = os.getenv("DEBUG", "False").strip().lower() == "true"
    MOCK_DATA = os.getenv("MOCK_DATA", "False").strip().lower() == "true"
    SEO_DATA_API_KEY = os.getenv("SEO_DATA_API_KEY")
    OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")


settings = Config()
