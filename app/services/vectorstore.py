from langchain_chroma import Chroma
from app.config import settings
from app.services.embeddings import EmbeddingModel


class VectorStore:

    @staticmethod
    def get_db():
        return Chroma(
            collection_name="rag_documents",
            persist_directory=settings.CHROMA_DB,
            embedding_function=EmbeddingModel.get_embeddings(),
        )

    @staticmethod
    def add_documents(documents):
        print("Opening DB...")
        db = VectorStore.get_db()

        print("Documents:", len(documents))
        print("First chunk:", documents[0].page_content[:50])

        print("Calling add_documents...")
        result = db.add_documents(documents)
        print("Returned from add_documents")

        print(result)