from langchain_chroma import Chroma
from app.config import settings

from app.services.embeddings import EmbeddingModel

class VectorStore:

    @staticmethod
    def get_db():
        return Chroma(
            persist_directory=settings.CHROMA_DB,
            embedding_function=EmbeddingModel.get_embeddings()
        )
    
    @staticmethod
    def add_documents(documents):
        db =VectorStore.get_db()
        db.add_documents(documents)