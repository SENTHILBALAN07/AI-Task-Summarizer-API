from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SUMMARY_API_URL: str = "https://api.quotable.io/random"

    class Config:
        env_file = ".env"

settings = Settings()
