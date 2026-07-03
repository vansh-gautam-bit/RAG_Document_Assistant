from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    GEMINI_API_KEY: str
    OPENROUTER_API_KEY: str  | None = None

    GEMINI_MODEL_NAME: str
    OPENROUTER_MODEL_NAME: str   | None = None

    GOOGLE_EMBEDDING_MODEL: str

    CHROMA_DB: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()