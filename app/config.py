from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    GEMINI_API_KEY: str
    OPENROTER_API_KEY: str

    GEMINI_MODEL_NAME: str
    OPENROUTER_MODEL_NAME: str

    GOOGLE_EMBEDDING_MODEL: str

    CHROMA_DB: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )