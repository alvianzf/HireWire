from pydantic_settings import BaseSettings
from pathlib import Path
from dotenv import load_dotenv
import os
import sys

env_path = Path(__file__).parent.parent / ".env"
if env_path.exists():
    load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    apify_token: str

    class Config:
        env_prefix = ""
        env_file = env_path
        env_file_encoding = "utf-8"

    @classmethod
    def load(cls):
        try:
            settings = cls()
        except Exception as e:
            print("ERROR: Failed to load settings. Make sure APIFY_TOKEN is set in environment or .env file.")
            print(f"DETAILS: {e}")
            sys.exit(1)
        return settings
