from langchain_community.vectorstores import FAISS

from app.services.embeddings import EmbeddingModel


class VectorStore:

    db = None

    @staticmethod
    def get_db():
        return VectorStore.db

    @staticmethod
    def add_documents(documents):

        print("Creating FAISS vector store...")

        embeddings = EmbeddingModel.get_embeddings()

        VectorStore.db = FAISS.from_documents(
            documents,
            embeddings,
        )

        print("Documents stored successfully!")