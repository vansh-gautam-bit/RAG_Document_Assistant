from pathlib import Path

from langchain_community.vectorstores import FAISS

from app.services.embeddings import EmbeddingModel


class VectorStore:

    DB_PATH = "app/db/faiss"

    db = None

    @staticmethod
    def get_embeddings():
        return EmbeddingModel.get_embeddings()

    @staticmethod
    def get_db():

        if VectorStore.db is not None:
            return VectorStore.db

        if Path(VectorStore.DB_PATH).exists():

            print("Loading existing FAISS database...")

            VectorStore.db = FAISS.load_local(
                VectorStore.DB_PATH,
                VectorStore.get_embeddings(),
                allow_dangerous_deserialization=True,
            )

        return VectorStore.db

    @staticmethod
    def add_documents(documents):

        db = VectorStore.get_db()

        if db is None:

            print("Creating new FAISS database...")

            db = FAISS.from_documents(
                documents,
                VectorStore.get_embeddings(),
            )

        else:

            print("Adding documents to existing FAISS database...")

            db.add_documents(documents)

        db.save_local(VectorStore.DB_PATH)

        VectorStore.db = db

        print("FAISS database updated successfully!")