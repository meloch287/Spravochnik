from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Spravochnik API"
    database_url: str = "sqlite:///./test.db"

settings = Settings()