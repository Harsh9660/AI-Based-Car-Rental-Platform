import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///./car_rental.db"
    openai_api_key: str = ""
    secret_key: str = "your-secret-key"
    
    class Config:
        env_file = ".env"

settings = Settings()