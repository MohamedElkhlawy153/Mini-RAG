from pydantic_settings import BaseSettings, SettingsConfigDict

class settings(BaseSettings):
    app_name: str
    app_version: str



    class config:
        env_file = ".env"

def get_settings():
    return settings()

