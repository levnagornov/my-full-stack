from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')
    
    DATABASE_URL: str
    
    SECRET_KEY: str
    ALGORITHM: str
    
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int
    
    REDIS_HOST: str
    REDIS_PORT: int
    
    CORS_ORIGINS: list[str]
    


settings = Settings()
