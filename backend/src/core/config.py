from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str  
    ALGORITHM: str 
    ACCESS_TOKEN_EXPIRE_MINUTES: int 
    FOLDER_ID: str
    SERVICE_ACCOUNT_FILE: str
    SCOPES: str
    MAKE_WEBHOOK_URL: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        extra = 'forbid'  

settings = Settings()