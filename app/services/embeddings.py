from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.config import settings

class EmbeddingModel:

    @staticmethod
    def get_embeddings():
        return GoogleGenerativeAIEmbeddings(
            model=settings.GOOGLE_EMBEDDING_MODEL,
            google_api_key=settings.GEMINI_API_KEY,
        )